import unittest
import app
from app import tasks
import json

class AppTestCases(unittest.TestCase):

    def setUp(self):
        self.app = app.basic_api.test_client()

    def test_get_task(self):
        response = self.app.get('/todo/api/v1.0/tasks')
        data = json.loads(response.data)
        self.assertEqual(data['tasks'], tasks)

if __name__ == '__main__':
    unittest.main()