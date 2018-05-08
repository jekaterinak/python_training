from model.contact import Contact
import re


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

    def open_edit_view_for_first_contact(self):
        self.open_edit_view_by_index(1)

    def open_edit_view_by_index(self, index):
        self.app.wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[8]/a/img")[index].click()

    def open_details_view_by_index(self, index):
        self.app.wd.find_elements_by_xpath("//*[@id='maintable']/tbody/tr/td[7]/a/img")[index].click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        self.app.wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact_by_index_via_main_view(self):
        self.delete_contact_by_index_via_main_view(1)

    def delete_contact_by_index_via_main_view(self, index):
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # click delete button
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # accept contact deletion
        self.app.wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_first_contact_by_index_via_edit_view(self):
        self.delete_contact_by_index_via_edit_view(1)

    def delete_contact_by_index_via_edit_view(self, index):
        self.app.open_home_page()
        # click edit contact icon
        self.open_edit_view_by_index(index)
        # click delete button
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        self.contact_cache = None

    def edit_first_contact_by_index_via_main_view(self, contact):
        self.edit_contact_by_index_via_main_view(1, contact)

    def edit_contact_by_index_via_main_view(self, index, contact):
        self.app.open_home_page()
        # click edit contact icon
        self.open_edit_view_by_index(index)
        # fill contact form
        self.fill_contact_data(contact)
        # click update button
        self.app.wd.find_element_by_name("update").click()
        self.contact_cache = None

    def edit_first_contact_by_index_via_details_view(self, contact):
        self.edit_contact_by_index_via_details_view(1, contact)

    def edit_contact_by_index_via_details_view(self, index, contact):
        self.app.open_home_page()
        # click details icon
        self.open_details_view_by_index(index)
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
                cells = element.find_elements_by_tag_name("td")
                lname = element.find_element_by_css_selector("td:nth-child(2)").text
                fname = element.find_element_by_css_selector("td:nth-child(3)").text
                address = element.find_element_by_css_selector("td:nth-child(4)").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=fname, lastname=lname, address=address, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        self.app.open_home_page()
        self.open_edit_view_by_index(index)
        firstname = self.app.wd.find_element_by_name("firstname").get_attribute("value")
        lastname = self.app.wd.find_element_by_name("lastname").get_attribute("value")
        address = self.app.wd.find_element_by_name("address").get_attribute("value")
        id = self.app.wd.find_element_by_name("id").get_attribute("value")
        homephone = self.app.wd.find_element_by_name("home").get_attribute("value")
        workphone = self.app.wd.find_element_by_name("work").get_attribute("value")
        mobilephone = self.app.wd.find_element_by_name("mobile").get_attribute("value")
        fax = self.app.wd.find_element_by_name("fax").get_attribute("value")
        email = self.app.wd.find_element_by_name("email").get_attribute("value")
        email2 = self.app.wd.find_element_by_name("email2").get_attribute("value")
        email3 = self.app.wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id, homephone=homephone,
                       workphone=workphone, mobilephone=mobilephone, fax=fax, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        self.app.open_home_page()
        self.open_details_view_by_index(index)
        text = self.app.wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone)
