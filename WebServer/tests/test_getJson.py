import unittest
import json
from app.routes import getJson

class testGetJson(unittest.TestCase):
    def test_getJson(self):
        path = './tests/test_getJson.json'
        result = json.dumps([
            ["-32.5041679", "116.9701738"], 
            ["-32.5041678", "116.9701739"],
            ["-32.5041672", "116.9701744"]
            ])
        
        self.assertEqual(getJson(path), result)

if __name__ == '__main__':
    unittest.main()