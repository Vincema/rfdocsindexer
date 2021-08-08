import functools
from typing import List, Optional

from pydantic import AnyUrl, BaseModel, FilePath
from robot.libdocpkg.model import LibraryDoc
from typing_extensions import Literal


class RFKeywordArg(BaseModel):
    """
    Dataclass representing a keyword argument.
    """

    repr: str


@functools.total_ordering
class RFKeyword(BaseModel):
    """
    Dataclass representing a keyword in a library.
    """

    name: str
    args: List[RFKeywordArg]
    shortdoc: str

    def __eq__(self, other: object) -> bool:
        assert isinstance(other, RFKeyword), "Must compare RFKeyword to RFKeyword"
        return self.name == other.name

    def __gt__(self, other: object) -> bool:
        assert isinstance(other, RFKeyword), "Must compare RFKeyword to RFKeyword"
        return self.name > other.name


@functools.total_ordering
class RFLibrary(BaseModel):
    """
    Dataclass representing a RF library.
    """

    name: str
    keywords: List[RFKeyword]
    version: str
    tags: List[str]
    source: FilePath

    def __eq__(self, other: object) -> bool:
        assert isinstance(other, RFLibrary), "Must compare RFLibrary to RFLibrary"
        return self.name == other.name

    def __gt__(self, other: object) -> bool:
        assert isinstance(other, RFLibrary), "Must compare RFLibrary to RFLibrary"
        return self.name > other.name


@functools.total_ordering
class RFLibdata(BaseModel):
    """
    Dataclass representing a RF library data for this app.
    """

    imported_by: Literal["name", "path"]
    libdoc: LibraryDoc
    rflibrary: RFLibrary

    @property
    def name(self) -> str:
        return self.rflibrary.name

    class Config:
        arbitrary_types_allowed = True

    def __eq__(self, other: object) -> bool:
        assert isinstance(other, RFLibdata), "Must compare RFLibdata to RFLibdata"
        return self.name == other.name

    def __gt__(self, other: object) -> bool:
        assert isinstance(other, RFLibdata), "Must compare RFLibdata to RFLibdata"
        return self.name > other.name


@functools.total_ordering
class IndexedRFLibrary(BaseModel):
    """
    Dataclass representing a RF library that has been indexed.
    """

    html_libdoc_path: FilePath
    xml_libdoc_path: Optional[FilePath]
    json_libdoc_path: Optional[FilePath]
    libspec_path: Optional[FilePath]
    libdata: RFLibdata

    @property
    def name(self) -> str:
        return self.libdata.name

    def __eq__(self, other: object) -> bool:
        assert isinstance(
            other, IndexedRFLibrary
        ), "Must compare IndexedRFLibrary to IndexedRFLibrary"
        return self.name == other.name

    def __gt__(self, other: object) -> bool:
        assert isinstance(
            other, IndexedRFLibrary
        ), "Must compare IndexedRFLibrary to IndexedRFLibrary"
        return self.name > other.name


@functools.total_ordering
class ExternalResource(BaseModel):
    """
    Dataclass representing an external resource.
    """

    name: str
    url: AnyUrl

    def __eq__(self, other: object) -> bool:
        assert isinstance(
            other, ExternalResource
        ), "Must compare ExternalResource to ExternalResource"
        return self.name == other.name

    def __gt__(self, other: object) -> bool:
        assert isinstance(
            other, ExternalResource
        ), "Must compare ExternalResource to ExternalResource"
        return self.name > other.name
