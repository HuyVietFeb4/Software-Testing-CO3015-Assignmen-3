# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class GradeTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def login(self):
        driver = self.driver
        driver.get("https://www.google.com")
        driver.get("https://school.moodledemo.net/login/index.php")
        driver.find_element(By.ID, "username").send_keys("teacher")
        driver.find_element(By.ID, "password").send_keys("moodle26")
        driver.find_element(By.ID, "loginbtn").click()

    def test_grade_settings(self, max_grade, grade_to_pass):
        driver = self.driver
        driver.get("https://school.moodledemo.net/mod/assign/view.php?id=807&action=edit")
        
        try:
            driver.find_element(By.LINK_TEXT, "Settings").click()
        except NoSuchElementException:
            pass # Already on settings page
        # Ensure section is open
        try:
            gs = driver.find_element(By.ID, "collapseElement-7")
            if gs.get_attribute("aria-expanded") == "false":
                driver.execute_script("arguments[0].click();", gs)
        except: pass

        # Input values
        driver.find_element(By.ID, "id_grade_modgrade_point").clear()
        driver.find_element(By.ID, "id_grade_modgrade_point").send_keys(str(max_grade))
        
        driver.find_element(By.ID, "id_gradepass").clear()
        driver.find_element(By.ID, "id_gradepass").send_keys(str(grade_to_pass))

        # Submit
        save_btn = driver.find_element(By.ID, "id_submitbutton")
        driver.execute_script("arguments[0].click();", save_btn)

        # --- Refined Error Catching ---
        # List of possible error locations based on your TC004007 and others
        error_locators = [
            (By.ID, "fgroup_id_error_grade"),  # TC004007 (Negative/Invalid Max Grade)
            (By.ID, "id_error_gradepass"),      # TC004005 (Non-numeric Pass Grade)
            (By.ID, "id_error_grade_modgrade_point") # Alternate Max Grade error ID
        ]

        for locator in error_locators:
            try:
                # Wait up to 3 seconds for the specific error to have text
                element = WebDriverWait(driver, 3).until(
                    lambda d: d.find_element(*locator).text.strip() != ""
                )
                return driver.find_element(*locator).text
            except (NoSuchElementException, TimeoutException):
                continue

        # If no errors after waiting, return the saved values
        driver.get("https://school.moodledemo.net/mod/assign/view.php?id=807&action=edit")
        try:
            driver.find_element(By.LINK_TEXT, "Settings").click()
        except NoSuchElementException:
            pass # Already on settings page
        
        try:
            gs = driver.find_element(By.ID, "collapseElement-7")
            if gs.get_attribute("aria-expanded") == "false":
                driver.execute_script("arguments[0].click();", gs)
        except: pass

        return f"Max: {driver.find_element(By.ID, 'id_grade_modgrade_point').get_attribute('value')}, Pass: {driver.find_element(By.ID, 'id_gradepass').get_attribute('value')}"

    def quit(self):
        self.driver.quit()