from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
import re


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        if not (self.wd.current_url.endswith("/addressbook/") and len(
                self.wd.find_elements_by_id("search-az")) > 0):
            self.wd.get("http://localhost/addressbook/")

    def clear_phones(self,s):
        return re.sub("[() -]", "", s)

    def remove_spaces(self,t):
        trimmed = t.strip()
        return re.sub("[ ]+", " ", trimmed)

    def destroy(self):
        self.wd.quit()
