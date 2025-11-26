
from login_page import login_page

class SessionHelper:

    def __init__(self,app):
        self.app = app


    def login(self, username, password):

        login_page().login(self.app.wd, username, password)

    def logout(self):
        self.app.wd.find_element("link text", "Logout").click()

