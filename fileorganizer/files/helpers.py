import os
from json import loads
from pathlib import Path
from subprocess import check_output
from typing import (
    Dict,
    Generator,
    Optional,
    Sequence,
    Tuple,
)

from fileorganizer.shared.logging import Logger

from .definitions import (
    AudioFile,
    DocumentFile,
    FileType,
    ImageFile,
    ScriptFile,
    VideoFile,
)


def extract_streams_by_codec(file_path: str, codec_type: str) -> Tuple[bool, int]:
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
        num = len(audio_streams)
        return num > 0, num

    return False, 0


def get_file_extension(file: str) -> Optional[str]:
    """Returns the extension of a given file."""
    return Path(file).suffix.lower()


def get_file_type(file_name: str, base_path: str) -> str:
    """Extracts the FileType from the extension, given the file name."""
    extension = get_file_extension(file_name)

    file_formats_types_map: Dict[str, Sequence[str]] = {
        FileType.AUDIO: AudioFile.values(),
        FileType.DOCUMENT: DocumentFile.values(),
        FileType.IMAGE: ImageFile.values(),
        FileType.VIDEO: VideoFile.values(),
        FileType.SCRIPT: ScriptFile.values(),
    }

    def is_ext_known(ext: str | None, ext_list: Sequence[str]) -> bool:
        return ext != None and ext in ext_list

    # Check if each file extension is supported by the organizer
    for file_type, extensions in file_formats_types_map.items():
        if is_ext_known(extension, extensions):
            file_path = os.path.join(base_path, file_name)

            # Disambiguate audio and video files with the same extension...
            if file_type == FileType.AUDIO:
                Logger.log(f"Checking if '{file_name}' has an audio stream...")

                has_streams, num_streams = extract_streams_by_codec(
                    file_path, FileType.VIDEO
                )

                if has_streams:
                    Logger.warning(
                        f"Audio file '{file_name}' has {num_streams} video streams! Categorized as {FileType.VIDEO}."
                    )

                    return FileType.VIDEO

            # Otherwise, returns the extracted file type
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
