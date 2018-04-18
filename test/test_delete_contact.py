def test_delete_first_contact_via_main_view(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact_via_main_view()
    app.session.logout()

def test_delete_first_contact_via_edit_view(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact_via_edit_view()
    app.session.logout()