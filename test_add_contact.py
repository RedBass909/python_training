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
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.сreate_new_contact(wd)
        self.rertur_to_homepage(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def rertur_to_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def сreate_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Name")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Second")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Last")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("Test")
        # wd.find_element_by_name("photo").click()
        # wd.find_element_by_name("photo").clear()
        # wd.find_element_by_name("photo").send_keys("C:\\Users\\drug_\\Downloads\\more_lodka_parusnik_145838_1600x1200.jpg")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("Test_Title")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("Test")
        wd.find_element_by_name("company").send_keys(Keys.DOWN)
        wd.find_element_by_name("company").send_keys(Keys.TAB)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("1234567")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("1234567")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("1234567")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("1234567")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("test")
        wd.find_element_by_name("email").send_keys(Keys.DOWN)
        wd.find_element_by_name("email").send_keys(Keys.TAB)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("Test@mail.com")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("Test@mail.com")
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("Test@mail.com")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("16")
        wd.find_element_by_xpath("//option[@value='16']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("September")
        wd.find_element_by_xpath("//option[@value='September']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("16")
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[18]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("June")
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[7]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("1995")
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("None")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("None")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("Best test")
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wd):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
