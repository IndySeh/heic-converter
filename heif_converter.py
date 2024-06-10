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



# from PIL import Image
# import pillow_heif
# import os
# import shutil

# class FileConverter:
#     def __init__(self, file_extension):
#         """
#         Constructor to initialize the FileConverter object.

#         Args:
#         - file_extension (str): Desired file extension to convert to (e.g., 'jpeg').

#         Returns:
#         - None
#         """
#         self.file_extension = file_extension

#     def check_for_dir(self):
#         """
#         Checks if the target directory exists and creates it if it doesn't.

#         Args:
#         - None

#         Returns:
#         - None
#         """
#         if not os.path.exists(self.file_extension) or not os.path.isdir(self.file_extension):
#             os.makedirs(self.file_extension, exist_ok=True)
#             print(f"{self.file_extension} directory created.")

#     def move_files(self, file_name):
#         """
#         Moves a file to the specified directory.

#         Args:
#         - file_name (str): Name of the file to be moved.

#         Returns:
#         - None
#         """
#         shutil.move(f"./{file_name}", f"./{self.file_extension}/{file_name}")
#         print(f"{file_name} moved to {self.file_extension} folder.")

#     def convert_to_format(self, file_name):
#         """
#         Converts a HEIF file to the specified format and moves it to the target directory.

#         Args:
#         - file_name (str): Name of the HEIF file to be converted.

#         Returns:
#         - None
#         """
#         self.check_for_dir()
#         print(f"Converting {file_name} to {self.file_extension}")

#         # Extract file name without extension
#         file_name_without_extension = os.path.splitext(file_name)[0]

#         # Construct new file name with the desired extension
#         new_file_name = f'{file_name_without_extension}.{self.file_extension}'

#         # Register HEIF opener
#         pillow_heif.register_heif_opener()

#         # Open the HEIF file
#         image = Image.open(file_name)

#         # Save the image in the target format
#         image.save(fp=f'{self.file_extension}/{new_file_name}', format=self.file_extension.upper())

#         print(f"{new_file_name} created ")
        
#         # Move the converted file to the target directory
#         self.move_files(file_name)

# # Iterate through files in the current directory
# for file in os.scandir("."):
#     if file.name.endswith("HEIC") and file.is_file():
#         # Create a FileConverter object for each HEIF file and convert it
#         converter = FileConverter(file_extension='jpeg')
#         converter.convert_to_format(file_name=file.name)
