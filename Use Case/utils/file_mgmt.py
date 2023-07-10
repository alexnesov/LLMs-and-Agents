import os
from typing import List
import chardet

def read_text_file(file_path: str) -> str:
    """
    Read the contents of a text file and return as a string.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The contents of the text file.

    Raises:
        ValueError: If the file_path is not a valid file.

    """
    if not os.path.isfile(file_path):
        raise ValueError(f"{file_path} is not a valid file.")

    with open(file_path, 'r') as file:
        contents = file.read()

    return contents



def create_folder_if_not_exists(path: str) -> None:
    """
    Check if a folder exists at the given path. If the folder doesn't exist, create it.

    Args:
        path (str): The path to the folder.

    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created folder: {path}")
    else:
        print(f"Folder already exists: {path}")




def open_text_file(file_path: str) -> str:
    """
    Read the contents of a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The contents of the text file.
    """
    with open(file_path, 'rb') as file:
        raw_contents = file.read()
        detected_encoding = chardet.detect(raw_contents)['encoding']
    file_contents = raw_contents.decode(detected_encoding)
    return file_contents


def get_txt_files(folder_path: str) -> List[str]:
    """
    Retrieve all .txt files in the specified folder.

    Args:
        folder_path (str): The path to the folder.

    Returns:
        List[str]: A list of file names with the .txt extension.

    Raises:
        ValueError: If the folder_path is not a valid directory.

    """
    if not os.path.isdir(folder_path):
        raise ValueError(f"{folder_path} is not a valid directory.")

    txt_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".txt")]
    return txt_files
