from model.contact import Contact
from model.group import Group
from generator import contact as f
from generator import group as t


def test_delete_contact_to_group(app, orm):
    contact_in_group = None
    group_for_removing_contact = None
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="grnew", header="res", footer="tes"))
    existing_groups = orm.get_group_list()
    for group in existing_groups:
        available_contacts = orm.get_contacts_in_group(group=group)
        if len(available_contacts) > 0:
            contact_in_group = available_contacts[0]
            group_for_removing_contact = group
            break
    if contact_in_group is None:
        existing_contacts = orm.get_contact_list()
        if len(existing_contacts) > 0:
            contact_in_group = existing_contacts[0]
        else:
            app.contact.add(Contact(firstname="faname", lastname="lname", address="address"))
            contact_in_group = orm.get_contact_list()[0]
        group_for_removing_contact = existing_groups[0]
        app.contact.add_contact_to_group(contact_in_group, group_for_removing_contact)
        assert orm.is_contact_in_group(contact_in_group, group_for_removing_contact)
    app.contact.delete_contact_from_group(contact_in_group, group_for_removing_contact)
    assert not orm.is_contact_in_group(contact_in_group, group_for_removing_contact), 'Contact still in group!'
