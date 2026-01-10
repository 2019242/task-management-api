from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = "database.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            deadline TEXT
        )
    """)
    conn.commit()
    conn.close()


@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return jsonify([dict(task) for task in tasks])


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task_by_id(task_id):
    conn = get_db_connection()
    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()
    conn.close()

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(dict(task))


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or not all(
        key in data for key in ["username", "title", "description", "deadline"]
    ):
        return jsonify({"error": "Invalid input"}), 400

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO tasks (username, title, description, deadline) VALUES (?, ?, ?, ?)",
        (
            data["username"],
            data["title"],
            data["description"],
            data["deadline"],
        ),
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Task created successfully"}), 201


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.execute(
        "DELETE FROM tasks WHERE id = ?", (task_id,)
    )
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"message": "Task deleted successfully"}), 200


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)

