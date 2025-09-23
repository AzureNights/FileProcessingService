import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def check():
    return "File Processing Service is running!"

@app.route("/upload-file", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "File not found"}), 400
    
    return jsonify({
        "message": "File uploaded successfully!",
        "filename": file.filename,
        "num_of_words": file.content_length
        # "text_length":
    }), 200

if __name__ == "__main__":
    app.run(debug=True)


