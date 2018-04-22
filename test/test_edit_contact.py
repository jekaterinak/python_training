from model.contact import Contact


def test_edit_first_group_via_main_view_lastname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="faname", lastname="lname", address="address", homephone="1",
                                mobilephone="2", workphone="3", fax="3", email="e1", email2="e2", email3="e3"))
    app.contact.edit_first_contact_via_main_view(Contact(lastname="newlastname"))


def test_edit_first_group_via_details_view_firstname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="faname", lastname="lname", address="address", homephone="1",
                                mobilephone="2", workphone="3", fax="3", email="e1", email2="e2", email3="e3"))
    app.contact.edit_first_contact_via_details_view(Contact(firstname="newfirstname"))
