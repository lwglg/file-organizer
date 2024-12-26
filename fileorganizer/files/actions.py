# Base imports
import os
from typing import Dict, List, Optional

# Project imports
from fileorganizer.shared.logging import Logger
from fileorganizer.shared.helpers import is_empty_no_side_effects
from .helpers import list_files, get_file_type
from .definitions import FileType


__all__ = [
    "map_file_types_to_paths",
    "associate_file_to_new_folder",
    "create_folder_structure",
    "organize_files",
]


def map_file_types_to_paths(base_path: str) -> Dict[str, str]:
    """Maps the file types to the destination folder path."""
    return {
        FileType.AUDIO: os.path.join(base_path, "audios"),
        FileType.DOCUMENT: os.path.join(base_path, "documents"),
        FileType.IMAGE: os.path.join(base_path, "images"),
        FileType.VIDEO: os.path.join(base_path, "videos"),
        FileType.SCRIPT: os.path.join(base_path, "scripts"),
        FileType.UNKNOWN: os.path.join(base_path, "others"),
    }


def associate_file_to_new_folder(
    base_path: str,
    file_name: str,
    folder_paths: Dict[str, str],
) -> None:
    """Builds the new file path and them moves the file to it's new destination."""
    file_type = get_file_type(file_name, base_path)

    # Builds the new file path with the extracted type
    new_path = os.path.join(folder_paths[file_type], file_name)

    # Move the file to its corresponding folder
    Logger.log(f'Moving "{file_name}" to "{new_path}"...')
    os.rename(os.path.join(base_path, file_name), new_path)


def create_folder_structure(folder_paths: List[str]) -> None:
    """Check if subdirectories exist and create them if they don't."""
    for folder_path in folder_paths:
        if not os.path.isdir(folder_path):
            os.mkdir(folder_path)


def organize_files(base_path: str, file_type: Optional[str] = None) -> None:
    """Organizes files in a given directory into corresponding
    subdirectories based on file extension."""
    folder_paths = map_file_types_to_paths(base_path)

    create_folder_structure(folder_paths.values())

    file_generator, is_empty = is_empty_no_side_effects(
        list_files(base_path, file_type)
    )

    if is_empty:
        Logger.warning("No files to be organized. No action taken")
        return

    for file_name in file_generator:
        associate_file_to_new_folder(base_path, file_name, folder_paths)
