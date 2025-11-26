from selenium.webdriver.common.by import By
from fixture.support import SupportHelper

class ContactHelper:
    def __init__(self, app):
        self.app = app

    # Нажатие на кнопку создать контракт
    def open_new_contact_page(self):
        self.app.wd.find_element("link text", "add new").click()

    # создание контракта
    def create_contact(self, contact):
        SupportHelper().send_key_by_name(self.app.wd, "firstname", contact.firstname)
        SupportHelper().send_key_by_name(self.app.wd, "middlename", contact.middlename)
        SupportHelper().send_key_by_name(self.app.wd, "lastname", contact.lastname)
        SupportHelper().send_key_by_name(self.app.wd, "nickname", contact.nickname)
        SupportHelper().send_key_by_name(self.app.wd, "title", contact.title)
        SupportHelper().send_key_by_name(self.app.wd, "company", contact.company)
        SupportHelper().send_key_by_name(self.app.wd, "address", contact.address)
        SupportHelper().send_key_by_name(self.app.wd, "home", contact.home)
        SupportHelper().send_key_by_name(self.app.wd, "mobile", contact.mobile)
        SupportHelper().send_key_by_name(self.app.wd, "work", contact.work)
        SupportHelper().send_key_by_name(self.app.wd, "fax", contact.fax)
        SupportHelper().send_key_by_name(self.app.wd, "email", contact.email)
        SupportHelper().send_key_by_name(self.app.wd, "email2", contact.email2)
        SupportHelper().send_key_by_name(self.app.wd, "email3", contact.email3)
        SupportHelper().send_key_by_name(self.app.wd, "homepage", contact.homepage)
        SupportHelper().select_drop_down(self.app.wd, "bday", str(contact.bday.day))
        SupportHelper().select_drop_down(self.app.wd, "bmonth", SupportHelper().get_month_name(contact.bday.month))
        SupportHelper().send_key_by_name(self.app.wd, "byear", str(contact.bday.year))
        SupportHelper().select_drop_down(self.app.wd, "aday", str(contact.ayear.day))
        SupportHelper().select_drop_down(self.app.wd, "amonth", SupportHelper().get_month_name(contact.ayear.month))
        SupportHelper().send_key_by_name(self.app.wd, "ayear", str(contact.ayear.year))
        self.app.wd.find_element(By.CSS_SELECTOR, "input:nth-child(75)").click()