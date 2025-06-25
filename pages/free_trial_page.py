from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

class FreeTrial:   
        def __init__(self, driver):
         self.driver = driver

        
        # locators
        FREE_TRIAL_BUTTON = (By.ID,"Form_submitForm_EmailHomePage")
        REQUEST_BUTTON = (By.ID,"Form_submitForm_action_request")
        TITLE = (By.XPATH,"//h1[contains(text(),'Revolutionize Your Human Resource Management Experience')]")
        USER_NAME = (By.ID,"Form_getForm_subdomain")
        FULL_NAME = (By.ID,"Form_getForm_Name")
        EMAIL = (By.ID,"Form_getForm_Email")
        PHONE = (By.ID,"Form_getForm_Contact")
        COUNTRY = (By.ID,"Form_getForm_Country")
        SUBMIT = (By.ID,"Form_getForm_action_submitForm")
        

        print("---- Free trial page ----")
        
        # Free trial button 
        def free_trial_button(self):
                driver = self.driver
                driver.find_element(*self.FREE_TRIAL_BUTTON).click()
                print("Free trial button clicked")
                time.sleep(2)
                print("")


        # request button 
        def request_button(self):
                driver = self.driver
                driver.find_element(*self.REQUEST_BUTTON).click()
                print("Request button clicked")
                time.sleep(2)


        # free trial page 
        def free_trial_page(self):
                driver = self.driver
                title = driver.find_element(*self.TITLE)
                title_text = title.text
                print("Free trial page open")
                print("Free trial page title: ",title_text)
                time.sleep(2)
                print("")


        # free trial form
        def free_trial_form(self,user_name_input,full_name_input,email_input,phone_input,country_input):
                print("---- Free trial form ----")
                name = self.driver.find_element(*self.USER_NAME)
                name.send_keys(user_name_input)
                print("Enter user name: ",name.get_attribute("value"))
                time.sleep(2)

                full_name = self.driver.find_element(*self.FULL_NAME)
                full_name.send_keys(full_name_input)
                print("Enter full name: ",full_name.get_attribute("value"))
                time.sleep(2)

                email = self.driver.find_element(*self.EMAIL)
                email.send_keys(email_input)
                print("Enter email: ",email.get_attribute("value"))
                time.sleep(2)

                phone = self.driver.find_element(*self.PHONE)
                phone.send_keys(phone_input)
                print("Enter phone number: ",phone.get_attribute("value"))
                time.sleep(2)

                country = self.driver.find_element(*self.COUNTRY)
                option_country = Select(country)
                option_country.select_by_visible_text(country_input)
                print("Country entered",country.get_attribute("value"))
                time.sleep(2)

                submit = self.driver.find_element(*self.SUBMIT)
                submit.click()
                print("Submit clicked and open")
                time.sleep(2)
                print("")

                
