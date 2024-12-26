# Base imports
import os
from typing import Generator, List, Optional
from subprocess import check_output
from pathlib import Path
from json import loads

# Project imports
from .definitions import (
    FileType,
    AudioFile,
    DocumentFile,
    ImageFile,
    VideoFile,
    ScriptFile,
)


def has_streams(file_path: str, codec_type: str) -> bool:
    """Check each stream to see if at least one has an "audio" type codec.
    Please note that an audio stream may be present but silent,
    in which case this will still return True."""
    command = [
        "ffprobe",
        "-hide_banner",
        "-loglevel",
        "error",
        "-show_streams",
        "-ignore_chapters",
        "1",
        "-print_format",
        "json",
        file_path,
    ]

    output = check_output(command)
    parsed = loads(output)
    streams = parsed.get("streams")

    if streams != None:
        audio_streams = list(
            filter((lambda x: x.get("codec_type") == codec_type), streams)
        )

        return len(audio_streams) > 0

    return False


def get_file_extension(file: str) -> Optional[str]:
    """Returns the extension of a given file."""
    return Path(file).suffix.lower()


def get_file_type(file_name: str, base_path: str) -> str:
    """Extracts the FileType from the extension, given the file name."""
    extension = get_file_extension(file_name)

    def inclusion_test(ext: str, ext_list: List[str]) -> bool:
        return ext in ext_list

    file_formats_types_map = [
        [AudioFile.values(), FileType.AUDIO],
        [DocumentFile.values(), FileType.DOCUMENT],
        [ImageFile.values(), FileType.IMAGE],
        [VideoFile.values(), FileType.VIDEO],
        [ScriptFile.values(), FileType.SCRIPT],
    ]

    for extensions, file_type in file_formats_types_map:
        if inclusion_test(extension, extensions):
            file_path = os.path.join(base_path, file_name)

            # In order to disambiguate audio and video files with the same extension
            if file_type == FileType.AUDIO and has_streams(file_path, FileType.VIDEO):
                return FileType.VIDEO

            return file_type

    return FileType.UNKNOWN


def list_files(
    base_path: str, file_type: Optional[str] = None
) -> Generator[Optional[str], None, None]:
    """Builds a string generator, containing just file names inside a given folder, and a file type."""
    for file_name in os.listdir(base_path):
        if os.path.isfile(os.path.join(base_path, file_name)):
            type_from_file = get_file_type(file_name, base_path)

            # Handle both cases in which the informed type does not
            # coincide with the extracted one and when the informed
            # type does not coincide with the supported ones
            file_type_invalid = file_type != None and (
                file_type != type_from_file or file_type not in FileType.values()
            )

            if not file_type_invalid:
                yield file_name
