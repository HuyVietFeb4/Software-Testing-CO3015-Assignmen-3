# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class TimeLimitTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def login(self):
        driver = self.driver
        driver.get("https://www.google.com")
        driver.get("https://school.moodledemo.net/login/index.php")
        
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "username").send_keys("teacher")
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys("moodle26")
        driver.find_element(By.ID, "loginbtn").click()

    def test_time_limit(self, input_value):
        driver = self.driver
        driver.get("https://school.moodledemo.net/mod/assign/view.php?id=980&action=edit")

        try:
            driver.find_element(By.LINK_TEXT, "Settings").click()
        except NoSuchElementException:
            pass 

        enable_checkbox = driver.find_element(By.ID, "id_timelimit_enabled")
        if not enable_checkbox.is_selected():
            driver.execute_script("arguments[0].click();", enable_checkbox)
        
        time_field = driver.find_element(By.ID, "id_timelimit_number")
        time_field.clear()
        time_field.send_keys(str(input_value))
        
        driver.find_element(By.ID, "id_submitbutton").click()

        try:
            error_element = driver.find_element(By.ID, "id_error_timelimit")
            return error_element.text
        except NoSuchElementException:
            driver.get("https://school.moodledemo.net/mod/assign/view.php?id=980&action=edit")
            try:
                driver.find_element(By.LINK_TEXT, "Settings").click()
            except NoSuchElementException:
                pass
            return driver.find_element(By.ID, "id_timelimit_number").get_attribute("value")

    def quit(self):
        self.driver.quit()