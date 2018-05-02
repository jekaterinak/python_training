from model.contact import Contact
from random import randrange


def test_edit_some_contact_via_main_view_lastname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="faname", lastname="lname", address="address", homephone="1",
                                mobilephone="2", workphone="3", fax="3", email="e1", email2="e2", email3="e3"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = old_contacts[index]
    contact.lastname = "newlastname"
    app.contact.edit_contact_by_index_via_main_view(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_some_contact_via_details_view_firstname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="faname", lastname="lname", address="address", homephone="1",
                                mobilephone="2", workphone="3", fax="3", email="e1", email2="e2", email3="e3"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = old_contacts[index]
    contact.firstname = "newfirstname"
    app.contact.edit_contact_by_index_via_details_view(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
