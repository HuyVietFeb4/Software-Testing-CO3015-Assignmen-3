# -*- coding: utf-8 -*-
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class TimeLimitTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def run_automated_test(self, row):
        driver = self.driver
        
        # 1. Dynamic Login
        driver.get(row['login_url'])
        try:
            driver.find_element(By.ID, row['user_id']).clear()
            driver.find_element(By.ID, row['user_id']).send_keys(row['username'])
            driver.find_element(By.ID, row['pass_id']).clear()
            driver.find_element(By.ID, row['pass_id']).send_keys(row['password'])
            driver.find_element(By.ID, row['login_btn_id']).click()
        except NoSuchElementException:
            pass # Already logged in

        # 2. Navigate to Test URL
        driver.get(row['test_url'])
        
        # 3. Dynamic Settings Click
        try:
            driver.find_element(By.LINK_TEXT, row['settings_link']).click()
        except NoSuchElementException:
            pass 

        # 4. Enable Checkbox (Moodle Time Limit specific)
        try:
            enable_checkbox = driver.find_element(By.ID, row['enable_id'])
            if not enable_checkbox.is_selected():
                driver.execute_script("arguments[0].click();", enable_checkbox)
        except NoSuchElementException:
            pass
        
        # 5. Dynamic Input
        time_field = driver.find_element(By.ID, row['input_id'])
        time_field.clear()
        time_field.send_keys(str(row['input_value']))
        
        # 6. Dynamic Save Button
        driver.find_element(By.ID, row['save_btn_id']).click()

        # 7. Check for error vs Verification
        try:
            error_element = driver.find_element(By.ID, row['error_id'])
            return error_element.text
        except NoSuchElementException:
            # Re-verify saved value
            driver.get(row['test_url'])
            try:
                driver.find_element(By.LINK_TEXT, row['settings_link']).click()
            except NoSuchElementException:
                pass
            
            raw_val = driver.find_element(By.ID, row['input_id']).get_attribute("value")
            # Format to remove .00 if necessary
            return str(int(float(raw_val))) if raw_val.replace('.', '', 1).isdigit() else raw_val

    def quit(self):
        self.driver.quit()