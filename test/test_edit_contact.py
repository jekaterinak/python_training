from model.contact import Contact


def test_edit_first_contact_via_main_view_lastname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="faname", lastname="lname", address="address", homephone="1",
                                mobilephone="2", workphone="3", fax="3", email="e1", email2="e2", email3="e3"))
    old_contacts = app.contact.get_contact_list()
    contact = old_contacts[0]
    contact.lastname = "newlastname"
    app.contact.edit_first_contact_via_main_view(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_first_contact_via_details_view_firstname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="faname", lastname="lname", address="address", homephone="1",
                                mobilephone="2", workphone="3", fax="3", email="e1", email2="e2", email3="e3"))
    old_contacts = app.contact.get_contact_list()
    contact = old_contacts[0]
    contact.firstname = "newfirstname"
    app.contact.edit_first_contact_via_details_view(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
