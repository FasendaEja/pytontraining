
from model.contact import Contact
from datetime import date

from conftest import *
 #добавление контракта
def test_addcontact(app):



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





def test_Edit_contact(app):

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



def test_delete_first_contact(app):

    app.contract.open_contacts_page()
    app.contract.delete_first_contact()


