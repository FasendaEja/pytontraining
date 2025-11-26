from selenium import webdriver
from selenium.webdriver.common.by import By

class   SupportHelper:

    # заполнение текстового поля по имени
    def send_key_by_name(self,wd, name, text):
        wd.find_element(By.NAME, name).click()
        wd.find_element(By.NAME, name).clear()
        wd.find_element(By.NAME, name).send_keys(text)

