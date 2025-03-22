# Snapchat Data Metadata Fixer

This Python script updates the metadata (creation dates) of media files (images and videos) downloaded from Snapchat's "Download My Data" feature. Snapchat provides media files from the "Chat Media" and "Memories" folders with incorrect metadata, where the file creation date reflects the download date rather than the actual capture date. Fortunately, the filenames contain the correct date in the format `YYYY-MM-DD`. This script extracts the date from the filename and applies it to the file's system timestamps and, for JPEG images, the EXIF metadata.

## Prerequisites

Before running the script, ensure you have the following installed and set up:

### 1. Python
The script requires Python 3.x to run.

- **Check if Python is installed:**
  Open a terminal or command prompt and run:
  ```
  python3 -V
  ```
  Alternatively, try:
  ```
  python -V
  ```
  If a version number (e.g., `Python 3.11.0`) is returned, Python is installed. If not, download and install it from:
  - [Python Official Website](https://www.python.org/downloads/)

- **Note:** Ensure Python is added to your system's PATH during installation so you can run it from the terminal.

### 2. Pip
Pip is the package manager for Python, used to install required libraries.

- **Check if Pip is installed:**
  Run:
  ```
  pip --version
  ```
  Or:
  ```
  pip3 --version
  ```
  If a version number is returned (e.g., `pip 23.0.1`), Pip is installed. If not, install it:
  - [Pip Installation Guide](https://pip.pypa.io/en/stable/installation/)
  - On most systems, Pip comes bundled with Python. If it’s missing, run:
    ```
    python -m ensurepip --upgrade
    python -m pip install --upgrade pip
    ```

### 3. Required Python Libraries
The script depends on the following libraries:
- `os` (built-in, no installation needed)
- `time` (built-in, no installation needed)
- `datetime` (built-in, no installation needed)
- `piexif` (for updating EXIF metadata in JPEG files)
- `Pillow` (PIL, for handling image files)

Install these libraries using Pip:
```
pip install piexif
pip install Pillow
```

## Setup and Usage

### 1. Download Your Snapchat Data
- Log in to Snapchat and request your data via the "Download My Data" feature.
- Once received, unzip the downloaded file. The media files are located in:
  - `chat_media/` (for chat-related images/videos)
  - `memories/` (for saved memories)
- Decide which folder you want to process (`chat_media`, `memories`, or both).

### 2. Prepare the Script
- Save the script (e.g., as `fix_snapchat_metadata.py`) in a convenient location.
- Open the script in a text editor and locate this line:
  ```python
  FOLDER_PATH = "YOUR FOLDER PATH HERE"
  ```
- Replace `"YOUR FOLDER PATH HERE"` with the full path to the folder containing your Snapchat media files. Examples:
  - Windows: `"C:/Users/YourName/Downloads/snapchat_data/memories"`
  - Mac/Linux: `"/home/yourname/Downloads/snapchat_data/chat_media"`
- **Note:** Use forward slashes (`/`) or double backslashes (`\\`) on Windows to avoid path errors.

- **Optional:** If you want to process both `chat_media` and `memories` together, copy the contents of both folders into a single directory and set `FOLDER_PATH` to that directory. The script processes one folder at a time.

### 3. Run the Script
- Open a terminal or command prompt.
- Navigate to the directory containing the script:
  ```
  cd /path/to/script
  ```
- Run the script:
  ```
  python3 fix_snapchat_metadata.py
  ```
  Or:
  ```
  python fix_snapchat_metadata.py
  ```
- The script will:
  - List all files in the specified folder.
  - Extract dates from filenames (assuming the format `YYYY-MM-DD` at the start).
  - Update system timestamps for all files.
  - Update EXIF metadata for JPEG files (`.jpg`, `.jpeg`).
  - Print progress and a summary of processed files.

## How It Works
- **Filename Parsing:** The script assumes filenames start with a date in `YYYY-MM-DD` format (e.g., `2023-05-14_image.jpg`). It extracts this date and converts it to a timestamp.
- **Timestamp Update:** Updates the file's "last modified" and "access" times to match the extracted date.
- **EXIF Update:** For JPEG files, updates the `DateTimeOriginal` EXIF tag with the extracted date.
- **Supported Files:** Works on all file types for system timestamps, but only updates EXIF for `.jpg` and `.jpeg` files.

## Limitations
- The script assumes filenames begin with a valid `YYYY-MM-DD` date. Files without this format are skipped.
- EXIF updates apply only to JPEG files (not videos or other formats like PNG).
- You must process one folder at a time unless you combine files into a single directory.

## Troubleshooting
- **"Module not found" errors:** Ensure `piexif` and `Pillow` are installed (see step 3 under Prerequisites).
- **Permission denied:** Run the terminal as an administrator (Windows) or use `sudo` (Linux/Mac) if needed.
- **No files processed:** Double-check the `FOLDER_PATH` and ensure it points to the correct directory.

## Contributing
Feel free to fork this project, improve the code, or suggest enhancements (e.g., support for video metadata or custom filename formats). Submit pull requests or open issues as needed.

---

This README should be clear and comprehensive for users unfamiliar with your script. Let me know if you'd like me to tweak anything!
