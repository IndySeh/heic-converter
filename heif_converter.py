from PIL import Image
import pillow_heif  # Ensure you have this installed
import os
import shutil


def check_for_dir(dir_name: str) -> None:
    """Checks if a directory exists and creates it if it doesn't."""
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print(f"{dir_name} created in the current folder.")


def move_files(folder_name: str, file_name: str) -> None:
    """Moves a file to a specified folder within the current directory."""
    shutil.move(f"./{file_name}", f"./{folder_name}/{file_name}")
    print(f"{file_name} moved to {folder_name} folder.")


def heif_converter(file_extension: str, file: str) -> None:
    """Converts HEIF files to the specified format and moves them to a folder."""
    check_for_dir(dir_name=file_extension)
    print(f"Converting {file} to {file_extension}")

    file_name = os.path.splitext(file)[0]  # Split filename from extension
    new_file_name = f"{file_name}.{file_extension}"

    # Register HEIF opener (only needed once)
    pillow_heif.register_heif_opener()

    # Open the HEIC file and convert it
    try:
        image = Image.open(file)
        image.save(fp=new_file_name, format=file_extension.upper())
        print(f"{new_file_name} created ")

        move_files(folder_name=file_extension, file_name=new_file_name)
    except Exception as e:
        print(f"Error converting {file}: {e}")


# Iterate through files in the current directory
for file in os.scandir("."):
    if file.name.lower().endswith(".heic") and file.is_file():
        heif_converter(file_extension="webp", file=file.name)
