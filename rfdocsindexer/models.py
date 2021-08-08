from typing import List, Literal, Optional

from pydantic import AnyUrl, BaseModel, FilePath


ImportedFromType = Literal["name", "path"]


class RFLibrary(BaseModel):
    """
    Dataclass representing a RF library.
    """

    imported_from: ImportedFromType
    name: str
    keywords_list: List[str]
    synopsis: str

    class Config:
        frozen = True


class IndexedRFLibrary(RFLibrary):
    """
    Dataclass representing a RF library that has been indexed.
    """

    html_libdoc_path: FilePath
    xml_libdoc_path: Optional[FilePath]
    json_libdoc_path: Optional[FilePath]

    class Config:
        frozen = True


class ExternalResource(BaseModel):
    """
    Dataclass representing an external resource.
    """

    url: AnyUrl
    name: Optional[str]

    class Config:
        frozen = True
