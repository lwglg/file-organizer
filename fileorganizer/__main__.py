# Base imports
import sys
import argparse

# Project import
from fileorganizer.shared.logging import Logger, Text
from fileorganizer.shared.arguments import ArgumentParser
from fileorganizer.files import organize_files, FileType


def extract_arguments():
    # Create ArgumentParser
    parser = ArgumentParser(
        description=Text.bold("Program that organizes files into separate folders, grouped by type, given a valid root folder and a file type."),
        epilog="Copyright (c) 2023 João Victor Vilela dos Santos",
        argument_default=argparse.SUPPRESS,
        allow_abbrev=False,
        add_help=False
    )


    # Add positionals
    parser.add_argument(
        "base_path",
        action="store",
        metavar="base_path",
        type=str,
        help=Text.italic("The absolute path for target folder containing the files to be organized")
    )

    # Add options
    parser.add_argument(
        "-t",
        "--file-type",
        action="store",
        metavar=FileType.values(),
        type=str,
        choices=FileType.values(),
        help=Text.italic("The file type to be organized. Files of other type will be ignored")
    )
    parser.add_argument(
        "-h",
        "--help",
        action="help",
        help=Text.italic("Display this message")
    )


    return parser.parse_args()


def main() -> None:
    parsed = extract_arguments()
    
    args = {
        'base_path': parsed.base_path,
    }

    message = f'Organizing files for target "{parsed.base_path}"'

    if hasattr(parsed, 'file_type'):
        message += f' and type "{parsed.file_type}"'
        args.update({'file_type': parsed.file_type})
    
    Logger.log(Text.bold(f'{message}:\n'))

    organize_files(**args)

    Logger.success(Text.bold('\nDone!'))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        Logger.danger(f'{exc.__class__.__name__}: {str(exc)}')
        sys.exit(2)
    except KeyboardInterrupt:
        Logger.danger("SIGINT triggered. Exitting application...")
        sys.exit(0)
