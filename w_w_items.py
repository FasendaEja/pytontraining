from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import group
from group import Group

class w_w_items:

    def send_key_by_name(salfe,wd, name, text):
        wd.find_element(By.NAME, name).click()
        wd.find_element(By.NAME, name).clear()
        wd.find_element(By.NAME, name).send_keys(text)