# -*- coding: utf-8 -*-
import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from service import common_tasks


class Connect1038Test(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
        self.profile = webdriver.FirefoxProfile()
        self.profile.native_events_enabled = False
        self.driver = webdriver.Firefox(self.profile)
        self.driver.maximize_window()

        self.driver.implicitly_wait(2)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_connect1038(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()



        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("landwirte", 7)
        self.zielgruppe_weiter_tarifdaten()

        self.tarifdaten_zuruck_zielgruppe()
        self.zielgruppe_btrklasse_select_by_name("arzte", 10)

        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_zuruck_zielgruppe()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["arzte"]["header_xpath"])))
        WebDriverWait(self.driver, 20).until_not(EC.visibility_of_element_located(
            (By.XPATH, self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["landwirte"]["header_xpath"])))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["arzte"]["header_xpath"])))
        try:
            self.assertNotEqual(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["landwirte"]["header_text"],
                             self.driver.find_element_by_xpath(
                                 self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["landwirte"]["header_xpath"]).text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
__author__ = 'Jablonski'
