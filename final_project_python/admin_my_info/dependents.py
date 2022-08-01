import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Dependents(unittest.TestCase):
    def test_dependents_details(self):
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
        username.send_keys('jarvis')

        password.clear()
        password.send_keys('masuk123')

        login_btn.click()

        # My Info Link Click
        driver.find_element(By.LINK_TEXT, 'My Info').click()

        # Click Dependents
        driver.find_element(By.LINK_TEXT, 'Dependents').click()

        add = driver.find_element(By.ID, 'btnAddDependent')
        add.click()
        time.sleep(2)

        name = driver.find_element(By.ID, 'dependent_name')
        name.click()
        name.send_keys('Jarvis Depent')

        relationship = driver.find_element(By.ID, 'dependent_relationshipType')
        sel = Select(relationship)
        sel.select_by_value('child')

        date_of_birth = driver.find_element(By.ID, 'dependent_dateOfBirth')
        date_of_birth.clear()
        date_of_birth.send_keys('01-01-2020')
        time.sleep(2)

        save = driver.find_element(By.ID, 'btnSaveDependent')
        save.click()
        time.sleep(2)

        driver.close()

if __name__ == '__main__':
    unittest.main()