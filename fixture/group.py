from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        if text is not None:
            self.app.wd.find_element_by_name(field_name).click()
            self.app.wd.find_element_by_name(field_name).clear()
            self.app.wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_data(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def open_groups_page(self):
        if not (self.app.wd.current_url.endswith("/group.php") and len(self.app.wd.find_elements_by_name("new")) > 0):
            self.app.wd.find_element_by_link_text("groups").click()

    def create(self, group):
        self.open_groups_page()
        # init group creation
        self.app.wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_data(group)
        # submit group creation
        self.app.wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        self.open_groups_page()
        # select first group
        self.select_group_by_index(index)
        # submit deletion
        self.app.wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        self.open_groups_page()
        # select first group
        self.select_group_by_id(id)
        # submit deletion
        self.app.wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        self.app.wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        self.app.wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        self.app.wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_first_group(self, group):
        self.edit_group_by_index(0, group)

    def edit_group_by_index(self, index, group):
        self.open_groups_page()
        self.select_group_by_index(index)
        # click edit group button
        self.app.wd.find_element_by_name("edit").click()
        self.fill_group_data(group)
        # click update button
        self.app.wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group(self, group):
        self.open_groups_page()
        self.select_group_by_id(group.id)
        # click edit group button
        self.app.wd.find_element_by_name("edit").click()
        self.fill_group_data(group)
        # click update button
        self.app.wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def return_to_groups_page(self):
        self.app.wd.find_element_by_link_text("group page").click()

    def count(self):
        self.open_groups_page()
        return len(self.app.wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            self.open_groups_page()
            self.group_cache = []
            for element in self.app.wd.find_elements_by_css_selector('span.group'):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
