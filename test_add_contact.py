# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from contact import Contact
import unittest, time, re

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.сreate_new_contact(wd, Contact(
            firstname="Name",
            middlename="Second",
            lastname="Last",
            nickname="Test",
            title="Test_Title",
            company="Test",
            home_number="1234567",
            mobile_number="1234567",
            work_number="1234567",
            fax="1234567",
            email="Test1@mail.com", email2="Test2@mail.com", email3="Test3@mail.com",
            homepage="Test.com",
            bday="16", bmonth="June", byear="2000",
            aday="21", amonth="September", ayear="1997",
            address2="None", phone2="None",
            notes="Best test"))
        self.rertur_to_homepage(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def rertur_to_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def сreate_new_contact(self, wd, contact):
        # init group creation
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("%s" % contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("%s" % contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("%s" % contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("%s" % contact.nickname)
        wd.find_element_by_name("photo").send_keys("C:\\Users\\drug_\\Downloads\\more_lodka_parusnik_145838_1600x1200.jpg")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("%s" % contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("%s" % contact.company)
        wd.find_element_by_name("company").send_keys(Keys.DOWN)
        wd.find_element_by_name("company").send_keys(Keys.TAB)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("%s" % contact.home_number)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("%s" % contact.mobile_number)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("%s" % contact.work_number)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("%s" % contact.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("%s" % contact.email)
        wd.find_element_by_name("email").send_keys(Keys.DOWN)
        wd.find_element_by_name("email").send_keys(Keys.TAB)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("%s" % contact.email2)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("%s" % contact.homepage)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("%s" % contact.email3)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("%s" % contact.bday)
        wd.find_element_by_xpath("//option[@value='%s']" % contact.bday).click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("%s" % contact.bmonth)
        wd.find_element_by_xpath("//option[@value='%s']" % contact.bmonth).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("%s" % contact.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("%s" % contact.aday)
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[@value = '%s']" % contact.aday).click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("%s" % contact.amonth)
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[@value = '%s']" % contact.amonth).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("%s" % contact.ayear)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("%s" % contact.address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("%s" % contact.phone2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("%s" % contact.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wd, username="admin", password="secret"):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
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
