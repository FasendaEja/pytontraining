from selenium import webdriver
from selenium.webdriver.common.by import By

class   SupportHelper:

    # заполнение текстового поля по имени
    def send_key_by_name(self,wd, name, text):
        wd.find_element(By.NAME, name).click()
        wd.find_element(By.NAME, name).clear()
        wd.find_element(By.NAME, name).send_keys(text)

    # выбор значения из дропдауна
    def select_drop_down(self,wd, name, value):
        wd.find_element(By.NAME, name).click()
        dropdown = wd.find_element(By.NAME, name)
        dropdown.find_element(By.XPATH, f'//select[@name="{name}"]/option[@value="{value}"]').click()

    # Получение названия месяца по его номеру
    def get_month_name(self, month_num):
        months = {
        1: 'January', 2: 'February', 3: 'March',
        4: 'April', 5: 'May', 6: 'June',
        7: 'July', 8: 'August', 9: 'September',
        10: 'October', 11: 'November', 12: 'December'
        }
        return months[month_num]

