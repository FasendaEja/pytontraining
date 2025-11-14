# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import group
from group import Group


class Testaddgrup(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_addgrup(self):
        wd = self.wd
        # открываем домашнюю страницу
        self.open_home_page(wd)
        #Логинимся
        self.login(wd,"admin","secret")
        #переходим на вкладку группы
        self.open_groups_page(wd)
        #Создаем новую группу
        self.create_group(wd,Group( "grup1", "grup1", "grup1"))
        # переходим на вкладку группы
        self.open_groups_page(wd)
        #выходим из уз
        wd.find_element("link text", "Logout").click()

    def test_add_empt_grup(self):
        wd = self.wd
        # открываем домашнюю страницу
        self.open_home_page(wd)
        #Логинимся
        self.login(wd,"admin","secret")
        #переходим на вкладку группы
        self.open_groups_page(wd)
        #Создаем новую группу
        self.create_group(wd, Group("", "", ""))
        # переходим на вкладку группы
        self.open_groups_page(wd)
        #выходим из уз
        wd.find_element("link text", "Logout").click()

    def create_group(self, wd, group):
        # Нажимаем создать новую группу
        wd.find_element(By.NAME, "new").click()
        # Вводим название группы
        self.send_key_by_name(wd, "group_name", group.name)
        # вводим хэадер группы
        self.send_key_by_name(wd, "group_header", group.header)
        # вводим футер группы
        self.send_key_by_name(wd, "group_footer", group.footer)
        # подтверждаем создание группы
        wd.find_element("name", "submit").click()

    def open_groups_page(self, wd):
        wd.find_element("link text", "groups").click()

    def login(self, wd,name,passwd):
        # Вводим логин
        self.send_key_by_name(wd, "user", name)
        # Вводим пароль
        self.send_key_by_name(wd, "pass", passwd)
        # Нажимаем кнопку войти(залогиниться)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, wd):

        wd.get("http://localhost/addressbook/")

    def send_key_by_name(self,wd,name,text):
        wd = self.wd
        wd.find_element(By.NAME, name).click()
        wd.find_element(By.NAME, name).clear()
        wd.find_element(By.NAME, name).send_keys(text)

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
