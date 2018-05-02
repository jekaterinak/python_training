from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        if text is not None:
            self.app.wd.find_element_by_name(field_name).click()
            self.app.wd.find_element_by_name(field_name).clear()
            self.app.wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_data(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)

    def add(self, contact):
        # init group creation
        self.app.wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_data(contact)
        # submit contact creation
        self.app.wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def open_edit_view(self):
        self.app.wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def delete_first_contact_via_main_view(self):
        self.app.open_home_page()
        # select first contact
        self.app.wd.find_element_by_name("selected[]").click()
        # click delete button
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # accept contact deletion
        self.app.wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_first_contact_via_edit_view(self):
        self.app.open_home_page()
        # select first contact
        self.app.wd.find_element_by_name("selected[]").click()
        self.open_edit_view()
        # click delete button
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        self.contact_cache = None

    def edit_first_contact_via_main_view(self, contact):
        self.app.open_home_page()
        # select first contact
        self.app.wd.find_element_by_name("selected[]").click()
        # click edit contact icon
        self.open_edit_view()
        # fill contact form
        self.fill_contact_data(contact)
        # click update button
        self.app.wd.find_element_by_name("update").click()
        self.contact_cache = None

    def edit_first_contact_via_details_view(self, contact):
        self.app.open_home_page()
        # select first contact
        self.app.wd.find_element_by_name("selected[]").click()
        # click details icon
        self.app.wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()
        # click modify button
        self.app.wd.find_element_by_xpath("//*[@id='content']/form[1]/input[2]").click()
        self.fill_contact_data(contact)
        # click update button
        self.app.wd.find_element_by_name("update").click()
        self.contact_cache = None

    def count(self):
        self.app.open_home_page()
        return len(self.app.wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            self.app.open_home_page()
            self.contact_cache = []
            for element in self.app.wd.find_elements_by_css_selector('tr[name="entry"]'):
                lname = element.find_element_by_css_selector("td:nth-child(2)").text
                fname = element.find_element_by_css_selector("td:nth-child(3)").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=fname, lastname=lname, id=id))
        return list(self.contact_cache)
