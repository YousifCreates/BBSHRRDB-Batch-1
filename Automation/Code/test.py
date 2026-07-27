FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar"],
    "Code": [".py", ".cpp", ".c", ".java", ".html", ".css", ".js"],
    "Data": [".csv", ".xlsx", ".json"],
}


def get_category(extension):
    """
    Returns category name according to file extension.
    """

    extension = extension.lower()

    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category

    return "Others"


print(get_category(".PDF"))
print(get_category(".PNG"))
print(get_category(".mp4"))