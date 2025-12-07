from model.group import Group
from conftest import *
from fixture.application import Application



#Добавление группы
def test_addgrup(app):

    # открываем домашнюю страницу
    app.open_home_page()
    #Логинимся
    app.session.login("admin", "secret")
    #переходим на вкладку группы
    app.group.open_groups_page()
    #Создаем новую группу
    app.group.create_group(Group( "grup1", "grup1", "grup1"))
    # переходим на вкладку группы
    app.group.open_groups_page()
    app.session.logout()


# тест создание пустой группы
def test_add_empt_grup(app):

    # открываем домашнюю страницу
    app.open_home_page()
    #Логинимся
    app.session.login("admin", "secret")
    #переходим на вкладку группы
    app.group.open_groups_page()
    #Создаем новую группу
    app.group.create_group(Group("", "", ""))
    # переходим на вкладку группы
    app.group.open_groups_page()
    #выходим из уз
    app.session.logout()

def test_edit_grup(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.open_groups_page()
    app.group.edit_group(Group("new_grup_name", "new_grup_header", "new_grup_footer"))
    app.session.logout()

def test_delete_first_group(app):
    # открываем домашнюю страницу
    app.open_home_page()
    # Логинимся
    app.session.login("admin", "secret")
    app.group.delete_first_group()
    # выходим из уз
    app.session.logout()