import time
import unittest

import ddt
from selenium import webdriver

from beike.csvFileManager4 import CsvFileManager4
from beike.myTestCase import MyTestCase
from beike.zhucePage import RegisterPage
from day4.CsvFileManager3 import CsvFileManager3


@ddt.ddt
class ZhuceTest(MyTestCase):

    test_data = CsvFileManager4().read("test_data.csv")

    @ddt.data(*test_data)
    def test_zhuce(self, row):
        # driver = self.driver
        po = RegisterPage(self.driver)
        po.open()
        po.input_username(row[0])
        # driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        # driver.find_element_by_name("username").send_keys(row[0])
        # driver.find_element_by_name("password").send_keys(row[1])
        # driver.find_element_by_name("userpassword2").send_keys(row[2])
        # driver.find_element_by_name("mobile_phone").send_keys(row[3])
        # driver.find_element_by_name("email").send_keys(row[4])
        # driver.find_element_by_class_name("reg_btn").click()


if __name__ == '__main__':
    unittest.main()