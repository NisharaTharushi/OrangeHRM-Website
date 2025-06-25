from selenium.webdriver.common.by import By
import time

class PeopleManagement():   
        def __init__(self, driver):
         self.driver = driver

        # Locators
        people_management_text = (By.XPATH, "//h2[normalize-space()='People Management']")
        learn_more_button = (By.XPATH, "//a[@href='/en/solutions/people-management/hr-administration']//div[@class='link-text']//h6[contains(text(),'Learn More')]")
        hr_title = (By.XPATH, "//h1[normalize-space()='HR Administration']")
        book_demo = (By.XPATH, "//div[@class='platform-slider-content']//a[normalize-space()='Book a Free Demo']")
        enhanced_security = (By.XPATH, "//h2[normalize-space()='Enhanced Security with MFA']")
        mfa_image = (By.XPATH, "//h2[normalize-space()='Enhanced Security with MFA']")
        audit_text = (By.XPATH, "//h2[normalize-space()='Audit Trail']")
        audit_image = (By.XPATH, "//div[contains(@role,'button')]//img[contains(@alt,'Audit Trail')]")
        asset_text = (By.XPATH, "//h2[normalize-space()='Asset Tracking']")
        asset_image = (By.XPATH, "//div[contains(@role,'button')]//img[contains(@alt,'Asset Tracking')]")
        news_text = (By.XPATH, "//h2[normalize-space()='News & HR Policy Publisher']")
        news_image = (By.XPATH, "//div[contains(@role,'button')]//img[contains(@alt,'News & HR Policy Publisher')]")
        notification_text = (By.XPATH, "//h2[normalize-space()='Notifications']")
        notification_image = (By.XPATH, "//div[contains(@role,'button')]//img[contains(@alt,'Notifications')]")
        custom_roles_text = (By.XPATH, "//h2[normalize-space()='Custom User Roles']")
        custom_roles_image = (By.XPATH, "//div[contains(@role,'button')]//img[contains(@alt,'User Roles')]")


        # people Management Section 
        print("---- People Management Section----")
        def open_people_management_section(self):
            print("people Management Section")
            people = self.driver.find_element(*self.people_management_text)
            print("People Management text: ", people.get_attribute('innerHTML'))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", people)
            time.sleep(3)

        # Learn more button 
        def click_learn_more(self):
            learn_more = self.driver.find_element(*self.learn_more_button)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", learn_more)
            learn_more.click()
            time.sleep(3)
            print("Learn More button clicked to open HR Administration page")
            print("open HR Administration page after clicking People Management learn more button\n")

        # HR administration page 
        def test_hr_administration_page(self):
            print("HR Administration page test")
            hr = self.driver.find_element(*self.hr_title)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", hr)
            print("HR Administration text:", hr.get_attribute('innerHTML'))
            time.sleep(2)

            book = self.driver.find_element(*self.book_demo)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", book)
            print("Book a Free Demo button: ", book.get_attribute('innerHTML'))
            book.click()
            time.sleep(3)
            self.driver.back()

        # Enhanced Security 
        def verify_enhanced_security(self):
            enhanced = self.driver.find_element(*self.enhanced_security)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", enhanced)
            print("Enhanced Security with MFA text: ", enhanced.get_attribute('innerHTML'))
            time.sleep(2)

            mfa = self.driver.find_element(*self.mfa_image)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", mfa)
            print("MFA image: ", mfa.get_attribute('alt'))
            time.sleep(2)
            print("")

        # Audit Trial 
        def verify_audit_trail(self):
            audit = self.driver.find_element(*self.audit_text)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", audit)
            print("Audit Trail text: ", audit.get_attribute('innerHTML'))

            image = self.driver.find_element(*self.audit_image)
            print("Audit Trail image: ", image.get_attribute('alt'))
            time.sleep(2)
            print("")

        # Asset Tracking 
        def verify_asset_tracking(self):
            asset = self.driver.find_element(*self.asset_text)
            print("Asset Tracking text: ", asset.get_attribute('innerHTML'))

            image = self.driver.find_element(*self.asset_image)
            print("Asset Tracking image: ", image.get_attribute('alt'))
            time.sleep(2)
            print("")

        # News and Policy 
        def verify_news_and_policy(self):
            news = self.driver.find_element(*self.news_text)
            print("News & HR Policy Publisher text: ", news.get_attribute('innerHTML'))

            image = self.driver.find_element(*self.news_image)
            print("News & HR Policy Publisher image: ", image.get_attribute('alt'))
            time.sleep(2)
            print("")

        # Notifictaions 
        def verify_notifications(self):
            notif = self.driver.find_element(*self.notification_text)
            print("Notifications text: ", notif.get_attribute('innerHTML'))

            image = self.driver.find_element(*self.notification_image)
            print("Notifications image: ", image.get_attribute('alt'))
            time.sleep(2)
            print("")

        # Customer User Roles
        def verify_custom_user_roles(self):
            custom = self.driver.find_element(*self.custom_roles_text)
            print("Custom User Roles text: ", custom.get_attribute('innerHTML'))

            image = self.driver.find_element(*self.custom_roles_image)
            print("Custom User Roles image: ", image.get_attribute('alt'))
            time.sleep(2)
            print("")
