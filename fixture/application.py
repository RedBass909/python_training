from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def rerturn_to_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("%s" % group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("%s" % group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("%s" % group.footer)
        # submit form creation
        wd.find_element_by_name("submit").click()
        self.rerturn_to_group_page()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_id("content").click()
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def rertur_to_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def сreate_new_contact(self, contact):
        wd = self.wd
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
        wd.find_element_by_name("photo").send_keys(
            "C:\\Users\\drug_\\Downloads\\more_lodka_parusnik_145838_1600x1200.jpg")
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
        wd.find_element_by_xpath(
            "//div[@id='content']/form/select[4]/option[@value = '%s']" % contact.amonth).click()
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

        # def login(self, username="admin", password="secret"):
        #     wd = self.wd
        #     wd.find_element_by_name("user").clear()
        #     wd.find_element_by_name("user").send_keys("%s" % username)
        #     wd.find_element_by_name("pass").click()
        #     wd.find_element_by_name("pass").clear()
        #     wd.find_element_by_name("pass").send_keys("%s" % password)
        #     wd.find_element_by_xpath("//input[@value='Login']").click()

        # def open_home_page(self):
        #     wd = self.wd
        #     wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

