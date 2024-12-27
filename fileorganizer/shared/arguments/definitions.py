# Base imports
import argparse
from typing import Dict, List, NotRequired, TypedDict

__all__ = [
    "APParserSpecs",
    "APArgumentSpecs",
]


type TArgumentValue = str | bool | int | float | None
type TFormatterClass = argparse.RawDescriptionHelpFormatter | argparse.RawTextHelpFormatter | argparse.ArgumentDefaultsHelpFormatter | argparse.MetavarTypeHelpFormatter


class APParserSpecs(TypedDict):
    prog: str  # The name of the program (default: os.path.basename(sys.argv[0]))
    usage: NotRequired[
        str
    ]  # The string describing the program usage (default: generated from arguments added to parser)
    description: NotRequired[
        str
    ]  # Text to display before the argument help (by default, no text)
    epilog: NotRequired[
        str
    ]  # Text to display after the argument help (by default, no text)
    parents: NotRequired[
        List[argparse.ArgumentParser]
    ]  # A list of ArgumentParser objects whose arguments should also be included
    formatter_class: NotRequired[
        TFormatterClass
    ]  # A class for customizing the help output
    prefix_chars: NotRequired[
        str
    ]  # The set of characters that prefix optional arguments (default: ‘-‘)
    fromfile_prefix_chars: NotRequired[
        str
    ]  # The set of characters that prefix files from which additional arguments should be read (default: None)
    argument_default: NotRequired[
        TArgumentValue
    ]  # The global default value for arguments (default: None)
    conflict_handler: NotRequired[
        str
    ]  # The strategy for resolving conflicting optionals (usually unnecessary)
    add_help: NotRequired[bool]  # Add a -h/--help option to the parser (default: True)
    allow_abbrev: NotRequired[
        bool
    ]  # Allows long options to be abbreviated if the abbreviation is unambiguous. (default: True)
    exit_on_error: NotRequired[
        bool
    ]  # Determines whether or not ArgumentParser exits with error info when an error occurs. (default: True)


class APArgumentSpecs(TypedDict):
    name_or_flags: List[
        str
    ]  # Either a name or a list of option strings, e.g. 'foo' or '-f', '--foo'.
    action: NotRequired[
        str
    ]  # The basic type of action to be taken when this argument is encountered at the command line.
    nargs: NotRequired[
        int
    ]  # The number of command-line arguments that should be consumed.
    const: NotRequired[
        TArgumentValue
    ]  # A constant value required by some action and nargs selections.
    default: NotRequired[
        TArgumentValue
    ]  # The value produced if the argument is absent from the command line and if it is absent from the namespace object.
    type: NotRequired[
        TArgumentValue
    ]  # The type to which the command-line argument should be converted.
    choices: NotRequired[
        List[TArgumentValue]
    ]  # A sequence of the allowable values for the argument.
    required: NotRequired[
        bool
    ]  # Whether or not the command-line option may be omitted (optionals only).
    help: NotRequired[str]  # A brief description of what the argument does.
    metavar: NotRequired[str]  # A name for the argument in usage messages.
    dest: NotRequired[
        str
    ]  # The name of the attribute to be added to the object returned by parse_args().
    deprecated: NotRequired[bool]  # Whether or not use of the argument is deprecated.
