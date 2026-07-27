import streamlit as st
from pathlib import Path
import shutil

st.set_page_config(
    page_title="Download Folder Automation",
    page_icon="📂",
    layout="centered"
)

# ======================================================
# File Categories
# ======================================================

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar"],
    "Code": [".py", ".cpp", ".c", ".java", ".html", ".css", ".js"],
    "Data": [".csv", ".xlsx", ".json"],
}

# ======================================================
# Backup Function
# ======================================================

def create_backup(folder_path):
    backup_folder = folder_path.parent / f"{folder_path.name}_Backup"

    try:
        if backup_folder.exists():
            shutil.rmtree(backup_folder)

        shutil.copytree(folder_path, backup_folder)

        archive_path = shutil.make_archive(
            str(backup_folder),
            "zip",
            backup_folder
        )

        return True, archive_path

    except Exception as e:
        return False, str(e)

# ======================================================
# Category Function
# ======================================================

def get_category(extension):
    extension = extension.lower()

    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category

    return "Others"

# ======================================================
# Organize Files
# ======================================================

def organize_files(folder_path):

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

            if item.is_dir():
                continue

            category = get_category(item.suffix)

            destination = folder_path / category
            destination.mkdir(exist_ok=True)

            shutil.move(
                str(item),
                str(destination / item.name)
            )

            summary[category] += 1

        return summary

    except Exception as e:
        st.error(f"Error: {e}")
        return summary

# ======================================================
# Summary
# ======================================================

def show_summary(summary, backup_success):

    total = sum(summary.values())

    st.success("Automation Completed Successfully!")

    st.subheader("📊 Automation Summary")

    st.table({
        "Category": [
            "Images",
            "Documents",
            "Videos",
            "Audio",
            "Archives",
            "Code",
            "Data",
            "Others",
            "Total"
        ],
        "Files": [
            summary["Images"],
            summary["Documents"],
            summary["Videos"],
            summary["Audio"],
            summary["Archives"],
            summary["Code"],
            summary["Data"],
            summary["Others"],
            total
        ]
    })

    if backup_success:
        st.success("✅ Backup created successfully.")
    else:
        st.error("❌ Backup could not be created.")

# ======================================================
# Main
# ======================================================

def main():

    st.title("📂 Download Folder Automation System")

    st.write(
        """
Organize files automatically into categories.

**Categories**
- Images
- Documents
- Videos
- Audio
- Archives
- Code
- Data
- Others
"""
    )

    folder = st.text_input(
        "Enter Folder Path",
        placeholder=r"C:\Users\Student\Downloads"
    )

    if st.button("🚀 Organize Files"):

        if not folder:
            st.warning("Please enter a folder path.")
            return

        folder_path = Path(folder)

        if not folder_path.exists():
            st.error("Folder does not exist.")
            return

        with st.spinner("Creating Backup..."):
            backup_status, backup = create_backup(folder_path)

        with st.spinner("Organizing Files..."):
            summary = organize_files(folder_path)

        show_summary(summary, backup_status)

        if backup_status:
            with open(backup, "rb") as file:
                st.download_button(
                    label="⬇ Download Backup ZIP",
                    data=file,
                    file_name=Path(backup).name,
                    mime="application/zip"
                )


if __name__ == "__main__":
    main()