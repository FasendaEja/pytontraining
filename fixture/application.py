from selenium import webdriver
from login_page import login_page
from w_w_items import w_w_items
from selenium.webdriver.common.by import By


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def destroy(self):
        self.wd.quit()

    def login(self, username, password):
        wd = self.wd
        login_page().login(wd, username,password)

    def create_group(self, group):
        wd=self.wd
        # Нажимаем создать новую группу
        wd.find_element(By.NAME, "new").click()
        # Вводим название группы
        w_w_items().send_key_by_name(wd, "group_name", group.name)
        # вводим хэадер группы
        w_w_items().send_key_by_name(wd, "group_header", group.header)
        # вводим футер группы
        w_w_items().send_key_by_name(wd, "group_footer", group.footer)
        # подтверждаем создание группы
        wd.find_element("name", "submit").click()

    #открытие страницы группы
    def open_groups_page(self):
        self.wd.find_element("link text", "groups").click()


    # открытие домашней страницы
    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    # заполнение текстового поля по имени
    def send_key_by_name1(self,name,text):
        wd = self.wd
        wd.find_element(By.NAME, name).click()
        wd.find_element(By.NAME, name).clear()
        wd.find_element(By.NAME, name).send_keys(text)

    def logout(self):
        self.wd.find_element("link text", "Logout").click()

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
