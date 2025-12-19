from flask import Flask, request, jsonify, send_file
import json
import os

app = Flask(__name__)
WISH_FILE = "wishes.json"

# Ensure wishes file exists
if not os.path.exists(WISH_FILE):
    with open(WISH_FILE, "w") as f:
        json.dump([], f)

@app.route("/")
def index():
    return send_file("index.html")  # Serve HTML directly

@app.route("/submit_wish", methods=["POST"])
def submit_wish():
    data = request.json
    wish = data.get("wish")
    if wish:
        with open(WISH_FILE, "r") as f:
            wishes = json.load(f)
        wishes.append(wish)
        with open(WISH_FILE, "w") as f:
            json.dump(wishes, f)
        return jsonify({"status":"success"})
    return jsonify({"status":"error"}), 400

@app.route("/get_wishes")
def get_wishes():
    with open(WISH_FILE, "r") as f:
        wishes = json.load(f)
    return jsonify(wishes)

if __name__ == "__main__":
    app.run(debug=True)
