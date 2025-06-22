from selenium.webdriver.common.by import By
import time
# select
from selenium.webdriver.support.ui import Select


class Home:   
        def __init__(self, driver):
         self.driver = driver
         
        
        TITLE = (By.XPATH,"//h1[1]")
        LOGO = (By.XPATH,"//a[@class='navbar-brand nav-logo']")
        LANGUAGE = (By.XPATH,"//select[@name='locale']")
        HEADER = (By.ID,"navbarSupportedContent")
        BOOK_DEMO = (By.XPATH,"//div[contains(@class,'d-flex web-menu-btn')]//li[1]//a[1]")
        BOOK_DEMOTITLE = (By.XPATH,"//h1[normalize-space()='Manage Your People and Operations in One Place']")
        NAME = (By.ID,"Form_getForm_FullName")
        PHONE = (By.ID,"Form_getForm_Contact")
        EMAIL = (By.ID,"Form_getForm_Email")
        COMPANY_NAME = (By.ID,"Form_getForm_CompanyName")
        COUNTRY = (By.ID,"Form_getForm_Country")
        NO_OF_EMPLOYEES = (By.ID,"Form_getForm_NoOfEmployees")
        JOB_TITLE = (By.ID,"Form_getForm_JobTitle")
        COMMENT = (By.ID,"Form_getForm_Comment")
        RECAPTCHA = (By.XPATH,"//body")
        SUBMIT = (By.ID, "Form_getForm_action_submitForm")
        
        CONTEXT = (By.XPATH,"//div[@role='main']")
        
        YOU_TUBE_IFRAME = (By.CSS_SELECTOR, "div.homepage-hrforall-video iframe")
        YOUTUBE_PLAY_BUTTON = (By.CSS_SELECTOR, "button.ytp-large-play-button")


        # Page title
        print("---- Home Page ----")
        def title(self):
            title = self.driver.find_element(*Home.TITLE)
            print("Title of the page is",title.text)
            time.sleep(2)
            print("")


        def logo(self):
            logo = self.driver.find_element(By.XPATH,"//a[@class='navbar-brand nav-logo']")
            print("logo href value is ",logo.get_attribute("href"))
            print("Logo clicked and open",logo.get_attribute('href'))
            time.sleep(2)
            print("")


        def language(self):
            language = self.driver.find_element(*Home.LANGUAGE)
            language.click()
            print("Language dropdown clicked")
            time.sleep(2)

            option = Select(language)
            option = self.driver.find_element(By.XPATH,"//option[@value='/en']")
            option.click()
            print("Language clicked and open")
            time.sleep(2)
            print("")
            
        
        def header(self):
            header = self.driver.find_element(*Home.HEADER)
            print("Header opened")
            time.sleep(2)
            for link in header.find_elements(By.TAG_NAME, "li"):
                print(link.text)
            print("")


        def book_demo(self,name_input,phone_input,email_input,company_name_input,country_input,no_of_employees_input):    
            book_demo = self.driver.find_element(*Home.BOOK_DEMO)
            book_demo.click()
            print("Book a Demo clicked")
            print("Book a Demo page open ")
            time.sleep(2)
            print("")

            book_demo_title = self.driver.find_element(*Home.BOOK_DEMOTITLE)
            print("Book a Demo title: ",book_demo_title.get_attribute('innerHTML'))
            time.sleep(2)
            print("")
            
            name = self.driver.find_element(*Home.NAME)
            name.send_keys(name_input)
            print("Name entered", name.get_attribute("value"))
            time.sleep(2)
            print("")

            phone = self.driver.find_element(*Home.PHONE)
            phone.send_keys(phone_input)
            print("Phone number entered",phone.get_attribute("value"))
            time.sleep(2)
            print("")

            email = self.driver.find_element(*Home.EMAIL)
            email.send_keys(email_input)
            print("Email entered",email.get_attribute("value"))
            time.sleep(2)
            print("")

            company_name = self.driver.find_element(*Home.COMPANY_NAME)
            company_name.send_keys(company_name_input)
            print("Company name entered",company_name.get_attribute("value"))
            time.sleep(2)
            print("")

            country = self.driver.find_element(*Home.COUNTRY)
            country.send_keys(country_input)
            print("Country entered",country.get_attribute("value"))
            time.sleep(2)
            print("")

            no_of_employees = self.driver.find_element(*Home.NO_OF_EMPLOYEES)
            no_of_employees.send_keys(no_of_employees_input)
            print("No of employees entered",no_of_employees.get_attribute("value"))
            time.sleep(2)
            print("")

            recaptcha = self.driver.find_element(*Home.RECAPTCHA)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", recaptcha)
            print("I'm not a Robot icon found ")
            self.driver.execute_script("arguments[0].click();", recaptcha)
            print("I'm not a Robot icon clicked")
            time.sleep(7)
            print("")

            submit = self.driver.find_element(*Home.SUBMIT)
            self.driver.execute_script("arguments[0].click();", submit)
            submit.click()
            print("Submit clicked and open")
            time.sleep(10)
            print("")


        def back_to_home(self):
            self.driver.get("https://www.orangehrm.com/")
            print("Back to home page")
            time.sleep(2)
            print("")


        def context(self):
            print("Context")
            context = self.driver.find_element(*Home.CONTEXT)
            context_tags = context.find_elements(By.TAG_NAME, "p")
            for context_tag in context_tags:
                print(context_tag.text)
                print(context_tag.get_attribute("innerHTML"))
            time.sleep(2)
            print("")


