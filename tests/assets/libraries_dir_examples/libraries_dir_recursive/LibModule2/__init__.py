from robot.api.deco import keyword, library

ROBOT_LIBRARY_VERSION = "1.2.3"


@library
class LibModule2CustomName:
    """LibModule2CustomName library"""

    def __init__(self):
        pass

    @keyword(name="Keyword1")
    def Keyword1(self):
        pass

    @keyword(name="Keyword2")
    def Keyword2(self, arg1: str):
        pass
