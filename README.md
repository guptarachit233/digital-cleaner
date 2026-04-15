# 📂 File Organizer Script (Python)

A simple Python script that automatically organizes files in a folder into categorized subfolders based on their file types.

---

## 🚀 Features

* Automatically sorts files into categories:

  * Images
  * Documents
  * Videos
  * Music
  * Archives
* Creates folders if they don’t exist
* Moves unknown file types to an **Others** folder
* Easy to customize and use

---

## 🛠️ Technologies Used

* Python 3
* Built-in libraries:

  * `os`
  * `shutil`

---

## 📁 Project Structure

```
project-folder/
│── org.py
│── README.md
```

---

## ⚙️ How It Works

1. The script scans all files in the specified folder.
2. It checks each file’s extension.
3. Based on the file type, it moves the file into the appropriate folder.
4. If no match is found, the file is moved to the **Others** folder.

---

## 📌 Setup Instructions

1. Download or clone this project.

2. Open the script file:

   ```
   org.py
   ```

3. Change the folder path:

   ```python
   SOURCE_FOLDER = "C:/Users/Public/Documents"
   ```

4. Run the script:

   ```bash
   python org.py
   ```

---

## 📊 Supported File Types

| Category  | Extensions                      |
| --------- | ------------------------------- |
| Images    | .jpg, .jpeg, .png, .gif         |
| Documents | .pdf, .docx, .txt, .pptx, .xlsx |
| Videos    | .mp4, .mkv, .avi                |
| Music     | .mp3, .wav                      |
| Archives  | .zip, .rar                      |

---
