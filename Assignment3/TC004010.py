# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TC004010(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t_c004010(self):
        driver = self.driver
        driver.get("https://school.moodledemo.net/")
        driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("teacher")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("moodle25")
        driver.find_element_by_id("loginbtn").click()
        driver.find_element_by_xpath("//div[@id='course-info-container-59-3']/div/div").click()
        driver.find_element_by_xpath("//div[@id='yui_3_18_1_1_1776780753234_32']/a/span[3]/span[2]").click()
        driver.find_element_by_xpath("//li[@id='module-807']/div/div[2]/div[2]/div/div/a").click()
        driver.find_element_by_link_text("Settings").click()
        driver.find_element_by_id("collapseElement-7").click()
        driver.find_element_by_id("yui_3_18_1_1_1776780761854_994").click()
        driver.find_element_by_id("id_grade_modgrade_point").clear()
        driver.find_element_by_id("id_grade_modgrade_point").send_keys("1.1")
        driver.find_element_by_id("yui_3_18_1_1_1776780761854_998").click()
        driver.find_element_by_id("id_gradepass").clear()
        driver.find_element_by_id("id_gradepass").send_keys("1")
        driver.find_element_by_id("id_submitbutton").click()
        #ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=id_tags | label=Advanced]]
        #ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=id_tags | label=Basic]]
        #ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=id_tags | label=Intermediate]]
        driver.find_element_by_xpath("//div[@id='fitem_fgroup_id_grade']/div[2]").click()
        try: self.assertEqual("Invalid grade value. This must be an integer between 1 and 100", driver.find_element_by_id("fgroup_id_error_grade").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
