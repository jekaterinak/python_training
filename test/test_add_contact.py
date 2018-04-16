# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact(firstname="faname", lastname="lname", address="address", homephone="1",
                            mobilephone="2", workphone="3", fax="3", email="e1", email2="e2", email3="e3"))
    app.session.logout()
