# Base imports
import os
from typing import  Generator, Optional
from pathlib import Path

# Project imports
from .definitions import (
    FileType,
    AudioFile,
    DocumentFile,
    ImageFile,
    VideoFile,
    ScriptFile,
)


def get_file_extension(file: str) -> Optional[str]:
    """Returns the extension of a given file."""
    return Path(file).suffix.lower()


def get_file_type(file_name: str) -> str:
    """Extracts the FileType from the extension, given the file name."""
    extension = get_file_extension(file_name)

    if extension in AudioFile.values():
        return FileType.AUDIO
    
    if extension in DocumentFile.values():
        return FileType.DOCUMENT
    
    if extension in ImageFile.values():
        return FileType.IMAGE
    
    if extension in VideoFile.values():
        return FileType.VIDEO
    
    if extension in ScriptFile.values():
        return FileType.SCRIPT
    
    return FileType.UNKNOWN


def list_files(base_path: str, file_type: Optional[str] = None) -> Generator[Optional[str], None, None]:
    """Builds a string generator, containing just file names inside a given folder, and a file type."""
    for file_name in os.listdir(base_path):
        if os.path.isfile(os.path.join(base_path, file_name)):
            type_from_file = get_file_type(file_name)

            # Handle both cases in which the informed type does not
            # coincide with the extracted one and when the informed
            # type does not coincide with the supported ones
            file_type_invalid = file_type != None \
                and (file_type != type_from_file or file_type not in FileType.values())

            if not file_type_invalid:
                yield file_name
