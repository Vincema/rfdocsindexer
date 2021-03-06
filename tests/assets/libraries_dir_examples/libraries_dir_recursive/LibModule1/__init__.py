import io

from robot.api.deco import keyword, library

ROBOT_LIBRARY_VERSION = "1.2.3"


@library
class LibModule1:
    """LibModule1 library"""

    def __init__(self):
        pass

    @keyword(name="Keyword1")
    def Keyword1(self):
        pass

    @keyword(name="Keyword2")
    def Keyword2(self, arg1: str):
        pass

    @keyword(name="Keyword Which Embeds ${arg1} And ${arg2}")
    def Keyword_With_Embedded_Args(self, arg1, arg2):
        pass
