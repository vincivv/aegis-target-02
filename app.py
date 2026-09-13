"""Notes service monitored by AEGIS."""
from flask import Flask, jsonify

app = Flask(__name__)
NOTES = {1: {"id": 1, "title": "welcome", "body": "hello"}}


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/notes")
def list_notes():
    return jsonify(list(NOTES.values()))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
