import unittest
from attr import field
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class AddReport(unittest.TestCase):
    def test_add_report(self):
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
        driver.find_element(By.LINK_TEXT, 'Reports').click()

        # Click Add
        add = driver.find_element(By.ID, 'btnAdd')
        add.click()
        time.sleep(3)

        report_name = driver.find_element(By.ID, 'report_report_name')
        report_name.clear()
        report_name.send_keys('Test Report')
        time.sleep(1)

        select_criteria = driver.find_element(By.ID, 'report_criteria_list')
        sel = Select(select_criteria)
        sel.select_by_value('job_title')
        time.sleep(1)

        add_criteria = driver.find_element(By.ID, 'btnAddConstraint')
        add_criteria.click()
        time.sleep(3)

        job_title = driver.find_element(By.ID, 'report_job_title')
        sel = Select(job_title)
        sel.select_by_value('26')
        time.sleep(1)

        field_group = driver.find_element(By.ID, 'report_display_groups')
        sel = Select(field_group)
        sel.select_by_value('display_group_4')
        time.sleep(1)

        job_title = driver.find_element(By.ID, 'report_display_field_list')
        sel = Select(job_title)
        sel.select_by_value('display_field_32')
        time.sleep(1)

        add_display = driver.find_element(By.ID, 'btnAddDisplayGroup')
        add_display.click()
        time.sleep(3)

        checkbox = driver.find_element(By.ID, 'display_group_4')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
            time.sleep(2)

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

    def test_add_report_empty(self):
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
        driver.find_element(By.LINK_TEXT, 'Reports').click()

        # Click Add
        add = driver.find_element(By.ID, 'btnAdd')
        add.click()
        time.sleep(3)

        report_name = driver.find_element(By.ID, 'report_report_name')
        report_name.clear()
        report_name.send_keys('')
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
