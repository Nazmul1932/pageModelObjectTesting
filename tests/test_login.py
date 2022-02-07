from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from pages.homePage import HomePage
from pages.loginPage import LoginPage
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.setUserName("Admin")
        login.setPassword("admin123")
        login.clickLogin()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

    def test_login_invalid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.setUserName("Admin1")
        login.setPassword("admin12356")
        login.clickLogin()
        message = driver.find_element_by_xpath("Invalid credentials123").text
        self.assertEqual(message, "")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == "__main__":
    unittest.main()
