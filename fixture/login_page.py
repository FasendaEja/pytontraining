from selenium.webdriver.common.by import By
from fixture.support import SupportHelper

class login_page:
    # логин на сайт
    def login(salfe, wd, name, passwd):
        # Вводим логин
        SupportHelper().send_key_by_name(wd, "user", name)
        # Вводим пароль
        SupportHelper().send_key_by_name(wd, "pass", passwd)
        # Нажимаем кнопку войти(залогиниться)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()