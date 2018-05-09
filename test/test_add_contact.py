# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
import re


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


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    contact.firstname = app.remove_spaces(contact.firstname)
    contact.lastname = app.remove_spaces(contact.lastname)
    contact.address = app.remove_spaces(contact.address)
    contact.all_phones_from_home_page = app.contact.merge_phones_like_on_home_page(contact)
    contact.all_emails_from_home_page = app.contact.merge_emails_like_on_home_page(contact)
    old_contacts.append(contact)
    sorted_old_contacts = sorted(old_contacts, key=Contact.id_or_max)
    sorted_new_contacts = sorted(new_contacts, key=Contact.id_or_max)
    assert sorted_old_contacts == sorted_new_contacts
