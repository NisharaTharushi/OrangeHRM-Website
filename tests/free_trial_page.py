import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.free_trial_page import FreeTrial

driver = webdriver.Firefox() 
driver.get("https://www.orangehrm.com/")
driver.maximize_window()

home = FreeTrial(driver) 

home.free_trial_button()
home.request_button()
home.free_trial_page()
home.free_trial_form(
    user_name_input = "Nishara",
    full_name_input = "Tharushi",
    email_input = "nishara@gmail.com",
    phone_input = "0702242491",
    country_input="Australia"
)
