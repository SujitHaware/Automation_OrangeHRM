import sys
import unittest
import time

import HtmlTestRunner
from selenium import webdriver

sys.path.append('C:/Users/Sujitkumar Haware/Desktop/Sujit/Automation Testing/Automation_OrangeHRM')
from PageObj.Add_Employee import Add_Employee

class AddEmpTest(unittest.TestCase):
    baseURL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    username = 'Admin'
    password = 'admin123'
    firstname = 'Ram'
    middlename = 'Tejas'
    lastname = 'Patil'
    empid = int('301')
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
        aep = Add_Employee(self.driver)
        aep.setUsername(self.username)
        aep.setPassword(self.password)
        aep.clickLogin()
        aep.clickAddEmp()
        time.sleep(5)
        aep.setEmpFirstName(self.firstname)
        aep.setEmpMiddleName(self.middlename)
        aep.setEmpLastName(self.lastname)
        aep.setEmpId(self.empid)
        aep.clickSave()
        act_title = self.driver.title
        self.assertEqual(act_title, 'OrangeHRM', 'Title not match')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Sujitkumar Haware\\Desktop\\Sujit\\Automation Testing\\Automation_OrangeHRM\\Reports'))
