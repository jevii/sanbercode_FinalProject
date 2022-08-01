import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class ForgotPawwsord(unittest.TestCase):
    def test_forgot(self):
        base_url = 'https://opensource-demo.orangehrmlive.com/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        # Find Elements
        driver.get ('https://opensource-demo.orangehrmlive.com/index.php/auth/requestPasswordResetCode')

        username = driver.find_element(By.XPATH, '//*[@id="securityAuthentication_userName"]')
        username.clear()
        username.send_keys('admin')

        forgot = driver.find_element(By.ID, 'btnSearchValues')
        forgot.click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()