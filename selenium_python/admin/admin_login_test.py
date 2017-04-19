# -*- coding: utf-8 -*-
import os
import unittest
import sys

from datetime import datetime
from nose.plugins.attrib import attr
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from service import common_tasks


class AdminLoginTest(unittest.TestCase, common_tasks.CommonTasks):
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

    @attr('basic')
    def test_admin_login(self):
        driver = self.driver
        self.login_to_admin_panel(self.base_url)

    def tearDown(self):
        if sys.exc_info()[0]:
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
            test_method_name = self._testMethodName
            self.driver.save_screenshot('%s_%s_screenshot.png' % (now, test_method_name))
        super(self.__class__, self).tearDown()

        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
