# -*- coding: utf-8 -*-
from selenium import webdriver
from service import common_tasks
import unittest


class AdminLoginTest(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = False
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(10)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_admin_login(self):
        driver = self.driver
        self.login_to_admin_panel(self.base_url)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
