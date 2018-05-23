import re
from random import randrange
from model.contact import Contact


def test_contact_fields_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="faname", lastname="lname", address="address", homephone="1",
                                mobilephone="2", workphone="3", fax="3", email="e1", email2="e2", email3="e3"))
    contacts_from_db = db.get_contact_list()
    for index, contact_item in enumerate(contacts_from_db):
        formatted_contact = app.contact.contact_like_on_webpage(contact_item)
        contacts_from_db[index] = formatted_contact
    assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(contacts_from_db,
                                                                                   key=Contact.id_or_max)

# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#     assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
