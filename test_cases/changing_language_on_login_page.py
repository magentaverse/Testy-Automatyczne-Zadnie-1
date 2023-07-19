import os
import unittest

from selenium import webdriver

from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestChangeLanguage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_changing_language_before_login_in(self):
        user_login = LoginPage(self.driver)

        user_login.click_english_language_listbox()
        user_login.click_polski_language_option()


    @classmethod
    def tearDown(self):
        self.driver.quit()
