import io
import shutil
import sys
from contextlib import redirect_stdout
from glob import glob
from pathlib import Path
from typing import List, Literal, Optional, Union

import jinja2
from robot.libdoc import libdoc

from .config import Config
from .models import RFLibrary, IndexedLib, ExternalResource

HTML_LIBDOC_DIR = "libdocs_html"
XML_LIBDOC_DIR = "libdocs_xml"
JSON_LIBDOC_DIR = "libdocs_json"


def _expand_and_keep_filepaths(library_paths: List[str]) -> List[Path]:
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
            print(f'❗ Warning: No file found at path "{library_path}"')

        for str_path in expended_paths:
            pathlib_path = Path(str_path)

            # If the path is a file, append it to the list
            if pathlib_path.is_file():
                valid_paths += [pathlib_path]

    return valid_paths


def _run_libdoc(
    library_name_or_path: Union[str, Path],
    file_type: Literal["HTML", "XML", "JSON"],
    output_file: Path,
) -> None:
    """
    Runs libdoc on the given library.

    Args:
        library_name_or_path (str or pathlib.Path): The library to generate the
            documentation for.
        file_type (str): The file type to generate.
        output_file (pathlib.Path): The output file.

    Raises:
        RunTimeError: If an error occurs during the generation process.
    """
    with redirect_stdout(io.StringIO()):
        ret = libdoc(str(library_name_or_path), str(output_file), format=file_type)

    if ret != 0:
        raise RuntimeError(
            f"RF libdoc failed to generate the {file_type} documentation for "
            f'library "{library_name_or_path}"'
        )


def _get_libs_from_paths(library_paths: List[Union[str, Path]]) -> List[RFLibrary]:
    """
    Find the libraries in the given paths.

    Args:
        library_paths (list[str or pathlib.Path]): The paths to search for libraries.

    Returns:
        list[IndexedLib]: The indexed libraries.

    Raises:
        RuntimeError: If an error occurs during the library search process.
    """
    paths = _expand_and_keep_filepaths(library_paths)

    found_libraries: List[IndexedLib] = []


def _gen_doc_from_paths(
    library_paths: List[str],
    output_dir_html: Optional[Path],
    output_dir_xml: Optional[Path],
    output_dir_json: Optional[Path],
) -> List[IndexedFile]:
    """
    Walk the given paths and generate the RF docs.

    Args:
        library_paths (list[str]): The paths (glob style) to the libraries
            to be documented.
        output_dir_html (optional, pathlib.Path): The output directory for HTML libdocs.
        output_dir_xml (optional, pathlib.Path): The output directory for XML libdocs.
        output_dir_json (optional, pathlib.Path): The output directory for JSON libdocs.

    Returns:
        list[IndexedFile]: The indexed files.

    Raises:
        RunTimeError: If an error occurs during the generation process.
    """
    if output_dir_html is None and output_dir_xml is None and output_dir_json is None:
        return []

    paths = _expand_and_keep_filepaths(library_paths)
    generated_files: List[IndexedFile] = []

    for path in paths:
        libname = path.stem

        # Generate the HTML documentation
        if output_dir_html is not None:
            output_html_filepath = output_dir_html / (libname + ".html")
            _run_libdoc(path, "HTML", output_html_filepath)
            generated_files += [
                IndexedFile(
                    creation_path=output_html_filepath,
                    from_path=True,
                    origin=path,
                    file_type=FileTypeEnum.HTML_LIBDOC,
                    name=libname,
                )
            ]

        # Generate the XML documentation
        if output_dir_xml is not None:
            output_xml_filepath = output_dir_xml / (libname + ".xml")
            _run_libdoc(path, "XML", output_xml_filepath)
            generated_files += [
                IndexedFile(
                    creation_path=output_xml_filepath,
                    from_path=True,
                    origin=path,
                    file_type=FileTypeEnum.XML_LIBDOC,
                    name=libname,
                )
            ]

        # Generate the JSON documentation
        if output_dir_json is not None:
            output_json_filepath = output_dir_json / (libname + ".json")
            _run_libdoc(path, "JSON", output_json_filepath)
            generated_files += [
                IndexedFile(
                    creation_path=output_json_filepath,
                    from_path=True,
                    origin=path,
                    file_type=FileTypeEnum.JSON_LIBDOC,
                    name=libname,
                )
            ]
        print(f'🤖 Generated doc for "{libname}"')

    return generated_files


