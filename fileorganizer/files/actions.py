import os
from typing import Dict, List, Optional

from fileorganizer.shared.helpers import is_empty_no_side_effects
from fileorganizer.shared.logging import Logger

from .definitions import FileType
from .helpers import get_file_type, list_files

__all__ = [
    "map_file_types_to_paths",
    "associate_file_to_new_folder",
    "create_folder_structure",
    "organize_files",
]


def map_file_types_to_paths(
    base_path: str, file_type: str | None = None
) -> Dict[str, str]:
    """Maps the file types to the destination folder path."""
    file_type_folder_map = {
        FileType.AUDIO: os.path.join(base_path, "audios"),
        FileType.DOCUMENT: os.path.join(base_path, "documents"),
        FileType.IMAGE: os.path.join(base_path, "images"),
        FileType.VIDEO: os.path.join(base_path, "videos"),
        FileType.SCRIPT: os.path.join(base_path, "scripts"),
        FileType.UNKNOWN: os.path.join(base_path, "others"),
    }

    if file_type == None:
        return file_type_folder_map

    sanitized_type = file_type.lower().strip()

    return {
        ftype: folder_name
        for ftype, folder_name in file_type_folder_map
        if ftype == sanitized_type
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


def create_folder_structure(
    folder_paths: List[str], file_type: str | None = None
) -> None:
    """Check if subdirectories exist and create them if they don't."""

    def mkdir_if_not_exist(path: str) -> None:
        if not os.path.isdir(path):
            os.mkdir(path)

    # If the file type is informed, filter only the path related to the type
    if file_type != None and file_type != "":
        sanitized_type = file_type.lower().strip()
        filtered = [item for item in folder_paths if sanitized_type in item]

        if len(filtered) == 1:
            mkdir_if_not_exist(filtered[0])
    else:
        for folder_path in folder_paths:
            mkdir_if_not_exist(folder_path)


def organize_files(base_path: str, file_type: Optional[str] = None) -> None:
    """Organizes files in a given directory into corresponding
    subdirectories based on file extension."""
    file_generator, is_empty = is_empty_no_side_effects(
        list_files(base_path, file_type)
    )

    if is_empty:
        Logger.warning("No files to be organized. No action taken.")
        return

    folder_paths = map_file_types_to_paths(base_path, file_type)
    create_folder_structure(list(folder_paths.values()), file_type)

    for file_name in file_generator:
        associate_file_to_new_folder(base_path, file_name, folder_paths)
