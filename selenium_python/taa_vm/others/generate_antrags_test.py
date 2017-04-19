# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from service.common_tasks import CommonTasks


class GenerateAntrags(unittest.TestCase, CommonTasks):
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
        self.driver.implicitly_wait(10)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    @unittest.skip("generates bazillion og antrags")
    def test_generate_antrags(self):

        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        main_window = driver.current_window_handle
        self.go_to_rechner()
        self.driver.implicitly_wait(2)

        for x in range(10000):
            self.zielgruppe_btrklasse_select_by_name("familien")
            self.zielgruppe_weiter_tarifdaten()
            self.tarifdaten_weiter_antrastellerdaten()
            self.antragsteller_fill_data()
            self.antragsteller_weiter_zusatzdaten()

            self.zusatzdaten_weiter_antrag()
            self.check_and_click_element_by_link_text("Antrag senden")
            self.check_if_on_bestatigung_page()
            self.check_and_click_element_by_link_text("Neues Angebot")
            self.check_if_on_zielgruppe_page()
            print 'loop %d' % x

        driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
