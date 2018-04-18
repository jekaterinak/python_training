class GroupHelper:


    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        self.app.wd.find_element_by_link_text("groups").click()

    def create(self, group):
        self.open_groups_page()
        # init group creation
        self.app.wd.find_element_by_name("new").click()
        # fill group from
        self.app.wd.find_element_by_name("group_name").click()
        self.app.wd.find_element_by_name("group_name").clear()
        self.app.wd.find_element_by_name("group_name").send_keys(group.name)
        self.app.wd.find_element_by_name("group_header").click()
        self.app.wd.find_element_by_name("group_header").clear()
        self.app.wd.find_element_by_name("group_header").send_keys(group.header)
        self.app.wd.find_element_by_name("group_footer").click()
        self.app.wd.find_element_by_name("group_footer").clear()
        self.app.wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        self.app.wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        self.open_groups_page()
        # select first group
        self.app.wd.find_element_by_name("selected[]").click()
        # submit deletion
        self.app.wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        self.app.wd.find_element_by_link_text("group page").click()

