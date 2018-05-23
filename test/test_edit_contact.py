from model.contact import Contact
import random


def test_edit_some_contact_via_main_view_lastname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="faname", lastname="lname", address="address", homephone="1",
                                mobilephone="2", workphone="3", fax="3", email="e1", email2="e2", email3="e3"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact.lastname = "newlastname"
    app.contact.edit_contact_by_id_via_main_view(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    for index, contact_item in enumerate(old_contacts):
        if contact_item.id == contact.id:
            old_contacts[index] = contact
            break
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        for index, contact_item in enumerate(old_contacts):
            formatted_contact = app.contact.contact_like_on_webpage(contact_item)
            old_contacts[index] = formatted_contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_edit_some_contact_via_details_view_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="faname", lastname="lname", address="address", homephone="1",
                                mobilephone="2", workphone="3", fax="3", email="e1", email2="e2", email3="e3"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact.firstname = "newfirstname"
    app.contact.edit_contact_by_id_via_details_view(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    for index, contact_item in enumerate(old_contacts):
        if contact_item.id == contact.id:
            old_contacts[index] = contact
            break
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        for index, contact_item in enumerate(old_contacts):
            formatted_contact = app.contact.contact_like_on_webpage(contact_item)
            old_contacts[index] = formatted_contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
