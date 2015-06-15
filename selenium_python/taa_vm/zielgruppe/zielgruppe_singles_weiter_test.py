# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from service import common_tasks


class ZielgruppeSingelsWeiterTest(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = False
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(30)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_zielgruppe_singels_weiter(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("singles")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_zuruck_zielgruppe()
        try:
            self.assertTrue(driver.find_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["singles"]["radio_xpath"]).is_selected())
        except AssertionError as e:
            self.verificationErrors.append("Singles not selected")
        self.zielgruppe_weiter_tarifdaten()



    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
