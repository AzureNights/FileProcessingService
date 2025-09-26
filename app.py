import os
from flask import Flask, request, jsonify
import logging
from service import is_allowed_file

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/")
def check():
    logger.info("Service is running.")
    return "File Processing Service is running!"

@app.route("/upload-file", methods=["POST"])
def upload_file():
    logger.info("Upload file function is running.")

    if "file" not in request.files:
        logger.warning("There was no file uploaded.")
        return jsonify({"error": "No file uploaded."}), 400
    
    file = request.files["file"]

    if file.filename == "":
        logger.warning("No file name found.")
        return jsonify({"error": "File not found."}), 400
    
    if not is_allowed_file(file.filename):
        logger.warning("File type is not accepted.")
        return jsonify({"error": "File type is not accepted. Only .txt and .csv files can be uploaded."}), 400
    
    logger.info(f"File '{file.filename}' was uploaded successfully.")
    return jsonify({
        "message": "File uploaded successfully!",
        "filename": file.filename,
        "num_of_words": file.content_length
        # "text_length":
    }), 200

if __name__ == "__main__":
    app.run(debug=True)


