import os
from PIL import Image

def is_corrupted(image_path):
    """Check if the given image is corrupted."""
    try:
        with Image.open(image_path) as img:
            img.verify()  # This will check if the file appears to be a valid image
        return False
    except Exception:
        return True

def find_corrupted_jpgs_in_folder(folder_path):
    """Recursively check all JPGs in the folder and subfolders and discard corrupted ones."""
    corrupted_files = []

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.lower().endswith('.jpg'):
                file_path = os.path.join(dirpath, filename)
                if is_corrupted(file_path):
                    corrupted_files.append(file_path)

    return corrupted_files


if __name__ == "__main__":
    folder = input("Enter the path to the root folder containing JPGs: ").strip()
    
    corrupted_jpgs = find_corrupted_jpgs_in_folder(folder)
    if len(corrupted_jpgs) == 0:
        print("No corrupted JPGs found.")
        exit()
    inp = "."
    while inp not in ["y", "n", "show", ""]:
        inp = input(f"Found {len(corrupted_jpgs)} corrupted JPGs. Press Enter to delete them, or show to list them (y/n/show/Enter): ").strip().lower()
    if inp == "" or inp == "y":
        for file in corrupted_jpgs:
            os.remove(file)
        print("Deleted all corrupted JPGs.")
    elif inp == "show":
        for file in corrupted_jpgs:
            print(file)
    else:
        print("No files were deleted.")

    print("Finished checking for corrupted JPGs.")
