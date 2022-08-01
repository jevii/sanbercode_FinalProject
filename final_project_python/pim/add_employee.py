import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class AddEmployee(unittest.TestCase):
    def test_contact_details(self):
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

        # PIM Link Click
        driver.find_element(By.LINK_TEXT, 'PIM').click()

        # Click Add Employee
        driver.find_element(By.LINK_TEXT, 'Add Employee').click()

        first_name = driver.find_element(By.XPATH, '//*[@id="firstName"]')
        first_name.clear()
        first_name.send_keys('Jarvis')
        time.sleep(1)

        middle_name = driver.find_element(By.XPATH, '//*[@id="middleName"]')
        middle_name.clear()
        middle_name.send_keys('Friday')
        time.sleep(1)

        last_name = driver.find_element(By.XPATH, '//*[@id="lastName"]')
        last_name.clear()
        last_name.send_keys('Test')
        time.sleep(1)

        employee_id = driver.find_element(By.ID, 'employeeId')
        employee_id.clear()
        employee_id.send_keys('464026')
        time.sleep(1)

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

        driver.close()

if __name__ == '__main__':
    unittest.main()
