from model.contact import Contact
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_delete_some_contact_via_main_view(app, db,check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="faname", lastname="lname", address="address", homephone="1",
                                mobilephone="2", workphone="3", fax="3", email="e1", email2="e2", email3="e3"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id_via_main_view(contact.id)
    WebDriverWait(app.wd, 5).until(EC.url_matches(app.base_url), 'Delete failed, not redirected to main page?')
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        for index, contact_item in enumerate(old_contacts):
            formatted_contact = app.contact.contact_like_on_webpage(contact_item)
            old_contacts[index] = formatted_contact
        assert sorted(old_contacts, key=Contact.id_or_max)==sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

def test_delete_some_contact_via_edit_view(app, db,check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="faname", lastname="lname", address="address", homephone="1",
                                mobilephone="2", workphone="3", fax="3", email="e1", email2="e2", email3="e3"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id_via_edit_view(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        for index, contact_item in enumerate(old_contacts):
            formatted_contact = app.contact.contact_like_on_webpage(contact_item)
            old_contacts[index] = formatted_contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
