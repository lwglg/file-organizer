# Base imports
import argparse
from typing import Any, Dict, List, NotRequired, TypedDict

# Project imports
from fileorganizer.files import FileType
from fileorganizer.shared.arguments import APParserSpecs, APArgumentSpecs
from fileorganizer.shared.logging import Text


__all__ = [
    "ARGPARSER_SPECS",
]


class APSpecs(TypedDict):
    parser: APParserSpecs
    arguments: List[APArgumentSpecs]


ARGPARSER_SPECS: APSpecs = {
    "parser": {
        "description": Text.bold(
            "Program that organizes files into separate folders, grouped by type, given a valid root folder and a file type."
        ),
        "epilog": "Copyright (c) 2023 João Victor Vilela dos Santos",
        "argument_default": argparse.SUPPRESS,
        "allow_abbrev": False,
        "add_help": False,
    },
    "arguments": [
        {
            "name_or_flags": ["base_path"],
            "action": "store",
            "metavar": "base_path",
            "type": str,
            "help": Text.italic(
                "The absolute path for target folder containing the files to be organized"
            ),
        },
        {
            "name_or_flags": ["-t", "--file-type"],
            "action": "store",
            "metavar": FileType.values(),
            "type": str,
            "choices": FileType.values(),
            "help": Text.italic(
                "The file type to be organized. Files of other type will be ignored"
            ),
        },
    ],
}
