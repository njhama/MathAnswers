import os

directory_path = "temp"

new_names = [
    "35d",
    "36a",
    "36b",
    "37a",
    "37b",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43a",
    "43b",
    "44a",
    "44b",
    "44c",
    "45a",
    "45b",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52a",
    "52b",
    "53",
    "54",
    "55a",
    "55b",
    "56"
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
