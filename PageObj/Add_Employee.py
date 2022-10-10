class Add_Employee:
    textbox_username_name = 'username'
    textbox_password_name = 'password'
    button_login_xpath = '//button[@type="submit"]'
    button_AddEmp_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    textbox_firstname_xpath = '//input[@name="firstName"]'
    textbox_middlename_name = 'middleName'
    textbox_lastname_name = 'lastName'
    textbox_employeeid_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
    button_save_xpath = '//button[@type="submit"]'

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_name(self.textbox_username_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_name(self.textbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickAddEmp(self):
        self.driver.find_element_by_xpath(self.button_AddEmp_xpath).click()

    def setEmpFirstName(self, firstName):
        self.driver.find_element_by_xpath(self.textbox_firstname_xpath).send_keys(firstName)

    def setEmpMiddleName(self, middleName):
        self.driver.find_element_by_name(self.textbox_middlename_name).send_keys(middleName)

    def setEmpLastName(self, lastName):
        self.driver.find_element_by_name(self.textbox_lastname_name).send_keys(lastName)

    def setEmpId(self, id):
        self.driver.find_element_by_xpath(self.textbox_employeeid_xpath).send_keys(id)

    def clickSave(self):
        self.driver.find_element_by_xpath(self.button_save_xpath).click()