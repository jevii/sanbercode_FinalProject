import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Directory(unittest.TestCase):
    def test_directory(self):
        base_url = 'https://opensource-demo.orangehrmlive.com/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        # Find Elements
        username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        login_btn = driver.find_element(By.ID, 'btnLogin')

        # Login Action
        username.clear()
        username.send_keys('admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()

        # Assign Click
        driver.find_element(By.LINK_TEXT, 'Directory').click()

        name = driver.find_element(By.ID, 'searchDirectory_emp_name_empName')
        name.clear()
        name.send_keys('john smith')
        time.sleep(1)

        search = driver.find_element(By.ID, 'searchBtn')
        search.click()
        time.sleep(3)
                
        driver.close()

if __name__ == '__main__':
    unittest.main()