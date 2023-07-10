"""
Chunking and trying to find the signature date a the document that has headers with a date, with a "naive" approach 
(i. e. simply chunking the whole in x parts, asking a synthesis and asking the signature date for each part. Reconstructing the whole and asking the same question again once.
"""
import tiktoken
import os
import math
import chardet
import openai
from typing import List
import traceback
from typing import Callable
from datetime import datetime


def get_open_ai_response(message: str) -> str:
    """
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        temperature=0.8,
        max_tokens=700,
    )

    return response


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


def split_and_save_text(text: str,
                        chunks: int,
                        file_name: str,
                        save_location: str) -> str:
    """
    Split the given plain text into multiple chunks and save each chunk as a separate file.

    Args:
        text (str): The plain text to be split and saved.
        chunks (int): The number of files (or "chunks") to divide the text into.
        file_name (str): The base name of the output files.
        save_location (str): The path to the directory where the files will be saved.

    Returns:
        str: The location where the files are saved.
    """

    # Calculate the number of characters per file
    chars_per_file = len(text) // chunks

    # Create the directory if it doesn't exist
    os.makedirs(save_location, exist_ok=True)

    # Split the text into chunks
    chunks = [text[i:i+chars_per_file]
              for i in range(0, len(text), chars_per_file)]

    # Save each non-empty chunk as a separate file
    for i, chunk in enumerate(chunks):
        if chunk.strip():  # Check if the chunk contains non-whitespace characters
            file_path = os.path.join(save_location, f"{file_name}_{i+1}.txt")

            with open(file_path, 'w') as file:
                file.write(chunk)

    return save_location


def num_tokens_from_string(plain_txt: str, encoding_name: str) -> int:
    """
    Returns the number of tokens in a text string.

    Args:
        plain_txt (str): The input text string.
        encoding_name (str): The name of the encoding to use for tokenization.
                             Valid values: 'cl100k_base' (for gpt-4, gpt-3.5-turbo, text-embedding-ada-002).

    Returns:
        int: The number of tokens in the text string.

    Raises:
        ValueError: If an invalid encoding name is provided.

    Source:
        This function is based on the OpenAI Cookbook's example on how to count tokens with tiktoken.
        Link: https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
    """
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(plain_txt))

    # There is an underestimation that is about x% I noticed between local tokenization and remote
    # OpenAI
    real_token_count = round(num_tokens * 1.6)

    return real_token_count

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

    txt_files = [file for file in os.listdir(folder_path) if file.endswith(".txt")]
    return txt_files



def find_number_chunks(real_token_count: str, max_token: int) -> int:
    """
    Find number of text file the initial plain_txt needs to be split into
    in order to fit to the max otken allowed per request (as per OpenAI threshold)

    math.ceil() is a function from the math module in Python that returns the 
    smallest integer greater than or equal to a given number. It rounds up a floating-point 
    number to the nearest whole number.
    """
    number_of_parts = math.ceil(real_token_count / max_token)

    return number_of_parts


def exception_handler(func: Callable) -> Callable:
    """
    Decorator function for exception handling.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.

    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_message = traceback.format_exc()
            print(error_message)
            now = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"error_message_{now}.txt"
            with open(filename, "w") as file:
                file.write(error_message)
    return wrapper


@exception_handler
def main():
    save_location = "Output"
    large_txt_path = "Texts/Software Transfer Agreement.txt"
    plain_txt = open_text_file(large_txt_path)
    token_count = num_tokens_from_string(plain_txt, 'cl100k_base')
    n_parts = find_number_chunks(token_count, max_token=3000)
    file_name = os.path.splitext(os.path.basename(large_txt_path))[0]
    save_location = split_and_save_text(plain_txt,
                                        n_parts,
                                        file_name,
                                        save_location)


if __name__ == '__main__':
    main()

    message = "What kind of legal document is this? Who are the signatories? \
    What is the signature date of this legal document?"