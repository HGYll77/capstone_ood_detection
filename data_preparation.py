import os
import kagglehub
import shutil

# Download the dataset into the datasets folder
path = kagglehub.dataset_download("ambityga/imagenet100")

# Print the download path for confirmation
print(f"Dataset downloaded to: {path}")

# Define the destination folder within the dataset path
destination_root = os.path.join(path, "train")  # Modify the destination as needed (e.g., within "train" subdirectory)

# Ensure the destination folder exists
os.makedirs(destination_root, exist_ok=True)

# Loop over each train.X folder and move the class folders to the consolidated train folder
for subfolder in os.listdir(path):
    if subfolder.startswith("train.X"):  # Only consider folders that start with "train.X"
        subfolder_path = os.path.join(path, subfolder)
        for class_folder in os.listdir(subfolder_path):
            class_folder_path = os.path.join(subfolder_path, class_folder)
            destination_class_folder = os.path.join(destination_root, class_folder)

            # If the destination class folder doesn't exist, move it entirely
            if not os.path.exists(destination_class_folder):
                shutil.move(class_folder_path, destination_class_folder)
            else:
                # If the destination class folder exists, move individual images to avoid overwriting
                for img_file in os.listdir(class_folder_path):
                    src_img_path = os.path.join(class_folder_path, img_file)
                    dest_img_path = os.path.join(destination_class_folder, img_file)
                    if not os.path.exists(dest_img_path):  # Avoid overwriting
                        shutil.move(src_img_path, dest_img_path)

        # After processing all class folders in the current train.X, delete the empty train.X folder
        os.rmdir(subfolder_path)

# Rename 'val.X' to 'val'
old_folder_path = os.path.join(path, 'val.X')
new_folder_path = os.path.join(path, 'val')
os.rename(old_folder_path, new_folder_path)

# List all subdirectories in the path
subfolders = [folder for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder))]

# Print the subfolder names
for subfolder in subfolders:
    print(subfolder)
