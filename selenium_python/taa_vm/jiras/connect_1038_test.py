# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from service import common_tasks


class Connect1038Test(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
        if os.environ.has_key("SELENIUM_BROWSER"):
            if os.environ['SELENIUM_BROWSER'] == "chrome":
                self.driver = webdriver.Chrome()
            elif os.environ['SELENIUM_BROWSER'] == "ie":
                caps = DesiredCapabilities.INTERNETEXPLORER
                caps['ignoreZoomSetting'] = True
                self.driver = webdriver.Ie(capabilities=caps)
            elif os.environ['SELENIUM_BROWSER'] == "firefox":
                profile = webdriver.FirefoxProfile()
                profile.native_events_enabled = False
                self.driver = webdriver.Firefox(profile)
        else:
            profile = webdriver.FirefoxProfile()
            profile.native_events_enabled = False
            self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(30)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_connect1038(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.go_to_rechner()

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("landwirte", 7)
        self.zielgruppe_weiter_tarifdaten()

        self.tarifdaten_zuruck_zielgruppe()
        self.zielgruppe_btrklasse_select_by_name("arzte", 10)

        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_zuruck_zielgruppe()
        try:
            self.assertNotEqual(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["landwirte"]["header_text"],
                                self.driver.find_element_by_xpath(
                                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["arzte"]["header_xpath"]).text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
__author__ = 'Jablonski'
