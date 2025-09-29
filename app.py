import os
from flask import Flask, request, jsonify
import logging
from service import is_allowed_file, process_file, save_to_database

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = Flask(__name__)

IN_MEMORY_DB = {}
id_count = 0

@app.route("/")
def check():
    logger.info("App: File Processing Service is running.")
    return "File Processing Service is running!"

@app.route("/upload-file", methods=["POST"])
def upload_file():
    global id_count
    logger.info("App: Upload file function is running.")

    if "file" not in request.files:
        logger.warning("App: There was no file uploaded.")
        return jsonify({"error": "No file uploaded."}), 400
    
    file = request.files["file"]

    if file.filename == "":
        logger.warning("App: No file name found.")
        return jsonify({"error": "File not found."}), 400
    
    if not is_allowed_file(file.filename):
        logger.warning("App: File type is not accepted.")
        return jsonify({"error": "File type is not accepted. Only .txt and .csv files can be uploaded."}), 400
    
    try:
        file_content = file.read().decode('utf-8')
        logger.info("App: File was read and decoded to a string.")

        num_lines, num_words = process_file(file_content) 
        logger.info(f"App: File '{file.filename}' was processed. Line count is {num_lines} and word count is {num_words}.")

        id_count += 1
        data = {
            "filename": file.filename,
            "num_of_lines": num_lines,
            "num_of_words": num_words,
            "status": "processed"
        }

        save_to_database(id, data, IN_MEMORY_DB)
        logger.info(f"App: Data successfully stored data for ID: {id}")
        
    
        logger.info(f"App: File '{file.filename}' was uploaded successfully.")
        return jsonify({
            "message": "File uploaded successfully!",
            "id": id_count,
            "filename": file.filename,
            "num_of_lines": num_lines,
            "num_of_words": num_words 
        }), 200
    
    except UnicodeDecodeError as e:
        logger.error(f"App: File was not decoded due to {e}", exc_info=True)
        return jsonify({"error": "Could not decode the file"}),400

    except Exception as e:
        logger.error(f"App: File was not processed due to {e}", exc_info=True)
        return jsonify({"error": f"Internal error occurred."}), 500

if __name__ == "__main__":
    app.run(debug=True)


