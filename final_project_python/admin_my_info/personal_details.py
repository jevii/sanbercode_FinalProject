import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Personal(unittest.TestCase):
    def test_personal_details(self):
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

        # My Info Click
        driver.find_element(By.LINK_TEXT, 'My Info').click()
        time.sleep(2)

        # Click Edit
        edit = driver.find_element(By.ID, 'btnSave')
        edit.click()
        time.sleep(2)

        first_name = driver.find_element(By.XPATH, '//*[@id="personal_txtEmpFirstName"]')
        first_name.clear()
        first_name.send_keys('Jarvis')
        time.sleep(1)

        middle_name = driver.find_element(By.XPATH, '//*[@id="personal_txtEmpMiddleName"]')
        middle_name.clear()
        middle_name.send_keys('Friday')
        time.sleep(1)

        last_name = driver.find_element(By.XPATH, '//*[@id="personal_txtEmpLastName"]')
        last_name.clear()
        last_name.send_keys('Test')
        time.sleep(1)

        employee_id = driver.find_element(By.ID, 'personal_txtEmployeeId')
        employee_id.clear()
        employee_id.send_keys('464026')
        time.sleep(1)

        other_id = driver.find_element(By.ID, 'personal_txtOtherID')
        other_id.clear()
        other_id.send_keys('4147852')
        time.sleep(1)

        driver_license_number = driver.find_element(By.ID, 'personal_txtLicenNo')
        driver_license_number.clear()
        driver_license_number.send_keys('DK0405837C00000')
        time.sleep(1)

        license_expiry_date = driver.find_element(By.ID, 'personal_txtLicExpDate')
        license_expiry_date.clear()
        license_expiry_date.send_keys('15-06-2024')

        ssn_number = driver.find_element(By.ID, 'personal_txtNICNo')
        ssn_number.clear()
        ssn_number.send_keys('123456')
        time.sleep(1)

        sin_number = driver.find_element(By.ID, 'personal_txtSINNo')
        sin_number.clear()
        sin_number.send_keys('78910')
        time.sleep(1)

        gender = driver.find_element(By.ID, 'personal_optGender_2')
        status = gender.is_selected()

        if not status:
            gender.click()
            time.sleep(1)

        marital_status = driver.find_element(By.ID, 'personal_cmbMarital')
        sel = Select(marital_status)
        sel.select_by_value('Single')
        time.sleep(1)

        nationality = driver.find_element(By.ID, 'personal_cmbNation')
        sel = Select(nationality)
        sel.select_by_value('83')
        time.sleep(1)

        date_of_birth = driver.find_element(By.XPATH, '//*[@id="personal_DOB"]')
        date_of_birth.clear()
        date_of_birth.send_keys('01-01-1996')
        time.sleep(1)

        nick_name = driver.find_element(By.ID, 'personal_txtEmpNickName')
        nick_name.clear()
        nick_name.send_keys('Jarvish')
        time.sleep(1)

        military_service = driver.find_element(By.ID, 'personal_txtMilitarySer')
        military_service.clear()
        military_service.send_keys('No')
        time.sleep(1)

        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

        # Custom Fields
        edit = driver.find_element(By.ID, 'btnEditCustom')
        edit.click()
        time.sleep(1)

        blood_type = driver.find_element(By.XPATH, '//*[@id="frmEmpCustomFields"]/ol/li/select')
        sel = Select(blood_type)
        sel.select_by_value('A+')
        time.sleep(1)

        save = driver.find_element(By.ID, 'btnEditCustom')
        save.click()
        time.sleep(1)

        driver.close()

if __name__ == '__main__':
    unittest.main()
