import os
import logging
import pathlib

logger = logging.getLogger(__name__)

ALLOWED_EXTENSIONS = {".txt", ".csv"}

def is_allowed_file(filename):
    logger.info("Service: Starting file extension validation.")
    
    if "." not in filename:
        logger.info(f"Service: There is no extension detected.")
        return False
    
    file_extension = pathlib.Path(filename).suffix.lower()
    result = file_extension in ALLOWED_EXTENSIONS

    logger.info(f"Service: File {filename} is a {file_extension} file.")
    return result

def process_file(file_content):
    logger.info("Service: Starting file processing.")
    
    
    lines = file_content.splitlines()
    num_lines = len(lines)
    logger.info("Service: Number of lines determined.")

    num_words = 0
    for line in lines:
        words_per_line = line.split()
        num_words += len(words_per_line)
    logger.info("Service: Number of words determined.")

    return num_lines, num_words

def save_to_database(id, data, db):
    logger.info("Service: Starting saving to database.")

    db[id] = data
    logger.info(f"Service: Successfully saved ID: {id} to the database.")
