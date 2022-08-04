import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class ApplyLeave(unittest.TestCase):
    def test_apply_leave(self):
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

        # Apply Link Click
        driver.find_element(By.LINK_TEXT, 'Apply Leave').click()

        leave_type = driver.find_element(By.ID, 'applyleave_txtLeaveType')
        sel = Select(leave_type)
        sel.select_by_value('8')
        time.sleep(1)

        date_leave_from = driver.find_element(By.XPATH, '//*[@id="applyleave_txtFromDate"]')
        date_leave_from.clear()
        date_leave_from.send_keys('2022-08-04')
        time.sleep(1)

        date_leave_to = driver.find_element(By.XPATH, '//*[@id="applyleave_txtToDate"]')
        date_leave_to.clear()
        date_leave_to.send_keys('2022-08-04')
        time.sleep(1)

        duration = driver.find_element(By.ID, 'applyleave_duration_duration')
        sel = Select(duration)
        sel.select_by_value('full_day')
        time.sleep(1)

        comment_leave = driver.find_element(By.XPATH, '//*[@id="applyleave_txtComment"]')
        comment_leave.clear()
        comment_leave.send_keys('test comment apply leave')
        time.sleep(1)

        # Click Apply
        apply_btn = driver.find_element(By.ID, 'applyBtn')
        apply_btn.click()
        time.sleep(2)

    def test_apply_leave_type_required(self):
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

        # Apply Link Click
        driver.find_element(By.LINK_TEXT, 'Apply Leave').click()

        leave_type = driver.find_element(By.ID, 'applyleave_txtLeaveType')
        sel = Select(leave_type)
        sel.select_by_value('')
        time.sleep(1)

        date_leave_from = driver.find_element(By.XPATH, '//*[@id="applyleave_txtFromDate"]')
        date_leave_from.clear()
        date_leave_from.send_keys('2022-08-04')
        time.sleep(1)

        date_leave_to = driver.find_element(By.XPATH, '//*[@id="applyleave_txtToDate"]')
        date_leave_to.clear()
        date_leave_to.send_keys('2022-08-04')
        time.sleep(1)

        # Click Apply
        apply_btn = driver.find_element(By.ID, 'applyBtn')
        apply_btn.click()
        time.sleep(2)

        response_data = driver.find_element(By.CLASS_NAME,'validation-error').text
        self.assertIn(response_data,"Required")

    def test_apply_leave_date_invalid(self):
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
        driver.find_element(By.LINK_TEXT, 'Apply Leave').click()

        
        leave_type = driver.find_element(By.ID, 'applyleave_txtLeaveType')
        sel = Select(leave_type)
        sel.select_by_value('8')
        time.sleep(1)

        date_leave_from = driver.find_element(By.XPATH, '//*[@id="applyleave_txtFromDate"]')
        date_leave_from.clear()
        date_leave_from.send_keys('04-08-2022')
        time.sleep(1)

        date_leave_to = driver.find_element(By.XPATH, '//*[@id="applyleave_txtToDate"]')
        date_leave_to.clear()
        date_leave_to.send_keys('04-08-2022')
        time.sleep(1)

        # Click Apply
        apply_btn = driver.find_element(By.ID, 'applyBtn')
        apply_btn.click()
        time.sleep(2)
        
        response_data = driver.find_element(By.CLASS_NAME,'validation-error').text
        self.assertIn(response_data,"Should be a valid date in yyyy-mm-dd format")

        driver.close()

if __name__ == '__main__':
    unittest.main()
