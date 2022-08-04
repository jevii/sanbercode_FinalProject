import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Dashboard(unittest.TestCase):
    def test_dashboard(self):
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
        driver.find_element(By.LINK_TEXT, 'Assign Leave').click()
        driver.find_element(By.LINK_TEXT, 'Dashboard').click()

        driver.find_element(By.LINK_TEXT, 'Leave List').click()
        driver.find_element(By.LINK_TEXT, 'Dashboard').click()


        driver.find_element(By.LINK_TEXT, 'Timesheets').click()
        driver.find_element(By.LINK_TEXT, 'Dashboard').click()

        driver.find_element(By.LINK_TEXT, 'Apply Leave').click()
        driver.find_element(By.LINK_TEXT, 'Dashboard').click()

        driver.find_element(By.LINK_TEXT, 'My Leave').click()
        driver.find_element(By.LINK_TEXT, 'Dashboard').click()

        driver.find_element(By.LINK_TEXT, 'My Timesheet').click()
        driver.find_element(By.LINK_TEXT, 'Dashboard').click()
                
        driver.close()

if __name__ == '__main__':
    unittest.main()