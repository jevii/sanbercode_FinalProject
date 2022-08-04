import unittest
from attr import field
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class AddVacancies(unittest.TestCase):
    def test_add_a_vacancies(self):
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

        # Recruitment
        driver.find_element(By.LINK_TEXT, 'Recruitment').click()
        driver.find_element(By.LINK_TEXT, 'Vacancies').click()

        # Click Add
        add = driver.find_element(By.ID, 'btnAdd')
        add.click()
        time.sleep(3)

        job_title = driver.find_element(By.ID, 'addJobVacancy_jobTitle')
        sel = Select(job_title)
        sel.select_by_value('12')
        time.sleep(1)

        vacancy_name = driver.find_element(By.ID, 'addJobVacancy_name')
        vacancy_name.clear()
        vacancy_name.send_keys('Vacancy Name test')
        time.sleep(1)

        hiring_manager = driver.find_element(By.ID, 'addJobVacancy_hiringManager')
        hiring_manager.clear()
        hiring_manager.send_keys('Ananya Dash')
        time.sleep(1)

        no_position = driver.find_element(By.ID, 'addJobVacancy_noOfPositions')
        no_position.clear()
        no_position.send_keys('59')
        time.sleep(1)

        description = driver.find_element(By.ID,'addJobVacancy_description')
        description.clear()
        description.send_keys('test descriptions bla bla bla')

        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(3)

    def test_add_vacancies_invalid(self):
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

        # Recruitment
        driver.find_element(By.LINK_TEXT, 'Recruitment').click()
        driver.find_element(By.LINK_TEXT, 'Vacancies').click()

        # Click Add
        add = driver.find_element(By.ID, 'btnAdd')
        add.click()
        time.sleep(3)

        job_title = driver.find_element(By.ID, 'addJobVacancy_jobTitle')
        sel = Select(job_title)
        sel.select_by_value('12')
        time.sleep(1)

        vacancy_name = driver.find_element(By.ID, 'addJobVacancy_name')
        vacancy_name.clear()
        vacancy_name.send_keys('Vacancy Test')
        time.sleep(1)

        hiring_manager = driver.find_element(By.ID, 'addJobVacancy_hiringManager')
        hiring_manager.clear()
        hiring_manager.send_keys('')
        time.sleep(1)

        no_position = driver.find_element(By.ID, 'addJobVacancy_noOfPositions')
        no_position.clear()
        no_position.send_keys('59')
        time.sleep(1)

        description = driver.find_element(By.ID,'addJobVacancy_description')
        description.clear()
        description.send_keys('test descriptions bla bla bla')

        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(3)

        response_data = driver.find_element(By.CLASS_NAME,'validation-error').text
        self.assertIn(response_data,"Invalid")

    def test_add_vacancies_exist(self):
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

        # Recruitment
        driver.find_element(By.LINK_TEXT, 'Recruitment').click()
        driver.find_element(By.LINK_TEXT, 'Vacancies').click()

        # Click Add
        add = driver.find_element(By.ID, 'btnAdd')
        add.click()
        time.sleep(3)

        job_title = driver.find_element(By.ID, 'addJobVacancy_jobTitle')
        sel = Select(job_title)
        sel.select_by_value('12')
        time.sleep(1)

        vacancy_name = driver.find_element(By.ID, 'addJobVacancy_name')
        vacancy_name.clear()
        vacancy_name.send_keys('Vacancy Name test')
        time.sleep(1)

        hiring_manager = driver.find_element(By.ID, 'addJobVacancy_hiringManager')
        hiring_manager.clear()
        hiring_manager.send_keys('Ananya Dash')
        time.sleep(1)

        no_position = driver.find_element(By.ID, 'addJobVacancy_noOfPositions')
        no_position.clear()
        no_position.send_keys('59')
        time.sleep(1)

        description = driver.find_element(By.ID,'addJobVacancy_description')
        description.clear()
        description.send_keys('test descriptions bla bla bla')

        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(3)

        response_data = driver.find_element(By.CLASS_NAME,'validation-error').text
        self.assertIn(response_data,"Already exists")

        driver.close()

if __name__ == '__main__':
    unittest.main()
