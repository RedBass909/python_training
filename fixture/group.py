class GroupHelper:

    def __init__(self, app):
        self.app = app

    def rerturn_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
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
        wd = self.app.wd
        wd.find_element_by_id("content").click()
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit delition
        wd.find_element_by_name("delete").click()
        self.rerturn_to_group_page()

    def modification_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # click edit button
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").send_keys("%s" % group.name)
        wd.find_element_by_name("group_header").send_keys("%s" % group.header)
        wd.find_element_by_name("group_footer").send_keys("%s" % group.footer)
        # submit form update
        wd.find_element_by_name("update").click()
        self.rerturn_to_group_page()

