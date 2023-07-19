import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class AddAPlayer(BasePage):
    page_title_xpath = "//header//h6"
    email_field_xpath = "//input[@name='email']"
    name_field_xpath = "//input[@name='name']"
    surname_field_xpath = "//input[@name='surname']"
    phone_field_xpath = "//input[@name='phone']"
    weight_field_xpath = "//input[@name='weight']"
    height_field_xpath = "//input[@name='height']"
    age_field_xpath = "//input[@name='age']"
    leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_option_xpath = "//div[3]/ul/li[1]"
    left_leg_option_xpath = "//div[3]/ul/li[2]"
    club_field_xpath = "//input[@name='club']"
    level_field_xpath = "//input[@name='level']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    second_position_field_xpath = "//input[@name='secondPosition']"
    district_field_xpath = "//*[contains(@id,'select-district')]"
    district_xpath_map = {
        "Lower Silesia": "//li[1]",
        "Kuyavia-Pomerania": "//li[2]",
        "Lublin": "//li[3]",
        "Lubusz": "//li[4]",
        "Łódź": "//li[5]",
        "Lesser Poland": "//li[6]",
        "Masovia": "//li[7]",
        "Opole": "//li[8]",
        "Subcarpathia": "//li[9]",
        "Podlaskie": "//li[10]",
        "Pomerania": "//li[11]",
        "Silesia": "//li[12]",
        "Holy Cross Province": "//li[13]",
        "Warmia-Masuria": "//li[14]",
        "Greater Poland": "//li[15]",
        "West Pomerania": "//li[16]"

    }
    achievements_field_xpath = "//input[@name='achievements']"
    add_lang_button_xpath = "//button[@aria-label='Add language']"
    facebook_field_xpath = "//input[@name='webFB']"
    add_youtube_button_xpath = "//button[@aria-label='Add link to Youtube']"
    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//button[@type='submit']//following-sibling::button"
    progress_bar_toaster_xpath = "//*[@role='alert']"
    add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = 'Add player'
    name = ""
    surname = ""
    expected_title_player_added = " "

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def test_add_a_player_to_database(self):
        add_a_player = AddAPlayer(self.driver)
        add_a_player.get_page_title(add_a_player.add_a_player_url)
        time.sleep(5)
        add_a_player.title_of_page()

    def title_of_page(self):
        test_title = self.get_page_title(self.add_a_player_url)
        print("test_title:", test_title)
        print("expected_title:", self.expected_title)
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        assert test_title == self.expected_title

    def player_added_title_of_the_page(self):
        self.wait_for_element_to_be_visible(self.progress_bar_toaster_xpath)
        player_title = self.driver.title
        self.expected_title_player_added = f"Edit player {self.name} {self.surname}"
        assert player_title == self.expected_title_player_added
