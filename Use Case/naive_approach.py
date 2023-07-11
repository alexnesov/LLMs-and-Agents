"""
Chunking and trying to find the signature date a the document that has headers with a date, with a "naive" approach 
(i. e. simply chunking the whole in x parts, asking a synthesis and asking the signature date for each part. Reconstructing the whole and asking the same question again once.
"""
import tiktoken
import os
import math
import openai
import traceback
from typing import Callable
from datetime import datetime

from utils.file_mgmt import get_txt_files, open_text_file

SAVE_LOCATION = "Output" # Where the chunkified text will be saved
LARGE_TXT_PTH = "Texts/Software Transfer Agreement.txt" # raw large text path

def get_open_ai_response(message: str) -> str:
    """
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        temperature=0.1,
        max_tokens=700,
    )



    return response['choices'][0]['text']


def split_and_save_text(text: str,
                        chunks: int,
                        file_name: str,
                        save_location: str) -> None:
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
def chunkify():

    plain_txt = open_text_file(LARGE_TXT_PTH)
    token_count = num_tokens_from_string(plain_txt, 'cl100k_base')
    n_parts = find_number_chunks(token_count, max_token=3000)
    file_name = os.path.splitext(os.path.basename(LARGE_TXT_PTH))[0]
    split_and_save_text(plain_txt,
                        n_parts,
                        file_name,
                        SAVE_LOCATION)


if __name__ == '__main__':
    # chunkify()
    files = get_txt_files(SAVE_LOCATION)
    print(files)

    for f in files:
        print(f"\n\nProcessing the following document: {f}\n")
        txt = open_text_file(f)
        message = f"What kind of Legal Document is this? \
                    Who are the signatories? \
                    What is the signature date of this legal document? --- \
                    Legal Document: {txt} --- \
                    Response format: 3 bullet points, strictly."

        answer = get_open_ai_response(message=message)
        print(answer)