def _gen_doc_from_names(
    library_names: List[str],
    extra_pythonpath: List[Path],
    output_dir_html: Optional[Path],
    output_dir_xml: Optional[Path],
    output_dir_json: Optional[Path],
) -> List[IndexedFile]:
    """
    Generate the RF docs for the given library names.

    Args:
        library_names (list[str]): The names of the libraries to be documented.
        output_dir_html (optional, pathlib.Path): The output directory for HTML libdocs.
        output_dir_xml (optional, pathlib.Path): The output directory for XML libdocs.
        output_dir_json (optional, pathlib.Path): The output directory for JSON libdocs.

    Returns:
        list[IndexedFile]: The indexed files.
    """
    if output_dir_html is None and output_dir_xml is None and output_dir_json is None:
        return []

    # Append extra python paths to the pythonpath
    sys.path.extend(list(map(str, extra_pythonpath)))

    generated_files: List[IndexedFile] = []

    for libname in library_names:
        # Generate the HTML documentation
        if output_dir_html is not None:
            # Get the library name if separated by a dot: "modulename.classname"
            class_libname = libname.split(".")[-1]

            output_html_filepath = output_dir_html / (class_libname + ".html")
            _run_libdoc(libname, "HTML", output_html_filepath)
            generated_files += [
                IndexedFile(
                    creation_path=output_html_filepath,
                    from_name=True,
                    origin=libname,
                    file_type=FileTypeEnum.HTML_LIBDOC,
                    name=libname,
                )
            ]

        # Generate the XML documentation
        if output_dir_xml is not None:
            output_xml_filepath = output_dir_xml / (libname + ".xml")
            _run_libdoc(libname, "XML", output_xml_filepath)
            generated_files += [
                IndexedFile(
                    creation_path=output_xml_filepath,
                    from_name=True,
                    origin=libname,
                    file_type=FileTypeEnum.XML_LIBDOC,
                    name=libname,
                )
            ]

        # Generate the JSON documentation
        if output_dir_json is not None:
            output_json_filepath = output_dir_json / (libname + ".json")
            _run_libdoc(libname, "JSON", output_json_filepath)
            generated_files += [
                IndexedFile(
                    creation_path=output_json_filepath,
                    from_name=True,
                    origin=libname,
                    file_type=FileTypeEnum.JSON_LIBDOC,
                    name=libname,
                )
            ]
        print(f'🤖 Generated doc for "{libname}"')

    return generated_files


def _index_external_resources(urls: List[str]) -> List[IndexedFile]:
    """
    Index the given URLs as external resources.

    Args:
        urls (list[str]): The URLs to be indexed.

    Raises:
        RuntimeError: If an error occurs during the indexing process.
    """
    ext_resources: List[IndexedFile] = []

    for url in urls:

        # Extract url components (can be "name | http://example")
        name_delimiter = " | "
        name: str = url
        origin: str = url
        if url.count(name_delimiter) > 1:
            raise RuntimeError(f'Url format is invalid for url "{url}"')
        if name_delimiter in url:
            name, origin = list(map(str.strip, url.split(name_delimiter)))
        if not all((name, origin)):
            raise RuntimeError(f'Url format is invalid for url "{url}"')

        ext_resources += [
            IndexedFile(
                from_url=True, origin=origin, file_type=FileTypeEnum.EXT_DOC, name=name
            )
        ]

    if len(ext_resources) > 0:
        print("🌐 Indexed external resources")

    return ext_resources


def _gen_index_file(
    generated_docs: List[IndexedFile],
    title: str,
    output_dir: Path,
) -> None:
    """
    Generate the index file.

    Args:
        generated_docs (list[IndexedFile]): The indexed files.
        output_dir (pathlib.Path): The output directory.
    """
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(Path(__file__).parent / "templates"),
    )
    with open(output_dir / "index.html", "w") as f:
        f.write(
            env.get_template("index.html").render(
                filepath=output_dir,
                title=title,
                html_libdocs=list(
                    filter(
                        lambda x: x.file_type == FileTypeEnum.HTML_LIBDOC,
                        generated_docs,
                    )
                ),
                ext_resources=list(
                    filter(
                        lambda x: x.file_type == FileTypeEnum.EXT_DOC,
                        generated_docs,
                    )
                ),
            )
        )


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
    # Paths to the generated libdoc
    if config.generate_html_libdoc:
        libdocs_html_dirpath = output_dir / "libdocs_html"
        if libdocs_html_dirpath.exists():
            shutil.rmtree(libdocs_html_dirpath)
        libdocs_html_dirpath.mkdir(parents=True)

    if config.generate_xml_libdoc:
        libdocs_xml_dirpath = output_dir / "libdocs_xml"
        if libdocs_xml_dirpath.exists():
            shutil.rmtree(libdocs_xml_dirpath)
        libdocs_xml_dirpath.mkdir(parents=True)

    if config.generate_json_libdoc:
        libdocs_json_dirpath = output_dir / "libdocs_json"
        if libdocs_json_dirpath.exists():
            shutil.rmtree(libdocs_json_dirpath)
        libdocs_json_dirpath.mkdir(parents=True)

    generated_docs: List[IndexedFile] = []

    # Generate the documentation
    generated_docs.extend(
        _gen_doc_from_paths(
            library_paths=config.library_paths,
            output_dir_html=libdocs_html_dirpath
            if config.generate_html_libdoc
            else None,
            output_dir_xml=libdocs_xml_dirpath if config.generate_xml_libdoc else None,
            output_dir_json=libdocs_json_dirpath
            if config.generate_json_libdoc
            else None,
        )
    )

    generated_docs.extend(
        _gen_doc_from_names(
            library_names=config.library_names,
            extra_pythonpath=config.extra_pythonpath,
            output_dir_html=libdocs_html_dirpath
            if config.generate_html_libdoc
            else None,
            output_dir_xml=libdocs_xml_dirpath if config.generate_xml_libdoc else None,
            output_dir_json=libdocs_json_dirpath
            if config.generate_json_libdoc
            else None,
        )
    )

    generated_docs.extend(_index_external_resources(config.external_resources))

    # Write the index file
    _gen_index_file(
        generated_docs=generated_docs,
        title=config.index_title,
        output_dir=output_dir,
    )
