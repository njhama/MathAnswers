import os

# Directory where the images are located
directory_path = "answers/chapter1/Self-Test"

# List of new names
new_names = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19"
]

# Get the list of image files in the directory
image_files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

# Sort the image files alphabetically
image_files.sort()

# Rename the image files with the new names
for i, image_file in enumerate(image_files):
    if i < len(new_names):
        # Get the file extension
        file_extension = os.path.splitext(image_file)[1]
        # Construct the new file name with the new name and file extension
        new_file_name = f"{new_names[i]}{file_extension}"
        # Full path of the original and new files
        old_file_path = os.path.join(directory_path, image_file)
        new_file_path = os.path.join(directory_path, new_file_name)
        # Check if the file already exists and remove it
        if os.path.exists(new_file_path):
            os.remove(new_file_path)
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {image_file} -> {new_file_name}")

print("All images renamed successfully.")
