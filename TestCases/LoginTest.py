import unittest
import HtmlTestRunner
from selenium import webdriver
from pageObjects import LoginPage


class TestLogin(unittest.TestCase):
    baseURL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    username = 'Admin'
    password = 'admin123'
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_login(self):
        lp = LoginPage.LoginPage(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        act_title = self.driver.title
        lp.clickUser()
        lp.clickLogout()
        self.assertEqual(act_title, 'OrangeHRM', 'Title not match')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))
