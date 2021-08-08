import tempfile

from robot.libdocpkg.model import LibraryDoc

from rfdocsindexer.models import (
    ExternalResource,
    IndexedRFLibrary,
    RFKeyword,
    RFKeywordArg,
    RFLibdata,
    RFLibrary,
)

rfkeywordarg1 = RFKeywordArg(repr="arg1: str")
rfkeywordarg2 = RFKeywordArg(repr="arg2: str")
rfkeyword1 = RFKeyword(
    name="kw1",
    args=[rfkeywordarg1, rfkeywordarg2],
    shortdoc="shortdoc",
)
rfkeyword2 = RFKeyword(
    name="kw2",
    args=[rfkeywordarg1, rfkeywordarg2],
    shortdoc="shortdoc",
)
with tempfile.NamedTemporaryFile(suffix=".py") as tmpfile:
    rflibrary1 = RFLibrary(
        name="lib1",
        keywords=[rfkeyword1, rfkeyword2],
        version="0.1.2",
        tags=["tag1", "tag2"],
        source=tmpfile.name,
    )
    rflibrary2 = RFLibrary(
        name="lib2",
        keywords=[rfkeyword1, rfkeyword2],
        version="0.1.2",
        tags=["tag1", "tag2"],
        source=tmpfile.name,
    )
rflibdata1 = RFLibdata(imported_by="name", libdoc=LibraryDoc(), rflibrary=rflibrary1)
rflibdata2 = RFLibdata(imported_by="name", libdoc=LibraryDoc(), rflibrary=rflibrary2)
with tempfile.NamedTemporaryFile(suffix=".html") as tmpfile:
    indexedlib1 = IndexedRFLibrary(
        html_libdoc_path=tmpfile.name,
        xml_libdoc_path=None,
        json_libdoc_path=None,
        libspec_path=None,
        libdata=rflibdata1,
    )
    indexedlib2 = IndexedRFLibrary(
        html_libdoc_path=tmpfile.name,
        xml_libdoc_path=None,
        json_libdoc_path=None,
        libspec_path=None,
        libdata=rflibdata2,
    )
external1 = ExternalResource(
    url="http://example.com/",
    name="external1",
)
external2 = ExternalResource(
    url="http://example.com/",
    name="external2",
)

output_libdocs_html_name = "libdocs_html"
output_libdocs_json_name = "libdocs_json"
output_libdocs_xml_name = "libdocs_xml"
output_libdocs_specs_name = "libspecs"
