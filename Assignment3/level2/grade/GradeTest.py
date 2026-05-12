# -*- coding: utf-8 -*-
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class GradeTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def format_val(self, val):
        try:
            f = float(val)
            return str(int(f)) if f == int(f) else str(f)
        except:
            return val

    def run_grade_test(self, row):
        driver = self.driver
        
        # 1. Login
        driver.get(row['login_url'])
        try:
            if "login" in driver.current_url:
                driver.find_element(By.ID, row['user_id']).send_keys(row['username'])
                driver.find_element(By.ID, row['pass_id']).send_keys(row['password'])
                driver.find_element(By.ID, row['login_btn_id']).click()
        except: pass

        # 2. Navigation
        driver.get(row['test_url'])
        try:
            driver.find_element(By.LINK_TEXT, row['settings_link']).click()
        except NoSuchElementException: pass

        # 3. Expand Grade Section
        try:
            gs = driver.find_element(By.ID, row['expand_id'])
            if gs.get_attribute("aria-expanded") == "false":
                driver.execute_script("arguments[0].click();", gs)
        except: pass

        # 4. Input Values
        driver.find_element(By.ID, row['max_id']).clear()
        driver.find_element(By.ID, row['max_id']).send_keys(str(row['input1']))
        driver.find_element(By.ID, row['pass_id_field']).clear()
        driver.find_element(By.ID, row['pass_id_field']).send_keys(str(row['input2']))

        # 5. Save
        driver.find_element(By.ID, row['save_btn_id']).click()

        # 6. Check Errors (Dynamic locators from CSV)
        locators = row['err_locators'].split(',')
        for loc_id in locators:
            try:
                error_el = WebDriverWait(driver, 2).until(
                    lambda d: d.find_element(By.ID, loc_id.strip()).text.strip() != ""
                )
                return driver.find_element(By.ID, loc_id.strip()).text
            except: continue

        # 7. Verification if no error
        driver.get(row['test_url'])
        try:
            driver.find_element(By.LINK_TEXT, row['settings_link']).click()
            gs = driver.find_element(By.ID, row['expand_id'])
            if gs.get_attribute("aria-expanded") == "false":
                driver.execute_script("arguments[0].click();", gs)
        except: pass

        v1 = self.format_val(driver.find_element(By.ID, row['max_id']).get_attribute("value"))
        v2 = self.format_val(driver.find_element(By.ID, row['pass_id_field']).get_attribute("value"))
        return f"{v1}, {v2}"

    def quit(self):
        self.driver.quit()

