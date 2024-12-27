# Project imports
from fileorganizer.shared.arguments import ArgumentParser
from .definitions import ARGPARSER_SPECS


__all__ = ["extract_arguments"]


def extract_arguments():
    # Create ArgumentParser
    parser = ArgumentParser(ARGPARSER_SPECS.get("parser"))
    arguments_specs = ARGPARSER_SPECS.get("arguments")

    for specs in arguments_specs:
        name_or_flags = specs.get("name_or_flags")

        # Remove position args, leaving only keyword args
        del specs["name_or_flags"]

        parser.add_argument(*name_or_flags, **specs)

    return parser.parse_args()
