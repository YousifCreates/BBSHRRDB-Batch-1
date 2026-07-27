"""
Download Folder Automation System
---------------------------------
This program:
1. Creates a backup of the target folder.
2. Compresses the backup into a ZIP archive.
3. Organizes files into categories based on file extensions.
4. Displays an automation summary.
"""

from pathlib import Path
import shutil

# ==========================================================
# File Categories
# ==========================================================

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar"],
    "Code": [".py", ".cpp", ".c", ".java", ".html", ".css", ".js"],
    "Data": [".csv", ".xlsx", ".json"],
}

# ==========================================================
# Create Backup
# ==========================================================

def create_backup(folder_path):
    """
    Creates a complete backup of the folder
    and compresses it into a ZIP archive.
    """

    backup_folder = folder_path.parent / f"{folder_path.name}_Backup"

    try:
        # Remove old backup if it exists
        if backup_folder.exists():
            shutil.rmtree(backup_folder)

        # Copy entire folder
        shutil.copytree(folder_path, backup_folder)

        # Create ZIP archive
        shutil.make_archive(str(backup_folder), "zip", backup_folder)

        return True

    except Exception as e:
        print("Backup Error:", e)
        return False


# ==========================================================
# Get Category
# ==========================================================

def get_category(extension):
    """
    Returns category name according to file extension.
    """

    extension = extension.lower()

    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category

    return "Others"


# ==========================================================
# Organize Files
# ==========================================================

def organize_files(folder_path):
    """
    Organizes all files into categorized folders.
    """

    summary = {
        "Images": 0,
        "Documents": 0,
        "Videos": 0,
        "Audio": 0,
        "Archives": 0,
        "Code": 0,
        "Data": 0,
        "Others": 0
    }

    try:

        for item in folder_path.iterdir():

            # Skip folders
            if item.is_dir():
                continue

            category = get_category(item.suffix)

            destination = folder_path / category
            destination.mkdir(exist_ok=True)

            shutil.move(str(item), str(destination / item.name))

            summary[category] += 1

    except Exception as e:
        print("Organization Error:", e)

    return summary


# ==========================================================
# Display Summary
# ==========================================================

def display_summary(summary, backup_status):

    total = sum(summary.values())

    print("\n=========== AUTOMATION SUMMARY ==========")
    print(f"Images moved: {summary['Images']}")
    print(f"Documents moved: {summary['Documents']}")
    print(f"Videos moved: {summary['Videos']}")
    print(f"Audio files moved: {summary['Audio']}")
    print(f"Archives moved: {summary['Archives']}")
    print(f"Code files moved: {summary['Code']}")
    print(f"Data files moved: {summary['Data']}")
    print(f"Other files moved: {summary['Others']}")
    print("-----------------------------------------")
    print(f"Total files organized: {total}")

    if backup_status:
        print("Backup created successfully.")
    else:
        print("Backup creation failed.")

    print("File organization completed successfully.")


# ==========================================================
# Main Function
# ==========================================================

def main():

    folder = input("Enter Download Folder Path: ").strip()

    download_folder = Path(folder)

    if not download_folder.exists():
        print("Folder does not exist.")
        return

    print("\nCreating backup...")
    backup_status = create_backup(download_folder)
    print(f"Backup Status: {backup_status}")
    print("Organizing files...")
    summary = organize_files(download_folder)

    display_summary(summary, backup_status)


# ==========================================================
# Program Entry
# ==========================================================

if __name__ == "__main__":
    main()