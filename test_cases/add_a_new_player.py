import os
import unittest
import time

from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.add_a_player import AddAPlayer


class TestAddAPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player_to_database(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_add_a_player_button()
        add_a_player = AddAPlayer(self.driver)
        time.sleep(5)
        add_a_player.get_page_title(add_a_player.add_a_player_url)
        time.sleep(5)
        add_a_player.type_in_name('Joanna')
        add_a_player.type_in_surname('Borowska')
        add_a_player.type_in_age('19.05.1999')
        add_a_player.type_in_main_position('attack')
        add_a_player.click_submit_button()

    @classmethod
    def tearDown(self):
        self.driver.quit()
