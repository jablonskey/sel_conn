# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re
from service import common_tasks

class ZielgruppeFamilienWeiterTest(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = False
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(30)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_zielgruppe_familien_weiter(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_zuruck_zielgruppe()
        try:
            self.assertTrue(driver.find_element_by_xpath("(//input[@name='zielgruppe'])[1]").is_selected())
        except AssertionError as e:
            self.verificationErrors.append("Familien not selected")
        self.zielgruppe_weiter_tarifdaten()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
