import os

folder_path = r'C:\folder'

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, filename.replace(".txt", ".csv"))
        os.rename(old_file, new_file)