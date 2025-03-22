import os
import time
import datetime
import piexif
from PIL import Image

# Hardcoded folder path
FOLDER_PATH = "YOUR FILE PATH HERE"

# List all files in the folder and print them
files = [f for f in os.listdir(FOLDER_PATH) if os.path.isfile(os.path.join(FOLDER_PATH, f))]

print("Files found in directory:")
for f in files:
    print(f)

# Function to extract date from filename
def extract_date_from_filename(filename):
    try:
        date_part = filename[:10]  # First 10 characters (YYYY-MM-DD)
        date_obj = datetime.datetime.strptime(date_part, "%Y-%m-%d")
        timestamp = time.mktime(date_obj.timetuple())  # Convert to timestamp
        return date_obj, timestamp
    except ValueError:
        return None, None  # Skip files without valid dates

# Function to update file timestamps
def update_file_timestamps(file_path, timestamp):
    try:
        os.utime(file_path, (timestamp, timestamp))  # Update system timestamps
    except Exception as e:
        print(f"Error updating timestamps for {file_path}: {e}")

# Function to update EXIF metadata (for JPEG images)
def update_exif_metadata(file_path, date_obj):
    try:
        # Only process JPEG images
        if file_path.lower().endswith(('.jpg', '.jpeg')):
            exif_dict = {"Exif": {piexif.ExifIFD.DateTimeOriginal: date_obj.strftime("%Y:%m:%d %H:%M:%S")}}
            exif_bytes = piexif.dump(exif_dict)

            # Open image, update EXIF, and save it back
            image = Image.open(file_path)
            image.save(file_path, exif=exif_bytes)
            print(f"Updated EXIF metadata for: {file_path}")
    except Exception as e:
        print(f"Error updating EXIF for {file_path}: {e}")

# Process all files in the folder
def process_files():
    files = [f for f in os.listdir(FOLDER_PATH) if os.path.isfile(os.path.join(FOLDER_PATH, f))]
    processed_count = 0

    for filename in files:
        file_path = os.path.join(FOLDER_PATH, filename)
        date_obj, timestamp = extract_date_from_filename(filename)
        
        if timestamp:
            update_file_timestamps(file_path, timestamp)
            update_exif_metadata(file_path, date_obj)
            processed_count += 1
            print(f"Updated: {filename}")

    print(f"Metadata update completed for {processed_count} files.")

# Run the process
process_files()