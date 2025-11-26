from selenium.webdriver.common.by import By
from w_w_items import w_w_items

class login_page:
    # логин на сайт
    def login(salfe, wd, name, passwd):
        # Вводим логин
        w_w_items().send_key_by_name(wd, "user", name)
        # Вводим пароль
        w_w_items().send_key_by_name(wd, "pass", passwd)
        # Нажимаем кнопку войти(залогиниться)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()