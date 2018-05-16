# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts):
    contact = json_contacts
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
