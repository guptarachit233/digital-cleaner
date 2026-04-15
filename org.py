import os
import shutil

#  Change this to your folder path
SOURCE_FOLDER = "C:/Users/rachit gupta/OneDrive/Desktop"

#  File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

def organize_files():
    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(file)

        moved = False

        # Check category
        for folder, extensions in FILE_TYPES.items():
            if ext.lower() in extensions:
                folder_path = os.path.join(SOURCE_FOLDER, folder)

                # Create folder if not exists
                os.makedirs(folder_path, exist_ok=True)

                shutil.move(file_path, os.path.join(folder_path, file))
                moved = True
                break

        # If not matched → Others
        if not moved:
            other_folder = os.path.join(SOURCE_FOLDER, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, file))

    print("✅ Files organized successfully!")

if __name__ == "__main__":
    organize_files()