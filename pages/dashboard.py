from pages.base_page import BasePage


class Dashboard(BasePage):

main_page_button_xpath = "//*[text()="Main page"]"
players_button_xpath = "//*[text()="Players"]"
language_button_xpath = "//*[text()="Polski"]"
sign_out_button_xpath = "//*[text()="Sign out"]"
players_count_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div[1]/div/div[1]"
matches_count_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div[2]/div/div[1]"
reports_count_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div[3]/div/div[1]"
events_count_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div[4]/div/div[1]"
add_player_hyperlink_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
dev_team_contact_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"

pass
