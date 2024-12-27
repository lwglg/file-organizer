# Base imports
from typing import Optional

# Project imports
from .text import Text


__all__ = ["Logger"]


class Logger:
    @classmethod
    def log(cls, text: str, text_format: str = Text.CWHITE) -> None:
        print(Text.format_text(text, text_format))

    @classmethod
    def success(cls, text: str) -> None:
        Logger.log(text, Text.CGREEN)

    @classmethod
    def warning(cls, text: str) -> None:
        Logger.log(text, Text.CYELLOW)

    @classmethod
    def danger(cls, text: str) -> None:
        Logger.log(text, Text.CRED)
