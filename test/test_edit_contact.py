from model.contact import Contact


def test_edit_first_group_via_main_view_lastname(app):
    app.contact.edit_first_contact_via_main_view(Contact(lastname="newlastname"))


def test_edit_first_group_via_details_view_firstname(app):
    app.contact.edit_first_contact_via_details_view(Contact(firstname="newfirstname"))
