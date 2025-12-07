from selenium.webdriver.common.by import By

from fixture.support import SupportHelper


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create_group(self, group):
        wd = self.app.wd
        # Нажимаем создать новую группу
        wd.find_element(By.NAME, "new").click()
        # Вводим название группы
        SupportHelper().send_key_by_name(wd, "group_name", group.name)
        # вводим хэадер группы
        SupportHelper().send_key_by_name(wd, "group_header", group.header)
        # вводим футер группы
        SupportHelper().send_key_by_name(wd, "group_footer", group.footer)
        # подтверждаем создание группы
        wd.find_element("name", "submit").click()

        # открытие страницы группы

    def open_groups_page(self):
        self.app.wd.find_element("link text", "groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        #выбрать первую группу
        wd.find_element("name", "selected[]").click()
        #удалить выбранную группу
        wd.find_element("name", "delete").click()
        self.open_groups_page()

    def edit_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # выбрать первую группу
        wd.find_element("name", "selected[]").click()
        wd.find_element("name", "edit").click()
        # Вводим название группы
        SupportHelper().send_key_by_name(wd, "group_name", group.name)
        # вводим хэадер группы
        SupportHelper().send_key_by_name(wd, "group_header", group.header)
        # вводим футер группы
        SupportHelper().send_key_by_name(wd, "group_footer", group.footer)
        # подтверждаем создание группы
        wd.find_element("name", "update").click()


