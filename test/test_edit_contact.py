from model.contact import Contact


def test_edit_first_group_via_main_view(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact_via_main_view(Contact(firstname="newname", lastname="newlname", address="newaddress", homephone="4",
                            mobilephone="5", workphone="6", fax="7", email="e4", email2="e5", email3="e6"))
    app.session.logout()

def test_edit_first_group_via_details_view(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact_via_details_view(Contact(firstname="detailsnewname", lastname="newlname", address="newaddress", homephone="4",
                            mobilephone="5", workphone="6", fax="7", email="e4", email2="e5", email3="e6"))
    app.session.logout()