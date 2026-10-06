from pathlib import Path
import shutil

base = Path(r'C:/Users/User/Desktop/file_organizer_result')
desktop = Path.home()/'Desktop'
print(desktop)


categories = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".webp",
        ".bmp", ".svg", ".ico", ".tiff", ".tif", ".heic"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv",
        ".flv", ".webm", ".m4v", ".3gp"
    ],

    "Music": [
        ".mp3", ".wav", ".flac", ".aac", ".ogg",
        ".m4a", ".wma", ".opus"
    ],

    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".rtf",
        ".odt", ".pages"
    ],

    "Spreadsheets": [
        ".xls", ".xlsx", ".csv", ".ods"
    ],

    "Presentations": [
        ".ppt", ".pptx", ".odp", ".key"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz",
        ".bz2", ".xz", ".tar.gz", ".tar.bz2"
    ],

    "Programs": [
        ".exe", ".msi", ".bat", ".cmd", ".com"
    ],

    "Code": [
        ".py", ".js", ".ts", ".jsx", ".tsx",
        ".html", ".htm", ".css", ".scss",
        ".c", ".h", ".cpp", ".hpp",
        ".java", ".kt", ".go", ".rs",
        ".php", ".rb", ".swift",
        ".sql", ".sh", ".ps1"
    ],

    "Fonts": [
        ".ttf", ".otf", ".woff", ".woff2"
    ],

    "Subtitles": [
        ".srt", ".ass", ".ssa", ".vtt"
    ],

    "Databases": [
        ".db", ".sqlite", ".sqlite3", ".mdb", ".accdb"
    ],

    "DiskImages": [
        ".iso", ".img", ".dmg", ".vhd", ".vhdx"
    ],

    "Text": [
        ".log", ".md", ".markdown"
    ]
}


for category in categories.keys():
    folder = base / category
    folder.mkdir(exist_ok=True)
for item in desktop.iterdir():
    if item.is_file():
        extension = item.suffix
        for category , extensions  in categories.items():
            destination_file = base / category / item.name
            if extension in extensions:
                if destination_file.exists():
                    print("file is exists")    
                else:                                     
                    shutil.move(item,base / category)     
    