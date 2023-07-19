import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class Dashboard(BasePage):
    futbol_kolektyw_button_xpath = "//*[@title ='Logo Scouts Panel']"
    Add_player_xpath = "//*[text()='Add player']"
    expected_dashboard_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    add_player_expected_title = "Add player"
    add_a_player_button_xpath = "//div[2]/div/div/a/button/span[1]"
    main_page_button_xpath = "//ul[1]/div[1]/div[2]/span"
    players_button_xpath = "//ul[1]/div[2]"
    sign_out_button_xpath = "//ul[2]/div[2]/div[2]/span"
    last_created_player_button_xpath = "//div[3]/div/div/a[1]/button/span[1]"
    expected_last_created_player = "Adam Kowalski"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.main_page_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_dashboard_title

    def click_add_a_player_button(self):
        self.click_on_the_element(self.add_a_player_button_xpath)

    def click_players_button(self):
        self.click_on_the_element(self.players_button_xpath)

    def click_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def check_last_created_player(self):
        self.assert_element_text(self.driver, self.last_created_player_button_xpath, self.expected_last_created_player)

    def add_player_page(self):
        self.click_on_the_element(self.Add_player_xpath)
        time.sleep(5)
        actual_title = self.get_page_title(self.add_player_url)
        print("Actual Title:", actual_title)
        print("Expected Title:", self.add_player_expected_title)
        assert actual_title == self.add_player_expected_title
