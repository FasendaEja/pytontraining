
from fixture.application import Application
from model.group import Group
from model.contact import Contact
from datetime import date
import pytest

@pytest.fixture
def app(request):
    fix=Application()
    request.addfinalizer(fix.destroy)
    return fix


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

 #добавление контракта
def test_addcontact(app):

    # открываем домашнюю страницу
    app.open_home_page()
    # Логинимся
    app.session.login("admin", "secret")
    app.contract.open_new_contact_page()
    app.contract.create_contact(Contact("fname", "mname",
                                        "lname", "nick",
                                        "title", "comp",
                                        "addrrress", "11111111",
                                        "22222222", "33333333",
                                        "44444444", "q@q.com",
                                        "", "",
                                        "hp", date(1990, 10, 11),
                                        date(2025, 11, 17)))

    # выходим из уз
    app.session.logout()
