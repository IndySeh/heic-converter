from PIL import Image
import pillow_heif  # Ensure you have this installed
import os
import shutil

def check_for_dir(dir_name: str) -> None:
    """
    Checks if a directory exists and creates it if it doesn't.

    Args:
    - dir_name (str): Name of the directory.

    Returns:
    - None
    """
    if os.path.exists(dir_name) and os.path.isdir(dir_name):
        pass
    else:
        os.mkdir(dir_name)
        print(f"{dir_name} created in the current folder.")


def move_files(folder_name:str, file_name:str) -> None:
    """
    Moves a file to a specified folder within the current directory.

    Args:
    - folder_name (str): Destination folder, e.g., jpg or png.
    - file_name (str): Name of the file to be moved, e.g., photo.png.

    Returns:
    - None
    """
    shutil.move(f"./{file_name}", f"./{folder_name}/{file_name}")
    print(f"{file_name} moved to {folder_name} folder.")


def heif_converter(file_extension: str, file:str) -> None:
    """
    Converts HEIF files to the specified format and moves them to a folder.

    Args:
    - file_extension (str): Desired file extension, e.g., jpeg.
    - file (str): Name of the file to be converted.

    Returns:
    - None
    """
    check_for_dir(dir_name=file_extension)
    print(f"Converting {file} to {file_extension}")

    file_name = file.split(".")[0]  # Splitting photo.HEIC => ["photo", "HEIC"]
    new_file_name = f'{file_name}.{file_extension}'

    pillow_heif.register_heif_opener()

    image = Image.open(file)
    image.save(fp=f'{new_file_name}', format=file_extension.upper())

    print(f"{new_file_name} created ")
    
    move_files(folder_name=file_extension, file_name=new_file_name)


# Iterate through files in the current directory
for file in os.scandir("."):
    if file.name.endswith("HEIC") and file.is_file:
        heif_converter(file_extension='png', file=file.name)


