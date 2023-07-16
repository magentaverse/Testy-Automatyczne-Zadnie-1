import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    Add_player_xpath = "//*[text()='Add player']"
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    add_player_expected_title= "Add player"

    def title_of_page(self):
        time.sleep(5)
        actual_title = self.get_page_title(self.dashboard_url)
        print("Actual Title:", actual_title)
        print("Expected Title:", self.expected_title)
        assert actual_title == self.expected_title

    def add_player_page(self):
        self.click_on_the_element(self.Add_player_xpath)
        time.sleep(5)
        actual_title = self.get_page_title(self.add_player_url)
        print("Actual Title:", actual_title)
        print("Expected Title:", self.add_player_expected_title)
        assert actual_title == self.add_player_expected_title