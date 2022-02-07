from locator.locators import Locators

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id
        self.invalid_login_msg_xpath = "//span[@id='spanMessage']"
        
    def setUserName(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)
        
    def setPassword(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
        
    def clickLogin(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def check_invalid_login_details(self):
        msg = self.driver.find_element_by_xpath(self.invalid_login_msg_xpath).text
        return msg