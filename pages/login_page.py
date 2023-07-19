import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en/login'
    expected_title = "Scouts panel - sign in"
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    header_of_box = 'Scouts Panel'
    add_a_player_button_xpath = "//div[2]/div/div/a/button/span[1]"
    english_language_listbox_xpath = "//div[2]/div/div"
    polski_option_xpath = "//div[3]/ul/li[1]"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        test_title = self.get_page_title('https://scouts-test.futbolkolektyw.pl/en')

    def check_page_title(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.header_of_box)

    def click_english_language_listbox(self):
        self.click_on_the_element(self.english_language_listbox_xpath)

    def click_polski_language_option(self):
        self.click_on_the_element(self.polski_option_xpath)
