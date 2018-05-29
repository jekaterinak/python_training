from model.contact import Contact
from model.group import Group
from generator import contact as f
from generator import group as t


def test_add_contact_to_group(app, orm):
    old_contacts = None
    added_contact = None
    added_group = None
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="grnew", header="res", footer="tes"))
    existing_groups = orm.get_group_list()
    for group in existing_groups:
        available_contacts = orm.get_contacts_not_in_group(group=group)
        if len(available_contacts) > 0:
            added_contact = available_contacts[0]
            added_group = group
            break
    if added_contact is None:
        added_contact = Contact(firstname="faname", lastname="lname", address="address")
        old_contacts = orm.get_contact_list()
        app.contact.add(added_contact)
    if old_contacts is not None:
        new_contacts = orm.get_contact_list()
        added_contact = \
            [item for item in new_contacts if
             item not in old_contacts and item.firstname == added_contact.firstname][0]
    if added_group is None:
        added_group = orm.get_group_list()[0]
    app.contact.add_contact_to_group(added_contact, added_group)
    assert orm.is_contact_in_group(added_contact, added_group)
