from model.group import Group
from conftest import *
from fixture.application import Application



#Добавление группы
def test_addgrup(app):

    #переходим на вкладку группы
    app.group.open_groups_page()
    #Создаем новую группу
    app.group.create_group(Group( "grup1", "grup1", "grup1"))
    # переходим на вкладку группы
    app.group.open_groups_page()



# тест создание пустой группы
def test_add_empt_grup(app):


    #переходим на вкладку группы
    app.group.open_groups_page()
    #Создаем новую группу
    app.group.create_group(Group("", "", ""))
    # переходим на вкладку группы
    app.group.open_groups_page()


def test_edit_grup(app):

    app.group.open_groups_page()
    app.group.edit_first_group(Group("new_grup_name", "new_grup_header", "new_grup_footer"))


def test_edit_grup_name(app):

    app.group.open_groups_page()
    app.group.edit_first_group(Group(name="new_grup_name"))


def test_delete_first_group(app):

    app.group.delete_first_group()
