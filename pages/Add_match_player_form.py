from pages.base_page import BasePage


class Dashboard(BasePage):
my_team_label_xpath = "//input[@name='myTeam']/preceding::label"
enemy_team_score_textfield_xpath = "//input[@name='enemyTeamScore']"
reports_button_xpath = "//*[text()="Reports"]"
time_played_label_xpath = "//*[text()="Time played"]"
date_textfield_xpath = "//input[@name='date']"
league_textfield_xpath = "//input[@name='league']"
web_match_textfield_xpath = "//input[@name='webMatch']"
my_team_score_textfield_xpath = "//input[@name='myTeamScore']"
submit_button_xpath = "//*[text()="Submit"]"
clear_button_xpath = "//*[text()="Clear"]"

pass
