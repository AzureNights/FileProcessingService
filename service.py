import os
import logging
import pathlib

logger = logging.getLogger(__name__)

ALLOWED_EXTENSIONS = {".txt", ".csv"}

def is_allowed_file(filename):
    logger.info("Service: Validating file extension.")
    
    if "." not in filename:
        logger.info(f"There is no extension detected.")
        return False
    
    file_extension = pathlib.Path(filename).suffix.lower()
    result = file_extension in ALLOWED_EXTENSIONS

    logger.info(f"File {filename} is a {file_extension} file.")
    return result