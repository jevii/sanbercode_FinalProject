from audioop import add
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class AddCustomers(unittest.TestCase):
    def test_add_customers(self):
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

        # Admin Link Click
        driver.find_element(By.LINK_TEXT, 'Time').click()
        driver.find_element(By.LINK_TEXT, 'Project Info').click()
        driver.find_element(By.LINK_TEXT, 'Customers').click()

        # Click View
        Add = driver.find_element(By.ID, 'btnAdd')
        Add.click()
        time.sleep(2)

        customer_name = driver.find_element(By.XPATH, '//*[@id="addCustomer_customerName"]')
        customer_name.clear()
        customer_name.send_keys('Jarvis test')
        time.sleep(1)

        description = driver.find_element(By.ID, 'addCustomer_description')
        description.clear()
        description.send_keys('test description bla bla bla')
        time.sleep(1)

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

    def test_add_customers_required(self):
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

        # Admin Link Click
        driver.find_element(By.LINK_TEXT, 'Time').click()
        driver.find_element(By.LINK_TEXT, 'Project Info').click()
        driver.find_element(By.LINK_TEXT, 'Customers').click()

        # Click View
        Add = driver.find_element(By.ID, 'btnAdd')
        Add.click()
        time.sleep(2)

        customer_name = driver.find_element(By.XPATH, '//*[@id="addCustomer_customerName"]')
        customer_name.clear()
        customer_name.send_keys('')
        time.sleep(1)

        description = driver.find_element(By.ID, 'addCustomer_description')
        description.clear()
        description.send_keys('')
        time.sleep(1)

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

        response_data = driver.find_element(By.CLASS_NAME,'validation-error').text
        self.assertIn(response_data,"Required")
        driver.close()

if __name__ == '__main__':
    unittest.main()
