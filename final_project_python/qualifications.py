import imp


import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Qualifications(unittest.TestCase):
    def test_work_experience_details(self):
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

        # Click Qualifications
        driver.find_element(By.LINK_TEXT, 'Qualifications').click()

        # Add Work Experience
        add = driver.find_element(By.ID, 'addWorkExperience')
        add.click()
        time.sleep(2)

        cancel = driver.find_element(By.ID, 'btnWorkExpCancel')
        cancel.click()
        time.sleep(2)

        add = driver.find_element(By.ID, 'addWorkExperience')
        add.click()
        time.sleep(2)

        company = driver.find_element(By.ID, 'experience_employer')
        company.clear()
        company.send_keys('People N Tech')

        job_title = driver.find_element(By.ID, 'experience_jobtitle')
        job_title.clear()
        job_title.send_keys('SQA Engineer')

        from_date = driver.find_element(By.ID, 'experience_from_date')
        from_date.clear()
        from_date.send_keys('2022-01-01')

        to_date = driver.find_element(By.ID, 'experience_to_date')
        to_date.clear()
        to_date.send_keys('2022-06-15')

        comment = driver.find_element(By.ID, 'experience_comments')
        comment.clear()
        comment.send_keys('It was a very positive experience.')

        save = driver.find_element(By.ID, 'btnWorkExpSave')
        save.click()
        time.sleep(2)

        checkbox = driver.find_element(By.ID, 'workCheckAll')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
            time.sleep(2)

        delete = driver.find_element(By.ID, 'delWorkExperience')
        delete.click()
        time.sleep(2)

        # Education
        add = driver.find_element(By.ID, 'addEducation')
        add.click()
        time.sleep(2)

        cancel = driver.find_element(By.ID, 'btnEducationCancel')
        cancel.click()
        time.sleep(2)

        add = driver.find_element(By.ID, 'addEducation')
        add.click()
        time.sleep(2)

        level = driver.find_element(By.ID, 'education_code')
        sel = Select(level)
        sel.select_by_value('2')

        institute = driver.find_element(By.ID, 'education_institute')
        institute.clear()
        institute.send_keys('Daffodil International University')

        major_specialization = driver.find_element(By.ID, 'education_major')
        major_specialization.clear()
        major_specialization.send_keys('CSE')

        year = driver.find_element(By.ID, 'education_year')
        year.clear()
        year.send_keys('2018')

        gpa_score = driver.find_element(By.ID, 'education_gpa')
        gpa_score.clear()
        gpa_score.send_keys('3.50')

        start_date = driver.find_element(By.ID, 'education_start_date')
        start_date.clear()
        start_date.send_keys('2014-09-20')

        end_date = driver.find_element(By.ID, 'education_end_date')
        end_date.clear()
        end_date.send_keys('2018-10-25')

        save = driver.find_element(By.ID, 'btnEducationSave')
        save.click()
        time.sleep(2)

        checkbox = driver.find_element(By.ID, 'educationCheckAll')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
            time.sleep(2)

        delete = driver.find_element(By.ID, 'delEducation')
        delete.click()
        time.sleep(2)

        # Skills
        add = driver.find_element(By.ID, 'addSkill')
        add.click()
        time.sleep(2)

        cancel = driver.find_element(By.ID, 'btnSkillCancel')
        cancel.click()
        time.sleep(2)

        add = driver.find_element(By.ID, 'addSkill')
        add.click()
        time.sleep(2)

        skill = driver.find_element(By.ID, 'skill_code')
        sel = Select(skill)
        sel.select_by_value('7')

        years_of_experience = driver.find_element(By.ID, 'skill_years_of_exp')
        years_of_experience.clear()
        years_of_experience.send_keys('2')

        comment = driver.find_element(By.ID, 'skill_comments')
        comment.clear()
        comment.send_keys('Thank you for your hard work.')

        save = driver.find_element(By.ID, 'btnSkillSave')
        save.click()
        time.sleep(2)

        checkbox = driver.find_element(By.ID, 'skillCheckAll')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
            time.sleep(2)

        delete = driver.find_element(By.ID, 'delSkill')
        delete.click()
        time.sleep(2)

        # Languages
        add = driver.find_element(By.ID, 'addLanguage')
        add.click()
        time.sleep(2)

        cancel = driver.find_element(By.ID, 'btnLanguageCancel')
        cancel.click()
        time.sleep(2)

        add = driver.find_element(By.ID, 'addLanguage')
        add.click()
        time.sleep(2)

        language = driver.find_element(By.ID, 'language_code')
        sel = Select(language)
        sel.select_by_value('3')

        fluency = driver.find_element(By.ID, 'language_lang_type')
        sel = Select(fluency)
        sel.select_by_visible_text ('Writing')

        competency = driver.find_element(By.ID, 'language_competency')
        sel = Select(competency)
        sel.select_by_value('3')

        comment = driver.find_element(By.ID, 'language_comments')
        comment.clear()
        comment.send_keys('Keep it up.')

        save = driver.find_element(By.ID, 'btnLanguageSave')
        save.click()
        time.sleep(2)

        checkbox = driver.find_element(By.ID, 'languageCheckAll')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
            time.sleep(2)

        delete = driver.find_element(By.ID, 'delLanguage')
        delete.click()
        time.sleep(2)

        # License
        add = driver.find_element(By.ID, 'addLicense')
        add.click()
        time.sleep(2)

        cancel = driver.find_element(By.ID, 'btnLicenseCancel')
        cancel.click()
        time.sleep(2)

        add = driver.find_element(By.ID, 'addLicense')
        add.click()
        time.sleep(2)

        license_type = driver.find_element(By.ID, 'license_code')
        sel = Select(license_type)
        sel.select_by_value('4')

        license_number = driver.find_element(By.ID, 'license_license_no')
        license_number.clear()
        license_number.send_keys('849339')

        issued_date = driver.find_element(By.ID, 'license_date')
        issued_date.clear()
        issued_date.send_keys('2022-06-15')

        expiry_date = driver.find_element(By.ID, 'license_renewal_date')
        expiry_date.clear()
        expiry_date.send_keys('2032-06-15')

        save = driver.find_element(By.ID, 'btnLicenseSave')
        save.click()
        time.sleep(2)

        checkbox = driver.find_element(By.ID, 'licenseCheckAll')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
            time.sleep(2)

        delete = driver.find_element(By.ID, 'delLicense')
        delete.click()
        time.sleep(2)

        # Add Attachment
        # add = driver.find_element(By.ID, 'btnAddAttachment')
        # add.click()
        # time.sleep(2)

        # cancel = driver.find_element(By.ID, 'cancelButton')
        # cancel.click()
        # time.sleep(2)

        # add = driver.find_element(By.ID, 'btnAddAttachment')
        # add.click()
        # time.sleep(2)

        # select_file = driver.find_element(By.ID, 'ufile')
        # select_file.send_keys('C:\\Users\\morsh\\Desktop\\selenium_logo.png')
        # time.sleep(2)

        # comment = driver.find_element(By.ID, 'txtAttDesc')
        # comment.send_keys('The image uploaded successfully')

        # upload = driver.find_element(By.ID, 'btnSaveAttachment')
        # upload.click()

        # checkbox = driver.find_element(By.ID, 'attachmentsCheckAll')
        # status = checkbox.is_selected()
        # if not status:
        #     checkbox.click()
        #     time.sleep(2)

        # delete = driver.find_element(By.ID, 'btnDeleteAttachment')
        # delete.click()
        # time.sleep(2)

        driver.close()

if __name__ == '__main__':
    unittest.main()
