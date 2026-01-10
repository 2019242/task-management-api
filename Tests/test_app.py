import unittest
import json
from app import app, init_db


class TaskApiTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        init_db()

    def test_create_task(self):
        response = self.client.post(
            "/tasks",
            data=json.dumps({
                "username": "testuser",
                "title": "Test Task",
                "description": "Testing task creation",
                "deadline": "2025-12-31"
            }),
            content_type="application/json"
        )

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["message"], "Task created successfully")

    def test_get_tasks(self):
        response = self.client.get("/tasks")
        self.assertEqual(response.status_code, 200)

    def test_get_task_not_found(self):
        response = self.client.get("/tasks/9999")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["error"], "Task not found")

    def test_delete_task_not_found(self):
        response = self.client.delete("/tasks/9999")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["error"], "Task not found")


if __name__ == "__main__":
    unittest.main()
