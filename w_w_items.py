from selenium.webdriver.common.by import By


class w_w_items:

    def send_key_by_name(salfe,wd, name, text):
        wd.find_element(By.NAME, name).click()
        wd.find_element(By.NAME, name).clear()
        wd.find_element(By.NAME, name).send_keys(text)