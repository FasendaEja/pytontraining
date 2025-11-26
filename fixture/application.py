from selenium import webdriver

from fixture.group import GroupHelper
from fixture.session import SessionHelper


from selenium.webdriver.common.by import By
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def destroy(self):
        self.wd.quit()


    # открытие домашней страницы
    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    # Нажатие на кнопку создать контракт
    def open_new_contact_page(self):
        self.wd.find_element("link text", "add new").click()

    #создание контракта
    def create_contact(self, contact):
        w_w_items().send_key_by_name(self.wd, "firstname", contact.firstname)
        w_w_items().send_key_by_name(self.wd, "middlename", contact.middlename)
        w_w_items().send_key_by_name(self.wd, "lastname", contact.lastname)
        w_w_items().send_key_by_name(self.wd, "nickname", contact.nickname)
        w_w_items().send_key_by_name(self.wd, "title", contact.title)
        w_w_items().send_key_by_name(self.wd, "company", contact.company)
        w_w_items().send_key_by_name(self.wd, "address", contact.address)
        w_w_items().send_key_by_name(self.wd, "home", contact.home)
        w_w_items().send_key_by_name(self.wd, "mobile", contact.mobile)
        w_w_items().send_key_by_name(self.wd, "work", contact.work)
        w_w_items().send_key_by_name(self.wd, "fax", contact.fax)
        w_w_items().send_key_by_name(self.wd, "email", contact.email)
        w_w_items().send_key_by_name(self.wd, "email2", contact.email2)
        w_w_items().send_key_by_name(self.wd, "email3", contact.email3)
        w_w_items().send_key_by_name(self.wd, "homepage", contact.homepage)
        self.select_drop_down("bday", str(contact.bday.day))
        self.select_drop_down("bmonth", self.get_month_name(contact.bday.month))
        w_w_items().send_key_by_name(self.wd, "byear", str(contact.bday.year))
        self.select_drop_down("aday", str(contact.ayear.day))
        self.select_drop_down("amonth", self.get_month_name(contact.ayear.month))
        w_w_items().send_key_by_name(self.wd, "ayear", str(contact.ayear.year))
        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(75)").click()

    #выбор значения из дропдауна
    def select_drop_down(self, name, value):
        self.wd.find_element(By.NAME, name).click()
        dropdown = self.wd.find_element(By.NAME, name)
        dropdown.find_element(By.XPATH, f'//select[@name="{name}"]/option[@value="{value}"]').click()

    #Получение названия месяца по его номеру
    def get_month_name(self, month_num):
        months = {
            1: 'January', 2: 'February', 3: 'March',
            4: 'April', 5: 'May', 6: 'June',
            7: 'July', 8: 'August', 9: 'September',
            10: 'October', 11: 'November', 12: 'December'
        }
        return months[month_num]
