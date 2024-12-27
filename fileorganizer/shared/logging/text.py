__all__ = ["Text"]


# Adapted from https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal/39452138#39452138
class Text:
    """Static class that defines the ANSI codes for text formatting."""

    # Formatting codes
    CEND = "\33[0m"
    CBOLD = "\33[1m"
    CITALIC = "\33[3m"
    CURL = "\33[4m"
    CBLINK = "\33[5m"
    CBLINK2 = "\33[6m"
    CSELECTED = "\33[7m"

    # Foreground color codes
    CBLACK = "\33[30m"
    CRED = "\33[31m"
    CGREEN = "\33[32m"
    CYELLOW = "\33[33m"
    CBLUE = "\33[34m"
    CVIOLET = "\33[35m"
    CBEIGE = "\33[36m"
    CWHITE = "\33[37m"

    # Background color codes
    CBLACKBG = "\33[40m"
    CREDBG = "\33[41m"
    CGREENBG = "\33[42m"
    CYELLOWBG = "\33[43m"
    CBLUEBG = "\33[44m"
    CVIOLETBG = "\33[45m"
    CBEIGEBG = "\33[46m"
    CWHITEBG = "\33[47m"

    CGREY = "\33[90m"
    CRED2 = "\33[91m"
    CGREEN2 = "\33[92m"
    CYELLOW2 = "\33[93m"
    CBLUE2 = "\33[94m"
    CVIOLET2 = "\33[95m"
    CBEIGE2 = "\33[96m"
    CWHITE2 = "\33[97m"

    CGREYBG = "\33[100m"
    CREDBG2 = "\33[101m"
    CGREENBG2 = "\33[102m"
    CYELLOWBG2 = "\33[103m"
    CBLUEBG2 = "\33[104m"
    CVIOLETBG2 = "\33[105m"
    CBEIGEBG2 = "\33[106m"
    CWHITEBG2 = "\33[107m"

    @classmethod
    def format_text(cls, text: str, text_format: str) -> str:
        return text_format + text + cls.CEND

    @classmethod
    def bold(cls, text: str) -> str:
        return cls.format_text(text, cls.CBOLD)

    @classmethod
    def italic(cls, text: str) -> str:
        return cls.format_text(text, cls.CITALIC)

    @classmethod
    def url(cls, text: str) -> str:
        return cls.format_text(text, cls.CURL)

    @classmethod
    def blink(cls, text: str) -> str:
        return cls.format_text(text, cls.CBLINK)

    @classmethod
    def blink2(cls, text: str) -> str:
        return cls.format_text(text, cls.CBLINK2)
