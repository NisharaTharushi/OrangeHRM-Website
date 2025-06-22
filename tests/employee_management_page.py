import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.employee_management_page import EmployeeManagementPage

driver = webdriver.Firefox() 
driver.get("https://www.orangehrm.com/en/solutions/people-management/employee-management")
driver.maximize_window()

page = EmployeeManagementPage(driver)

page.employee_management_title()
page.employee_management_description()
page.demo_button_top()
page.demo_button_bottom()
page.dashboard_text()
page.dashboard_image()
page.employee_database_text()
page.employee_database_image()
page.staff_schedule_text()
page.staff_schedule_image()
page.disciplinary_text()
page.disciplinary_image()
page.org_chart_text()
page.org_chart_image()
page.corporate_directory_text()
page.corporate_directory_image()






