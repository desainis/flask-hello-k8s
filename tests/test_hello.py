from hello import app
import unittest

class ServerTestCase(unittest.TestCase):

    def setUp(self):
        # create a test client
        self.app = app.test_client()
        self.app.testing = True 

    def test_root_endpoint(self):
        result = self.app.get('/') 
        self.assertEqual(result.status_code, 404) 

    def test_health_endpoint(self):
        result = self.app.get('/health')
        self.assertEqual(result.json['message'], "UP")
        self.assertEqual(result.status_code, 200)
    
    def test_will_endpoint(self):
        result = self.app.get('/will')
        self.assertEqual(result.json['message'], "Hello World")
        self.assertEqual(result.status_code, 200)
    
    def test_ready_endpoint(self):
        result = self.app.get('/ready')
        self.assertEqual(result.json['message'], "It works!")
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()