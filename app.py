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


@app.post("/notes")
def create_note():
    data = request.get_json(force=True) or {}
    title, body = str(data.get("title", ""))[:200], str(data.get("body", ""))[:5000]
    if not title:
        return jsonify({"error": "title required"}), 400
    conn = db()
    cur = conn.execute("INSERT INTO notes (title, body) VALUES (?, ?)", (title, body))
    conn.commit()
    return jsonify({"id": cur.lastrowid, "title": title, "body": body}), 201


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
