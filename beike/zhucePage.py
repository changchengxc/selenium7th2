from selenium import webdriver


        # driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        # driver.find_element_by_name("username").send_keys(row[0])
        # driver.find_element_by_name("password").send_keys(row[1])
        # driver.find_element_by_name("userpassword2").send_keys(row[2])
        # driver.find_element_by_name("mobile_phone").send_keys(row[3])
        # driver.find_element_by_name("email").send_keys(row[4])
        # driver.find_element_by_class_name("reg_btn").click()
from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = webdriver.Chrome()
        self.url = "http://localhost/index.php?m=user&c=public&a=reg"
        # driver.get("http://localhost/index.php?m=user&c=public&a=reg")

    def open(self):
        self.driver.get(self.url)

    # driver.find_element_by_name("username").send_keys(row[0])
    username_input_loc = (By.NAME, "username")
    def input_username(self, username):
        self.driver.find_element(*self.username_input_loc).send_keys(username)
