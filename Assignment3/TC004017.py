# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TC004017(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t_c004017(self):
        driver = self.driver
        driver.get("https://school.moodledemo.net/")
        driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("teacher")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("moodle25")
        driver.find_element_by_id("loginbtn").click()
        driver.find_element_by_xpath("//div[@id='course-info-container-69-3']/div/div/a/span[3]/span[2]").click()
        driver.find_element_by_xpath("//li[@id='module-980']/div/div[2]/div[2]/div/div/a").click()
        driver.find_element_by_link_text("Settings").click()
        driver.find_element_by_id("yui_3_18_1_1_1776782410193_1019").click()
        driver.find_element_by_id("id_timelimit_number").clear()
        driver.find_element_by_id("id_timelimit_number").send_keys("50")
        driver.find_element_by_id("id_cancel").click()
        driver.find_element_by_link_text("Settings").click()
        driver.find_element_by_id("id_timelimit_number").click()
        try: self.assertEqual("30", driver.find_element_by_id("id_timelimit_number").get_attribute("value"))
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
