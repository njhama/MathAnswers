import os

directory_path = "answers/chapter2/Problems"

new_names = [
    "01",
    "02",
    "03",
    "04a",
    "04b",
    "05a",
    "05b",
    "05c",
    "05d",
    "06a",
    "06b",
    "06c",
    "06d",
    "07a",
    "07b",
    "07c",
    "08a",
    "08b",
    "08c",
    "09",
    "10a",
    "10b",
    "11a",
    "11b",
    "12a",
    "12b",
    "12c",
    "13a",
    "13b",
    "13c",
    "13d",
    "13e",
    "14",
    "15a",
    "15b",
    "15c",
    "15d",
    "15e",
    "16a",
    "16b",
    "16c",
    "16d",
    "16e",
    "16f",
    "16g",
    "17",
    "18",
    "19",
    "20",
    "21a",
    "21b",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28a",
    "28b",
    "28c",
    "29aa",
    "29ab",
    "29ac",
    "29b",
    "29c",
    "30a",
    "30b",
    "30c",
    "31a",
    "31b",
    "32",
    "33",
    "34",
    "35a",
    "35b",
    "35c",
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
