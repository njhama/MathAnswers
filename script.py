import os

# Directory where the images are located
directory_path = "answers/chapter1/problems"

# List of exercise names
exercise_names = [
    "Exercise 1a", "Exercise 1b", "Exercise 2", "Exercise 3", "Exercise 4", "Exercise 5",
    "Exercise 6", "Exercise 7a", "Exercise 7b", "Exercise 7c", "Exercise 7d", "Exercise 8a",
    "Exercise 8b", "Exercise 8c", "Exercise 8d", "Exercise 9", "Exercise 10a", "Exercise 10b",
    "Exercise 10c", "Exercise 10d", "Exercise 10e", "Exercise 11a", "Exercise 11b", "Exercise 11c",
    "Exercise 12a", "Exercise 12b", "Exercise 13", "Exercise 14", "Exercise 15", "Exercise 16a",
    "Exercise 16b", "Exercise 17", "Exercise 18", "Exercise 19a", "Exercise 19b", "Exercise 19c",
    "Exercise 20a", "Exercise 20b", "Exercise 21", "Exercise 22", "Exercise 23", "Exercise 24",
    "Exercise 25", "Exercise 26", "Exercise 27", "Exercise 28", "Exercise 29", "Exercise 30",
    "Exercise 31", "Exercise 32", "Exercise 33a", "Exercise 33b"
]

# Get the list of image files in the directory
image_files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

# Sort the image files alphabetically
image_files.sort()

# Rename the image files with exercise names
for i, image_file in enumerate(image_files):
    if i < len(exercise_names):
        # Get the file extension
        file_extension = os.path.splitext(image_file)[1]
        # Construct the new file name with the exercise name and file extension
        new_file_name = f"{exercise_names[i]}{file_extension}"
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
