# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="faname", lastname="lname", address="address", homephone="1",
                      mobilephone="2", workphone="3", fax="3", email="e1", email2="e2", email3="e3")
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    sorted_old_contacts = sorted(old_contacts, key=Contact.id_or_max)
    sorted_new_contacts = sorted(new_contacts, key=Contact.id_or_max)
    assert sorted_old_contacts == sorted_new_contacts
