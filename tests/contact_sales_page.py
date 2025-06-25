import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.contact_sales_page import ContactSales

driver = webdriver.Chrome() 
driver.get("https://www.orangehrm.com/")
driver.maximize_window()

home = ContactSales(driver) 

home.contact_sales_button()
home.contact_sales_form(
    name_input = "Nishara",
    phone_input = "1234567890",
    email_input = "nishara@gmail.com",
    job_title_input = "QA Engineer" 
)
home.context_p()
