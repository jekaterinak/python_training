from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="grnew", header="res", footer="tes"))
    app.group.edit_first_group(Group(name="newname1"))


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="grnew", header="res", footer="tes"))
    app.group.edit_first_group(Group(header="newheader1"))
