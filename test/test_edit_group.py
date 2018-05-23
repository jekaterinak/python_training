from model.group import Group
import random


def test_edit_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="grnew", header="res", footer="tes"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = "newname1"
    app.group.edit_group(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    for index, group_item in enumerate(old_groups):
        if group_item.id == group.id:
            old_groups[index] = group
            break
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_edit_first_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="grnew", header="res", footer="tes"))
#    app.group.edit_first_group(Group(header="newheader1"))
