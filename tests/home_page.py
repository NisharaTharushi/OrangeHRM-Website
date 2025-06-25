import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.home_page import Home

driver = webdriver.Firefox() 
driver.get("https://www.orangehrm.com/")
driver.maximize_window()

home = Home(driver) 

home.title()
home.logo()
home.header()
home.book_demo(
    name_input = "Nishara",
    phone_input = "1234567890",
    email_input = "d2w0J@example.com",
    company_name_input = "OrangeHRM",
    country_input = "Australia",
    no_of_employees_input = "11 - 50")

home.back_to_home()
home.context()
