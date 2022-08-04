import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class AddTrackers(unittest.TestCase):
    def test_add_trackers(self):
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

        # Tracker Link Click
        driver.find_element(By.ID, "menu__Performance").click()
        driver.find_element(By.ID, 'menu_performance_Configure').click()
        driver.find_element(By.ID, 'menu_performance_addPerformanceTracker').click()

        # Click Add
        add = driver.find_element(By.ID, 'btnAdd')
        add.click()
        time.sleep(3)

        tracker_name = driver.find_element(By.XPATH, '//*[@id="addPerformanceTracker_tracker_name"]')
        tracker_name.clear()
        tracker_name.send_keys('Test Tracker')
        time.sleep(1)

        employee_name = driver.find_element(By.XPATH, '//*[@id="addPerformanceTracker_employeeName_empName"]')
        employee_name.clear()
        employee_name.send_keys('Jasmine Morgan')
        time.sleep(1)

        reviewers = driver.find_element(By.ID, 'addPerformanceTracker_availableEmp')
        sel = Select(reviewers)
        sel.select_by_value('8')
        time.sleep(1)

        add_reviewer = driver.find_element(By.ID, 'btnAssignEmployee')
        add_reviewer.click()
        time.sleep(2)

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

    def test_add_trackers_required(self):
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

        # Tracker Link Click
        driver.find_element(By.ID, "menu__Performance").click()
        driver.find_element(By.ID, 'menu_performance_Configure').click()
        driver.find_element(By.ID, 'menu_performance_addPerformanceTracker').click()

        # Click Add
        add = driver.find_element(By.ID, 'btnAdd')
        add.click()
        time.sleep(3)

        tracker_name = driver.find_element(By.XPATH, '//*[@id="addPerformanceTracker_tracker_name"]')
        tracker_name.clear()
        tracker_name.send_keys('')
        time.sleep(1)

        employee_name = driver.find_element(By.XPATH, '//*[@id="addPerformanceTracker_employeeName_empName"]')
        employee_name.clear()
        employee_name.send_keys('Jasmine Morgan')
        time.sleep(1)
        
        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

        response_data = driver.find_element(By.CLASS_NAME,'validation-error').text
        self.assertIn(response_data,"Required")

    def test_add_trackers_invalid_employee(self):
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

        # Tracker Link Click
        driver.find_element(By.ID, "menu__Performance").click()
        driver.find_element(By.ID, 'menu_performance_Configure').click()
        driver.find_element(By.ID, 'menu_performance_addPerformanceTracker').click()

        # Click Add
        add = driver.find_element(By.ID, 'btnAdd')
        add.click()
        time.sleep(3)

        tracker_name = driver.find_element(By.XPATH, '//*[@id="addPerformanceTracker_tracker_name"]')
        tracker_name.clear()
        tracker_name.send_keys('Test tracker')
        time.sleep(1)

        employee_name = driver.find_element(By.XPATH, '//*[@id="addPerformanceTracker_employeeName_empName"]')
        employee_name.clear()
        employee_name.send_keys('Jasmine')
        time.sleep(1)
        
        reviewers = driver.find_element(By.ID, 'addPerformanceTracker_availableEmp')
        sel = Select(reviewers)
        sel.select_by_value('8')
        time.sleep(1)

        add_reviewer = driver.find_element(By.ID, 'btnAssignEmployee')
        add_reviewer.click()
        time.sleep(2)

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

        response_data = driver.find_element(By.CLASS_NAME,'validation-error').text
        self.assertIn(response_data,"invalid name")

        driver.close()

if __name__ == '__main__':
    unittest.main()
