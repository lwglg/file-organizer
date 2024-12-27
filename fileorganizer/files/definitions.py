from fileorganizer.shared.enums import BaseEnum

__all__ = [
    "UnknownFile",
    "AudioFile",
    "VideoFile",
    "ScriptFile",
    "DocumentFile",
    "ImageFile",
    "FileType",
    "FileTrasmissionType",
]


class UnknownFile(str, BaseEnum):
    UNKNOWN = "unknown"


class AudioFile(str, BaseEnum):
    AAC = ".aac"
    AIFF = ".aiff"
    ALAC = ".alac"
    MP3 = ".mp3"
    MP4 = ".mp4"
    M4A = ".m4a"
    FLAC = ".flac"
    WAVE = ".wav"
    WMA = ".wma"


class VideoFile(str, BaseEnum):
    AVCHD = ".avchd"
    AVI = ".avi"
    FLV = ".flv"
    MP4 = ".mp4"
    MKV = ".mkv"
    MOV = ".mov"
    WEBM = ".webm"
    WMV = ".wmv"


class ScriptFile(str, BaseEnum):
    BATCH = ".bat"
    C = ".c"
    CPP = ".cpp"
    COBOL = ".cbl"
    FORTRAN = ".f"
    JAVASCRIPT = ".js"
    PYTHON = ".py"
    SHELL = ".sh"
    SQL = ".sql"
    TYPESCRIPT = ".ts"


class DocumentFile(str, BaseEnum):
    PDF = ".pdf"
    DOC = ".doc"
    DOCX = ".docx"
    ODT = ".odt"
    MARKDOWN = ".md"
    PPT = ".ppt"
    PPTX = ".pptx"
    TXT = ".txt"
    XLS = ".xls"
    XLSX = ".xlsx"


class ImageFile(str, BaseEnum):
    JPG = ".jpg"
    JPEG = ".jpeg"
    PNG = ".png"
    SVG = ".svg"
    BITMAP = ".bmp"
    WEBP = ".webp"


class FileTrasmissionType(str, BaseEnum):
    TORRENT = ".torrent"


class FileType(str, BaseEnum):
    AUDIO = "audio"
    DOCUMENT = "document"
    IMAGE = "image"
    SCRIPT = "script"
    VIDEO = "video"
    UNKNOWN = "unknown"
    TRANSMISSION = "transmission"
