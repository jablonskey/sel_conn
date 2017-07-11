# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from service import common_tasks


class ZielgruppeSelbstandigeWeiterTest(unittest.TestCase, common_tasks.CommonTasks):
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

    def test_zielgruppe_selbstandige_weiter(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.go_to_rechner()

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("selbstandige", 10)
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()

        # TODO
        # Check zielgruppe section on tarifdaten page

        self.click_zuruck_on_tarifdaten_go_to_zielgruppe()
        try:
            self.assertTrue(driver.find_element_by_xpath(
                self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["selbstandige"]["radio_xpath"]).is_selected())
        except AssertionError as e:
            self.verificationErrors.append("Selbstandige not selected")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
