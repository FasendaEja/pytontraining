
from model.contact import Contact
from datetime import date

from conftest import *
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


def test_Edit_contact(app):
    # открываем домашнюю страницу
    app.open_home_page()
    # Логинимся
    app.session.login("admin", "secret")
    app.contract.open_contacts_page()
    app.contract.edit_contact(Contact("new_fname", "new_mname",
                                        "new_lname", "new_nick",
                                        "new_title", "new_comp",
                                        "addrrress", "11111111",
                                        "22222222", "33333333",
                                        "44444444", "q@q.com",
                                        "", "",
                                        "hp", date(1990, 10, 11),
                                        date(2025, 11, 17)))
    # выходим из уз
    app.session.logout()


def test_delete_first_contact(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.contract.open_contacts_page()
    app.contract.delete_first_contact()
    # выходим из уз
    app.session.logout()

