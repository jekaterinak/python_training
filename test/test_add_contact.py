# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.add(Contact(firstname="faname", lastname="lname", address="address", homephone="1",
                            mobilephone="2", workphone="3", fax="3", email="e1", email2="e2", email3="e3"))