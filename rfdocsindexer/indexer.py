import copy
import shutil
import sys
from glob import glob
from pathlib import Path
from typing import List, Optional, Union
from urllib.parse import quote, urlparse

import jinja2
from robot.errors import DataError
from robot.libdocpkg.builder import DocumentationBuilder
from robot.libdocpkg.model import LibraryDoc

from .config import Config
from .models import ExternalResource, IndexedRFLibrary, RFLibdata, RFLibrary

HTML_LIBDOC_DIR = "libdocs_html"
XML_LIBDOC_DIR = "libdocs_xml"
JSON_LIBDOC_DIR = "libdocs_json"
LIBSPEC_DIR = "libspecs"


def _expand_and_filter_filepaths(library_paths: List[str]) -> List[Path]:
    """
    Expands the given library paths and keeps the paths to a filename.

    Args:
        library_paths (list[str]): The paths to expand.
    Returns:
        list[pathlib.Path]: The expanded paths.
    """
    valid_paths: List[Path] = []

    for library_path in library_paths:
        expended_paths = glob(library_path, recursive=True)
        if len(expended_paths) == 0:
            print(f'Warning: No file found at path "{library_path}"')
            continue

        for str_path in expended_paths:
            pathlib_path = Path(str_path)

            # If the path is a file, append it to the list
            if pathlib_path.is_file():
                valid_paths += [pathlib_path]

    return valid_paths


def _get_libdoc_from_libname_or_path(
    library_name_or_path: Union[str, Path]
) -> LibraryDoc:
    """
    Return a LibraryDoc object from the given library name or path.

    Args:
        library_name_or_path (str or pathlib.Path): The library to generate the
            documentation for.

    Returns:
        LibraryDoc: A libdoc object.

    Raises:
        RuntimeError: If an error occurs during process.
    """
    if isinstance(library_name_or_path, Path):
        library_name_or_path = str(library_name_or_path)
    try:
        return DocumentationBuilder(library_name_or_path).build(library_name_or_path)
    except DataError as err:
        raise RuntimeError(
            f'Error generating documentation for library "{library_name_or_path}": '
            f"{err}"
        )


def _create_rflibdata_object_from_libname_or_path(
    libname_or_path: Union[str, Path]
) -> RFLibdata:
    """
    Creates a RFLibdata object from the given library name or path.

    Args:
        libname_or_path (str or pathlib.Path): The library to generate the
            documentation for.

    Returns:
        RFLibdata: A libdata object.
    """
    # Run libdoc to get the JSON object from the library
    libdoc = _get_libdoc_from_libname_or_path(str(libname_or_path))
    json_lib_obj = libdoc.to_dictionary()
    rflib = RFLibrary.parse_obj(json_lib_obj)

    return RFLibdata(
        imported_by="name" if isinstance(libname_or_path, str) else "path",
        libdoc=libdoc,
        rflibrary=rflib,
    )


def _get_libs_from_paths(library_paths: List[str]) -> List[RFLibdata]:
    """
    Find the libraries in the given paths.

    Args:
        library_paths (list[str]): The paths (glob) to search for libraries.

    Returns:
        list[RFLibdata]: The libraries found.

    Raises:
        RuntimeError: If an error occurs during the library search process.
    """
    libraries: List[RFLibdata] = []

    paths = _expand_and_filter_filepaths(library_paths)
    for libpath in paths:
        libraries += [_create_rflibdata_object_from_libname_or_path(libpath)]

    return libraries


def _get_libs_from_names(
    library_names: List[str], extra_modules_searchpaths: List[Path]
) -> List[RFLibdata]:
    """
    Find the libraries with the given name.

    Args:
        library_names (list[str]): The name of the library to search for.
        extra_pythonpath (list[Path]): The extra modules search paths
            to add to the PYTHONPATH.

    Returns:
        list[RFLibdata]: The libraries found.

    Raises:
        RuntimeError: If an error occurs during the library search process.
    """
    libraries: List[RFLibdata] = []

    # Append extra python paths to the pythonpath
    sys.path.extend(list(map(str, extra_modules_searchpaths)))

    for libname in library_names:
        libraries += [_create_rflibdata_object_from_libname_or_path(libname)]

    return libraries


def _index_external_resources(urls: List[str]) -> List[ExternalResource]:
    """
    Index the given URLs as external resources.

    Args:
        urls (list[str]): The URLs to be indexed.

    Returns:
        list[ExternalResource]: The indexed resources.

    Raises:
        RuntimeError: If an error occurs during the indexing process.
    """
    ext_resources: List[ExternalResource] = []

    if len(urls) == 0:
        return []

    for raw_url in urls:

        # Extract url components (can be "name | http://example")
        name_delimiter = " | "
        name: str = raw_url
        url: str = raw_url

        try:
            if raw_url.count(name_delimiter) > 1:
                raise ValueError
            if name_delimiter in raw_url:
                name, url = list(map(str.strip, raw_url.split(name_delimiter)))

            parsed_url = urlparse(url)
            if not parsed_url.netloc or not parsed_url.scheme:
                raise ValueError

        except ValueError:
            raise RuntimeError(f'Url format is invalid for url "{url}"')

        ext_resources += [ExternalResource(url=url, name=name)]

    print("Indexed external resources")

    return ext_resources


