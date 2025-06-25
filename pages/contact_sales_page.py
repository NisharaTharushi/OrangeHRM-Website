from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class ContactSales:   
        def __init__(self, driver):
         self.driver = driver


        # locators 
        CONTACTSALES_BUTTON = (By.XPATH,"//div[@class='d-flex web-menu-btn']//li[2]//a[1]")
        NAME = (By.ID,"Form_getForm_FullName")
        PHONE = (By.ID,"Form_getForm_Contact")
        EMAIL = (By.ID,"Form_getForm_Email")
        COUNTRY = (By.ID,"Form_getForm_Country")
        NO_OF_EMPLOYEES = (By.ID,"Form_getForm_NoOfEmployees")
        JOB_TITLE = (By.ID,"Form_getForm_JobTitle")
        COMMENT = (By.ID,"Form_getForm_Comment")
        RECAPTCHA = (By.XPATH,"//body")
        SUBMIT = (By.ID, "Form_getForm_action_submitForm")
        CONTEXT = (By.XPATH,"//div[@class='contact-page-slider-content']")

     
        print("---- Contact Sales Page ----")
        
        # Contact Sales button
        def contact_sales_button(self):
            ContactSales_button = self.driver.find_element(*ContactSales.CONTACTSALES_BUTTON)
            ContactSales_button.click()
            print("Contact Sales clicked")
            print("Contact Sales page open ")
            time.sleep(10)
            print("")
            
        
        # Contact Sales form
        def contact_sales_form(self,name_input,phone_input,email_input,job_title_input):
            print("---- Contact Sales form ----")
            name = self.driver.find_element(*ContactSales.NAME)
            name.send_keys(name_input)
            print("Name entered", name.get_attribute("value"))
            time.sleep(2)

            phone = self.driver.find_element(*ContactSales.PHONE)
            phone.send_keys(phone_input)
            print("Phone number entered",phone.get_attribute("value"))
            time.sleep(2)

            email = self.driver.find_element(*ContactSales.EMAIL)
            email.send_keys(email_input)
            print("Email entered",email.get_attribute("value"))
            time.sleep(2)

            country = self.driver.find_element(*ContactSales.COUNTRY)
            option_country = Select(country)
            option_country = self.driver.find_element(By.XPATH,"//option[@value='United States']")
            option_country.click()
            print("Country entered",country.get_attribute("value"))
            time.sleep(2)

            no_of_employees = self.driver.find_element(*ContactSales.NO_OF_EMPLOYEES)
            option_country = Select(no_of_employees)
            option_country = self.driver.find_element(By.XPATH,"//option[@value='51 - 200']")
            option_country.click()
            print("No of employees entered",no_of_employees.get_attribute("value"))
            time.sleep(2)


            job_title = self.driver.find_element(*ContactSales.JOB_TITLE)
            job_title.send_keys(job_title_input)
            print("Job title entered",job_title.get_attribute("value"))
            time.sleep(4)

            comment = self.driver.find_element(*ContactSales.COMMENT)
            comment.send_keys("comment")
            print("Comment entered",comment.get_attribute("value"))
            time.sleep(4)

            # Recaptcha = self.driver.find_element(*ContactSales.RECAPTCHA)
            # self.driver.execute_script("arguments[0].click();", Recaptcha)
            # print("I'm not a Robot icon clicked")
            # time.sleep(10)

            Submit = self.driver.find_element(*ContactSales.SUBMIT)
            self.driver.execute_script("arguments[0].click();", Submit)
            print("Submit clicked and open")
            time.sleep(10)
            print("")


        # Context
        def context_p(self):
            context = self.driver.find_element(*ContactSales.CONTEXT)
            for context in context.find_elements(By.TAG_NAME, "p"):
                 print("Context: ",context.get_attribute("innerHTML"))
                 time.sleep(2)       


