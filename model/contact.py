from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, address=None, homephone=None, mobilephone=None, workphone=None,
                 fax=None, email=None, email2=None, email3=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return '%s:%s:%s:%s:%s:%s' % (self.id, self.firstname, self.lastname, self.address,
                                      self.all_emails_from_home_page, self.all_phones_from_home_page)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname and self.address == other.address and \
               self.all_emails_from_home_page == other.all_emails_from_home_page and \
               self.all_phones_from_home_page == other.all_phones_from_home_page

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
