# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_add_contact(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("Name")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("Second")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("Last")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("Test")
        # driver.find_element_by_name("photo").click()
        # driver.find_element_by_name("photo").clear()
        # driver.find_element_by_name("photo").send_keys("C:\\Users\\drug_\\Downloads\\more_lodka_parusnik_145838_1600x1200.jpg")
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("Test_Title")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("Te")
        driver.find_element_by_name("company").send_keys(Keys.DOWN)
        driver.find_element_by_name("company").send_keys(Keys.TAB)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("1234567")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("1234567")
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("1234567")
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys("1234567")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("test")
        driver.find_element_by_name("email").send_keys(Keys.DOWN)
        driver.find_element_by_name("email").send_keys(Keys.TAB)
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys("Test@mail.com")
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys("Test@mail.com")
        driver.find_element_by_name("email3").click()
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys("Test@mail.com")
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("16")
        driver.find_element_by_xpath("//option[@value='16']").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("September")
        driver.find_element_by_xpath("//option[@value='September']").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1990")
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text("16")
        driver.find_element_by_xpath("//div[@id='content']/form/select[3]/option[18]").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("June")
        driver.find_element_by_xpath("//div[@id='content']/form/select[4]/option[7]").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("1995")
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("None")
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("None")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("Best test")
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        driver.find_element_by_link_text("home page").click()
        driver.find_element_by_link_text("Logout").click()
    
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

if __name__ == "__main__":
    unittest.main()