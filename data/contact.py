import random
import string
from model.contact import Contact

constant = [
    Contact(firstname="firstname1", lastname="lastname1", address="address1", homephone="1",
            mobilephone="2", workphone="3", email="email1", email2="email1", email3="email1"),
    Contact(firstname="firstname2", lastname="lastname2", address="address2", homephone="1",
            mobilephone="2", workphone="3", email="email2", email2="email2", email3="email2")

]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="", homephone="",
                    mobilephone="", workphone="", email="", email2="", email3="")] + [
               Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
                       address=random_string("address", 20), homephone=random_string("12", 5),
                       mobilephone=random_string("34", 5), workphone=random_string("56", 5),
                       email=random_string("email1", 5),
                       email2=random_string("email2", 5), email3=random_string("email3", 5))
               for i in range(5)
           ]
