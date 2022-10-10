class LoginPage():
    textbox_username_name = 'username'
    textbox_password_name = 'password'
    button_login_xpath = '//button[@type="submit"]'
    dropdown_user_xpath = '//p[@class="oxd-userdropdown-name"]'
    link_logout_linktext = 'Logout'
    button_addEmp_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'


    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_name(self.textbox_username_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_name(self.textbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickUser(self):
        self.driver.find_element_by_xpath(self.dropdown_user_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()