def _gen_index_file(
    indexed_libs: List[IndexedRFLibrary],
    external_resources: List[ExternalResource],
    output_dir: Path,
) -> None:
    """
    Generate the index file.

    Args:
        indexed_libs (list[IndexedRFLibrary]): The indexed libraries.
        external_resources (list[ExternalResource]): The external resources.
        output_dir (pathlib.Path): The output directory.
    """
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(Path(__file__).parent / "templates"),
    )
    env.filters["quote"] = lambda x: quote(x.encode("UTF-8"), safe="-_.!~*'()")
    env.filters["rmdot"] = lambda x: x.replace(".", "")
    with open(output_dir / "index.html", "w") as f:
        f.write(
            env.get_template("index.html").render(
                dirpath=output_dir,
                indexed_libs=indexed_libs,
                external_resources=external_resources,
            )
        )


def _prepare_output_directories(
    output_dir: Path,
    gen_machine_readable_libdocs: bool,
) -> None:
    """
    Clean and mkdir the output directories.

    Args:
        output_dir (pathlib.Path): The output directory.
        gen_machine_readable_libdocs (bool): Whether to generate machine readable
            libdocs.

    Raises:
        RuntimeError: If an error occurs during the directory preparation process.
    """
    output_subdirs_to_prepare = [HTML_LIBDOC_DIR]
    if gen_machine_readable_libdocs:
        output_subdirs_to_prepare += [XML_LIBDOC_DIR, JSON_LIBDOC_DIR, LIBSPEC_DIR]

    for output_subdir in output_subdirs_to_prepare:
        full_output_dir = output_dir / output_subdir
        try:
            if full_output_dir.exists():
                shutil.rmtree(full_output_dir)
            full_output_dir.mkdir(parents=True)
        except (PermissionError, OSError) as err:
            raise RuntimeError(f"Error when creating output directories: {err}")


def _generate_libdocs(
    libraries: List[RFLibdata],
    gen_machine_readable_libdocs: bool,
    output_dir: Path,
) -> List[IndexedRFLibrary]:
    """
    Generate the libdocs for the given libraries.

    Args:
        libraries (list[RFLibdata]): The libraries to be documented.
        gen_machine_readable_libdocs (bool): Whether to generate machine
            readable libdocs.
        output_dir (pathlib.Path): The output directory.

    Returns:
        list[IndexedRFLibrary]: The indexed libdocs.
    """
    indexed_libraries: List[IndexedRFLibrary] = []

    _prepare_output_directories(output_dir, gen_machine_readable_libdocs)

    for lib in libraries:
        libdoc_html = copy.deepcopy(lib.libdoc)
        libdoc_html.convert_docs_to_html()

        html_filepath = output_dir / HTML_LIBDOC_DIR / (lib.name + ".html")
        libdoc_html.save(html_filepath, "HTML")

        xml_filepath: Optional[Path] = None
        json_filepath: Optional[Path] = None
        if gen_machine_readable_libdocs:
            libdoc_robot = copy.deepcopy(lib.libdoc)

            xml_filepath = output_dir / XML_LIBDOC_DIR / (lib.name + ".xml")
            libdoc_robot.save(xml_filepath, "XML")

            json_filepath = output_dir / JSON_LIBDOC_DIR / (lib.name + ".json")
            libdoc_robot.save(json_filepath, "JSON")

            libspec_filepath = output_dir / LIBSPEC_DIR / (lib.name + ".spec")
            libdoc_html.save(libspec_filepath, "LIBSPEC")

        indexed_libraries += [
            IndexedRFLibrary(
                html_libdoc_path=html_filepath,
                xml_libdoc_path=xml_filepath,
                json_libdoc_path=json_filepath,
                libdata=lib.copy(deep=True),
            )
        ]

        print(f'Generated doc for "{lib.name}"')

    return indexed_libraries


def index_documentation(config: Config, output_dir: Path) -> None:
    """
    Indexes the RF documentation according to the config file.

    The documentation will be generated in the output_dir.

    Args:
        config (.config.Config): The configuration object.
        output_dir (pathlib.Path): The output directory.

    Raises:
        RunTimeError: If an error occurs during the indexing process.
    """

    libraries = []
    libraries.extend(_get_libs_from_paths(config.library_paths))
    libraries.extend(
        _get_libs_from_names(config.library_names, config.extra_modules_searchpaths)
    )
    indexed_libs = _generate_libdocs(
        libraries,
        gen_machine_readable_libdocs=config.build_machine_readable_libdoc,
        output_dir=output_dir,
    )
    external_resources = _index_external_resources(config.external_resources)
    _gen_index_file(indexed_libs, external_resources, output_dir)
