from model.contact import Contact


def test_delete_first_contact_via_main_view(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="faname", lastname="lname", address="address", homephone="1",
                                mobilephone="2", workphone="3", fax="3", email="e1", email2="e2", email3="e3"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact_via_main_view()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def test_delete_first_contact_via_edit_view(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="faname", lastname="lname", address="address", homephone="1",
                                mobilephone="2", workphone="3", fax="3", email="e1", email2="e2", email3="e3"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact_via_edit_view()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
