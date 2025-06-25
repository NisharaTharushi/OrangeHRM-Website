import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.people_management_page import PeopleManagement

driver = webdriver.Firefox() 
driver.get("https://www.orangehrm.com/")
driver.maximize_window()

page = PeopleManagement(driver)

page.open_people_management_section()
page.click_learn_more()
page.test_hr_administration_page()
page.verify_enhanced_security()
page.verify_audit_trail()
page.verify_asset_tracking()
page.verify_news_and_policy()
page.verify_notifications()
page.verify_custom_user_roles()
