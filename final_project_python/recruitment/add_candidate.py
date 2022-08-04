import unittest
from attr import field
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class AddCandidate(unittest.TestCase):
    def test_add_candidate(self):
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
        driver.find_element(By.LINK_TEXT, 'Recruitment').click()

        # Click Add
        add = driver.find_element(By.ID, 'btnAdd')
        add.click()
        time.sleep(3)

        first_name = driver.find_element(By.XPATH, '//*[@id="addCandidate_firstName"]')
        first_name.clear()
        first_name.send_keys('Jarvis')
        time.sleep(1)

        middle_name = driver.find_element(By.XPATH, '//*[@id="addCandidate_middleName"]')
        middle_name.clear()
        middle_name.send_keys('Friday')
        time.sleep(1)

        last_name = driver.find_element(By.XPATH, '//*[@id="addCandidate_lastName"]')
        last_name.clear()
        last_name.send_keys('Test')
        time.sleep(1)

        email = driver.find_element(By.ID, 'addCandidate_email')
        email.clear()
        email.send_keys('test@mail.com')
        time.sleep(1)

        contact = driver.find_element(By.ID, 'addCandidate_contactNo')
        contact.clear()
        contact.send_keys('01237736')

        job_vacancy = driver.find_element(By.ID, 'addCandidate_vacancy')
        sel = Select(job_vacancy)
        sel.select_by_value('5')
        time.sleep(1)

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

    def test_add_candidate_required(self):
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
        driver.find_element(By.LINK_TEXT, 'Recruitment').click()

        # Click Add
        add = driver.find_element(By.ID, 'btnAdd')
        add.click()
        time.sleep(3)

        first_name = driver.find_element(By.XPATH, '//*[@id="addCandidate_firstName"]')
        first_name.clear()
        first_name.send_keys('')
        time.sleep(1)

        middle_name = driver.find_element(By.XPATH, '//*[@id="addCandidate_middleName"]')
        middle_name.clear()
        middle_name.send_keys('')
        time.sleep(1)

        last_name = driver.find_element(By.XPATH, '//*[@id="addCandidate_lastName"]')
        last_name.clear()
        last_name.send_keys('')
        time.sleep(1)

        email = driver.find_element(By.ID, 'addCandidate_email')
        email.clear()
        email.send_keys('')
        time.sleep(1)

        # contact = driver.find_element(By.ID, 'addCandidate_contactNo')
        # contact.clear()
        # contact.send_keys('01237736')

        # job_vacancy = driver.find_element(By.ID, 'addCandidate_vacancy')
        # sel = Select(job_vacancy)
        # sel.select_by_value('5')
        # time.sleep(1)

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

        response_data = driver.find_element(By.CLASS_NAME,'validation-error').text
        self.assertIn(response_data,"Required")

        driver.close()

if __name__ == '__main__':
    unittest.main()
