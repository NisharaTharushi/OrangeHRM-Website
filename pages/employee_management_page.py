from selenium.webdriver.common.by import By


class EmployeeManagementPage:
    def __init__(self, driver):
        self.driver = driver

    
    print("---- Employee Management Page ----")
    # Employee Management Page 
    EMPLOYEE_MANAGEMENT_TITLE = (By.XPATH, "//h1[normalize-space()='Employee Management']")    
    EMPLOYEE_MANAGEMENT_DESCRIPTION = (By.XPATH, "//p[@class='platform-page-description text-center']")
    LEARN_MORE_BUTTON = (By.XPATH, "//a[@href='/en/solutions/people-management/employee-management']//div[@class='link-text']//p[contains(text(),'Learn More')]")
    DEMO_BUTTON_TOP = (By.XPATH, "//div[@class='platform-slider-content']//a[normalize-space()='Book a Free Demo']")
    DEMO_BUTTON_BOTTOM = (By.XPATH, "//div[@class='platform-main-description']//a[normalize-space()='Book a Free Demo']")
    DASHBOARD_TEXT = (By.XPATH, "//h2[normalize-space()='Dashboard']")
    DASHBOARD_IMAGE = (By.XPATH, "//div[contains(@role,'button')]//img[contains(@alt,'Dashboard')]")
    EMPLOYEE_DATABASE_TEXT = (By.XPATH, "//h2[normalize-space()='Employee Database & Profiles']")
    EMPLOYEE_DATABASE_IMAGE = (By.XPATH, "//div[contains(@role,'button')]//img[contains(@alt,'Employee Databse and Profile')]")
    STAFF_SCHEDULE_TEXT = (By.XPATH, "//h2[normalize-space()='Streamline Staff Scheduling with Work Schedules']")
    STAFF_SCHEDULE_IMAGE = (By.XPATH, "//div[contains(@role,'button')]//img[contains(@alt,'Streamline Staff Scheduling with Work Schedules')]")
    DISCIPLINARY_TEXT = (By.XPATH, "//h2[normalize-space()='Disciplinary Tracking']")
    DISCIPLINARY_IMAGE = (By.XPATH, "//div[contains(@role,'button')]//img[contains(@alt,'Disciplinary Tracking')]")
    ORG_CHART_TEXT = (By.XPATH, "//h2[normalize-space()='Organization Chart']")
    ORG_CHART_IMAGE = (By.XPATH, "//div[contains(@role,'button')]//img[contains(@alt,'Org Chart')]")
    CORPORATE_DIRECTORY_TEXT = (By.XPATH, "//h2[normalize-space()='Corporate Directory']")
    CORPORATE_DIRECTORY_IMAGE = (By.XPATH, "//div[contains(@role,'button')]//img[contains(@alt,'Corporate Directory')]")


    def employee_management_title(self):
        self.driver.find_element(*self.EMPLOYEE_MANAGEMENT_TITLE)
        print("Employee Management title: ",self.driver.find_element(*self.EMPLOYEE_MANAGEMENT_TITLE).text)
        print("")

    def employee_management_description(self):
        self.driver.find_element(*self.EMPLOYEE_MANAGEMENT_DESCRIPTION)
        print("Employee Management description: ",self.driver.find_element(*self.EMPLOYEE_MANAGEMENT_DESCRIPTION).text)
        print("")


    def demo_button_top(self):
        self.driver.find_element(*self.DEMO_BUTTON_TOP)
        print("Demo button top: ",self.driver.find_element(*self.DEMO_BUTTON_TOP).text)

    def demo_button_bottom(self):
        self.driver.find_element(*self.DEMO_BUTTON_BOTTOM)
        print("Demo button bottom: ",self.driver.find_element(*self.DEMO_BUTTON_BOTTOM).text)
        self.driver.get("https://www.orangehrm.com/en/solutions/people-management/employee-management")
        print("")

    def dashboard_text(self):
        self.driver.find_element(*self.DASHBOARD_TEXT)
        print("Dashboard text: ",self.driver.find_element(*self.DASHBOARD_TEXT).text)

    def dashboard_image(self):
        self.driver.find_element(*self.DASHBOARD_IMAGE)
        print("Dashboard image: ",self.driver.find_element(*self.DASHBOARD_IMAGE).is_displayed())
        print("")

    def employee_database_text(self):
        self.driver.find_element(*self.EMPLOYEE_DATABASE_TEXT)
        print("Employee Database text: ",self.driver.find_element(*self.EMPLOYEE_DATABASE_TEXT).text)

    def employee_database_image(self):
        self.driver.find_element(*self.EMPLOYEE_DATABASE_IMAGE)
        print("Employee Database image: ",self.driver.find_element(*self.EMPLOYEE_DATABASE_IMAGE).is_displayed())
        print("")

    def staff_schedule_text(self):
        self.driver.find_element(*self.STAFF_SCHEDULE_TEXT)
        print("Staff Schedule text: ",self.driver.find_element(*self.STAFF_SCHEDULE_TEXT).text)

    def staff_schedule_image(self):
        self.driver.find_element(*self.STAFF_SCHEDULE_IMAGE)
        print("Staff Schedule image: ",self.driver.find_element(*self.STAFF_SCHEDULE_IMAGE).is_displayed())
        print("")

    def disciplinary_text(self):
        self.driver.find_element(*self.DISCIPLINARY_TEXT)
        print("Disciplinary text: ",self.driver.find_element(*self.DISCIPLINARY_TEXT).text)

    def disciplinary_image(self):
        self.driver.find_element(*self.DISCIPLINARY_IMAGE)        
        print("Disciplinary image: ",self.driver.find_element(*self.DISCIPLINARY_IMAGE).is_displayed())
        print("")

    def org_chart_text(self):
        self.driver.find_element(*self.ORG_CHART_TEXT)
        print("Org Chart text: ",self.driver.find_element(*self.ORG_CHART_TEXT).text)

    def org_chart_image(self):              
        self.driver.find_element(*self.ORG_CHART_IMAGE)
        print("Org Chart image: ",self.driver.find_element(*self.ORG_CHART_IMAGE).is_displayed())
        print("")

    def corporate_directory_text(self):
        self.driver.find_element(*self.CORPORATE_DIRECTORY_TEXT)
        print("Corporate Directory text: ",self.driver.find_element(*self.CORPORATE_DIRECTORY_TEXT).text)

    def corporate_directory_image(self):
        self.driver.find_element(*self.CORPORATE_DIRECTORY_IMAGE)
        print("Corporate Directory image: ",self.driver.find_element(*self.CORPORATE_DIRECTORY_IMAGE).is_displayed())
        print("")
    









