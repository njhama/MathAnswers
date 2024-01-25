import os

directory_path = "temp"

new_names = [
    "1a",
    "1b",
    "1c",
    "1d",
    "1e",
    "1f",
    "2a",
    "2b",
    "3",
    "4",
    "5a",
    "5b",
    "6",
    "7a",
    "7b",
    "7c",
    "8a",
    "8b",
    "8c",
    "9a",
    "9b",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18a",
    "18b",
    "18c",
    "18d",
    "19a",
    "19b",
    "20"
]


image_files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

image_files.sort()

for i, image_file in enumerate(image_files):
    if i < len(new_names):
       
        file_extension = os.path.splitext(image_file)[1]
  
        new_file_name = f"{new_names[i]}{file_extension}"
   
        old_file_path = os.path.join(directory_path, image_file)
        new_file_path = os.path.join(directory_path, new_file_name)
        
        if os.path.exists(new_file_path):
            os.remove(new_file_path)
     
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {image_file} -> {new_file_name}")

print("All images renamed successfully.")
