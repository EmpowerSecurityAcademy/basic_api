import unittest
import app
from app import tasks
import json

class AppTestCases(unittest.TestCase):

    def setUp(self):
        self.app = app.basic_api.test_client()

    def test_get_tasks(self):
        response = self.app.get('/todo/api/v1.0/tasks')
        data = json.loads(response.data)
        self.assertEqual(data['tasks'], tasks)

    def test_post_tasks(self):
        response = self.app.post('/todo/api/v1.0/tasks', 
                       data=json.dumps(dict(title='Eat a sandwich', description='Enjoy it a lot', done=0)),
                       content_type = 'application/json')
        data = json.loads(response.data)
        self.assertEqual(data['id'], 3)

    def test_get_task(self):
        response = self.app.get('/todo/api/v1.0/tasks/1')
        data = json.loads(response.data)
        self.assertEqual(data['task'], {
                                            'id': 1,
                                            'title': 'Buy groceries',
                                            'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
                                            'done': False
                                        })

    def test_put_task(self):
        response = self.app.put('/todo/api/v1.0/tasks/1', 
                       data=json.dumps(dict(title='Order from Instacart', description='Milk, Cheese, Pizza, Fruit, Tylenol, Burrito', done=0)),
                       content_type = 'application/json')
        data = json.loads(response.data)
        self.assertEqual(data['task'], {
                                            'id': 1,
                                            'title': 'Order from Instacart',
                                            'description': 'Milk, Cheese, Pizza, Fruit, Tylenol, Burrito',
                                            'done': False
                                        })

    def test_delete_task(self):
        self.app.post('/todo/api/v1.0/tasks', 
                       data=json.dumps(dict(title='Eat a sandwich', description='Enjoy it a lot', done=0)),
                       content_type = 'application/json')
        response = self.app.delete('/todo/api/v1.0/tasks/3')
        data = json.loads(response.data)
        self.assertEqual(data['deleted_id'], 3)

if __name__ == '__main__':
    unittest.main()