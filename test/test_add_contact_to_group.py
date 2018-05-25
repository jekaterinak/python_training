from model.contact import Contact
from model.group import Group
from generator import contact as f
from generator import group as t


def test_add_contact_to_group(app, orm):
    old_contacts = orm.get_contact_list()
    old_groups = orm.get_group_list()
    contact_for_group = Contact(firstname=f.random_string("firstname", 10), lastname=f.random_string("lastname", 20))
    group_for_contact = Group(name=t.random_string("name", 10), header=t.random_string("header", 20),
                              footer=t.random_string("footer", 20))
    app.contact.add(contact_for_group)
    new_contacts = orm.get_contact_list()
    added_contact = \
        [item for item in new_contacts if item not in old_contacts and item.firstname == contact_for_group.firstname][0]
    app.group.create(group_for_contact)
    new_groups = orm.get_group_list()
    added_group = \
        [item for item in new_groups if item not in old_groups and item.name == group_for_contact.name][0]
    app.contact.add_contact_to_group(added_contact, added_group)
    assert orm.is_contact_in_group(added_contact, added_group)
