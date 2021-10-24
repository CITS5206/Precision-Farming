"""
    - it should test
        - when there are maps in the maps folder
            - The map page load
            - The map list show
            - The "view live" button work
            - Will redirect to tracking page
            - Tha "map" button show
            - The "stop and save" button show
        - when there are maps in the maps folder
            - The map page load
            - The map list will not show
            
   
 The University of Western Australia : 2021
 CITS5206 Professional Computing
 Group: Precision Farming
 Source Code
 Author: Clariza Look
 Date Created: 15-Oct-2021
 Version: 1.0
 State : Stable
 How to use: 
     - make sure server is running: python3 server.py (cd into that dir first)
     - python3 -m pytest test_emitoolkit.py
"""

import pytest
import time
import json
import shutil
import os
import sys
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestFarm():
  def setup_method(self, method):
    print(len(sys.argv))  
    self.driver = webdriver.Chrome(chromedriver_autoinstaller.install())
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_Map_exists(self):
    self.driver.get("http://localhost:3152/")
    assert self.driver.title == "EMI-Toolkit-Map"
    elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Field\')]")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, ".list:nth-child(2) .btn-intable:nth-child(1)").click()
    assert self.driver.title == "EMI-Toolkit-Tracking"
    elements = self.driver.find_elements(By.LINK_TEXT, "Map")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.ID, "saveImage")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.ID, "map")
    assert len(elements) > 0

if __name__ == "__main__":
    TestFarm()
    
