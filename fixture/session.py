class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.app.open_home_page()
        self.app.wd.find_element_by_name("user").click()
        self.app.wd.find_element_by_name("user").clear()
        self.app.wd.find_element_by_name("user").send_keys(username)
        self.app.wd.find_element_by_id("LoginForm").click()
        self.app.wd.find_element_by_name("pass").click()
        self.app.wd.find_element_by_name("pass").clear()
        self.app.wd.find_element_by_name("pass").send_keys(password)
        self.app.wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        return len(self.app.wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        return self.app.wd.find_element_by_xpath("//div/div[1]/form/b").text == "(" + username + ")"

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
