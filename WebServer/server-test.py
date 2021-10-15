"""
   This is a unit test for the web server
     - it should test if 'map' page (or '/') and '/tracking' page are loading properly (are returning to 200 status code)
     - it should test if other pages that is not map, tracking and '/' are serving a 404 message

   Author: Clariza Look
   Date Written: 15-Oct-2021
   
   How to use: 
     - python3 server-test.py
"""

import unittest
from app import app

class BasicTestCase(unittest.TestCase):

    
    # Ensure that map page loads correctly 
    def test_map_page_loads(self):
           
            tester = app.test_client(self)
            
            pages = ['/', '/map']
            for page in pages:
                    response = tester.get(page, content_type='html/text')
                    self.assertTrue(b'Map', response.data)

    # Check if page is not part of the website (we only have 3 pages) 
    # If the page is not part of the 3, that page should return a 404 error status code
    def test_404pages(self):
            tester = app.test_client(self)
            pages = ['/', '/map', '/heatmap', 'tracking'] # home page and /map is the same page
            for page in pages:
                    if (page != '/') or  (page != '/map') or  (page != '/heatmap') or (page != '/tracking'):
                            response = tester.get(page, content_type='html/text')
                            self.assertTrue(b'404 Not Found', response.data)

    # Ensure if Response is 200 for '/map' page
    # However since the map tiles are not enough cover the browser 
    # it returns Error 500 Internal server error pointing to 
    # the system cannot find the path specified: './app/static/maps'
    def test_map_page_loads(self):
           
            tester = app.test_client(self)
            
            pages = ['/', '/map']
            for page in pages:
                    response = tester.get(page, content_type='html/text')
                    self.assertEqual(response.status_code, 200) 
    
    # Ensure if Response is 200 for '/tracking' page
    # This page currently returns to Error 500 pointing
    # to FileNotFoundError: [Errno 2] No such file or directory: './leaflet-demo/d.json'
    def test_tracking_page_loads(self):
           
            tester = app.test_client(self)
            
            pages = ['/tracking/']
            for page in pages:
                    response = tester.get(page, content_type='html/text')
                    self.assertEqual(response.status_code, 200)                                       

if __name__ == '__main__':
    unittest.main()
    