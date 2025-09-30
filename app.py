import os
from flask import Flask, request, jsonify
import logging
from service import is_allowed_file, process_file, save_to_database

# Setting up the logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = Flask(__name__)

IN_MEMORY_DB = {}
id_count = 0

# Basic route to check if the app is working 
@app.route("/")
def check():
    logger.info("App: File Processing Service is running.")
    return "File Processing Service is running!"

# File upload route 
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

        # Saving func - from service  
        save_to_database(id_count, data, IN_MEMORY_DB)
        logger.info(f"App: Data successfully stored data for ID: {id_count}")

        # Successfully uploaded - json message
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
    
# Route tp check on all uploaded files 
@app.route("/view/all", methods=["GET"])
def view_all_files():
    logger.info("App: View all files function is running.")

    if not IN_MEMORY_DB:
        logger.info("App: In-memory database is empty.")
        return jsonify(IN_MEMORY_DB), 200
    
    logger.info("App: Showing all entries in the database.")
    return jsonify(IN_MEMORY_DB), 200

# Route to check for individual entries 
@app.route("/view/<int:id>", methods=["GET"])
def view_file_info(id):
    logger.info("App: View file function is running.")

    result = IN_MEMORY_DB.get(id)

    if result:
        logger.info(f"App: File ID: {id} found.")
        return jsonify(result), 200
    else:
        logger.info(f"App: File ID: {id} could not be retrieved.")
        return jsonify({"error": f"File ID could not be found."}), 404


if __name__ == "__main__":
    app.run(debug=True)


