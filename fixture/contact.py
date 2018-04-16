class ContactHelper:


    def __init__(self, app):
        self.app = app

    def add(self, contact):
        # init group creation
        self.app.wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.app.wd.find_element_by_name("firstname").click()
        self.app.wd.find_element_by_name("firstname").clear()
        self.app.wd.find_element_by_name("firstname").send_keys(contact.firstname)
        self.app.wd.find_element_by_name("lastname").click()
        self.app.wd.find_element_by_name("lastname").clear()
        self.app.wd.find_element_by_name("lastname").send_keys(contact.lastname)
        self.app.wd.find_element_by_name("address").click()
        self.app.wd.find_element_by_name("address").clear()
        self.app.wd.find_element_by_name("address").send_keys(contact.address)
        self.app.wd.find_element_by_name("home").click()
        self.app.wd.find_element_by_name("home").clear()
        self.app.wd.find_element_by_name("home").send_keys(contact.homephone)
        self.app.wd.find_element_by_name("mobile").click()
        self.app.wd.find_element_by_name("mobile").clear()
        self.app.wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        self.app.wd.find_element_by_name("work").click()
        self.app.wd.find_element_by_name("work").clear()
        self.app.wd.find_element_by_name("work").send_keys(contact.workphone)
        self.app.wd.find_element_by_name("fax").click()
        self.app.wd.find_element_by_name("fax").clear()
        self.app.wd.find_element_by_name("fax").send_keys(contact.fax)
        self.app.wd.find_element_by_name("email").click()
        self.app.wd.find_element_by_name("email").clear()
        self.app.wd.find_element_by_name("email").send_keys(contact.email)
        self.app.wd.find_element_by_name("email2").click()
        self.app.wd.find_element_by_name("email2").clear()
        self.app.wd.find_element_by_name("email2").send_keys(contact.email2)
        self.app.wd.find_element_by_name("email3").click()
        self.app.wd.find_element_by_name("email3").clear()
        self.app.wd.find_element_by_name("email3").send_keys(contact.email3)
        # subapp.wdt contact creation
        self.app.wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()