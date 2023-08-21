# Project imports
from fileorganizer.shared.enums import BaseEnum


class UnknownFile(str, BaseEnum):
    UNKNOWN = 'unknown'


class AudioFile(str, BaseEnum):
    MP3 = '.mp3'
    WAVE = '.wav'


class VideoFile(str, BaseEnum):
    MP4 = '.mp4'
    MKV = '.mkv'
    AVI = '.avi'


class ScriptFile(str, BaseEnum):
    BATCH = '.bat'
    SHELL = '.sh'
    PYTHON = '.py'
    JAVASCRIPT = '.js'
    TYPESCRIPT = '.ts'
    SQL = '.sql'


class DocumentFile(str, BaseEnum):
    PDF = '.pdf'
    DOC = '.doc'
    DOCX = '.docx'
    ODT = '.odt'
    MARKDOWN = '.md'
    PPT = '.ppt'
    PPTX = '.pptx'
    TXT = '.txt'
    XLS = '.xls'
    XLSX = '.xlsx'
    

class ImageFile(str, BaseEnum):
    JPG = '.jpg'
    JPEG = '.jpeg'
    PNG = '.png'
    SVG = '.svg'
    BITMAP = '.bmp'
    WEBP = '.webp'


class FileType(str, BaseEnum):
    AUDIO = 'audio'
    DOCUMENT = 'document'
    IMAGE = 'image'
    SCRIPT = 'script'
    VIDEO = 'video'
    UNKNOWN = 'unknown'
