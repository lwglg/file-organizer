# Base imports
import sys
import argparse

# Project import
from fileorganizer.arguments import extract_arguments
from fileorganizer.files import organize_files
from fileorganizer.shared.logging import Logger, Text


def main() -> None:
    parsed = extract_arguments()

    args = {
        "base_path": parsed.base_path,
    }

    message = f'Organizing files for target "{parsed.base_path}"'

    if hasattr(parsed, "file_type"):
        message += f' and type "{parsed.file_type}"'
        args.update({"file_type": parsed.file_type})

    Logger.log(Text.bold(f"{message}:\n"))

    organize_files(**args)

    Logger.success(Text.bold("\nDone!"))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        Logger.danger(f"{exc.__class__.__name__}: {str(exc)}")
        sys.exit(-1)
    except KeyboardInterrupt:
        Logger.danger("SIGINT triggered. Exitting application...")
        sys.exit(0)
    finally:
        sys.exit(0)
