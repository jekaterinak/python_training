from selenium.webdriver.firefox.webdriver import WebDriver


class Application:
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        self.open_home_page()
        self.wd.find_element_by_name("user").click()
        self.wd.find_element_by_name("user").clear()
        self.wd.find_element_by_name("user").send_keys(username)
        self.wd.find_element_by_id("LoginForm").click()
        self.wd.find_element_by_name("pass").click()
        self.wd.find_element_by_name("pass").clear()
        self.wd.find_element_by_name("pass").send_keys(password)
        self.wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_groups_page(self):
        self.wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        self.open_groups_page()
        # init group creation
        self.wd.find_element_by_name("new").click()
        # fill group from
        self.wd.find_element_by_name("group_name").click()
        self.wd.find_element_by_name("group_name").clear()
        self.wd.find_element_by_name("group_name").send_keys(group.name)
        self.wd.find_element_by_name("group_header").click()
        self.wd.find_element_by_name("group_header").clear()
        self.wd.find_element_by_name("group_header").send_keys(group.header)
        self.wd.find_element_by_name("group_footer").click()
        self.wd.find_element_by_name("group_footer").clear()
        self.wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        self.wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        self.wd.find_element_by_link_text("group page").click()

    def add_contact(self, contact):
        # init group creation
        self.wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.wd.find_element_by_name("firstname").click()
        self.wd.find_element_by_name("firstname").clear()
        self.wd.find_element_by_name("firstname").send_keys(contact.firstname)
        self.wd.find_element_by_name("lastname").click()
        self.wd.find_element_by_name("lastname").clear()
        self.wd.find_element_by_name("lastname").send_keys(contact.lastname)
        self.wd.find_element_by_name("address").click()
        self.wd.find_element_by_name("address").clear()
        self.wd.find_element_by_name("address").send_keys(contact.address)
        self.wd.find_element_by_name("home").click()
        self.wd.find_element_by_name("home").clear()
        self.wd.find_element_by_name("home").send_keys(contact.homephone)
        self.wd.find_element_by_name("mobile").click()
        self.wd.find_element_by_name("mobile").clear()
        self.wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        self.wd.find_element_by_name("work").click()
        self.wd.find_element_by_name("work").clear()
        self.wd.find_element_by_name("work").send_keys(contact.workphone)
        self.wd.find_element_by_name("fax").click()
        self.wd.find_element_by_name("fax").clear()
        self.wd.find_element_by_name("fax").send_keys(contact.fax)
        self.wd.find_element_by_name("email").click()
        self.wd.find_element_by_name("email").clear()
        self.wd.find_element_by_name("email").send_keys(contact.email)
        self.wd.find_element_by_name("email2").click()
        self.wd.find_element_by_name("email2").clear()
        self.wd.find_element_by_name("email2").send_keys(contact.email2)
        self.wd.find_element_by_name("email3").click()
        self.wd.find_element_by_name("email3").clear()
        self.wd.find_element_by_name("email3").send_keys(contact.email3)
        # submit contact creation
        self.wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()
