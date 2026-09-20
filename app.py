"""Notes service monitored by AEGIS."""
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DB = "notes.db"


def db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, title TEXT, body TEXT)")
    return conn


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/notes")
def list_notes():
    rows = db().execute("SELECT id, title, body FROM notes ORDER BY id").fetchall()
    return jsonify([dict(r) for r in rows])


@app.get("/notes/<int:note_id>")
def get_note(note_id):
    row = db().execute("SELECT id, title, body FROM notes WHERE id = ?", (note_id,)).fetchone()
    return jsonify(dict(row)) if row else (jsonify({"error": "not found"}), 404)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
