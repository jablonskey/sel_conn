# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0

from service import common_tasks


class Connect951Test(unittest.TestCase, common_tasks.CommonTasks):
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
        self.links_base_url = "https://vermittler.ks-auxilia.de/"

    @unittest.skip("skipped until tests adapted to new IFRAME")
    def test_connect951_logged_off(self):
        driver = self.driver

        self.go_to_vermittler_login_page(self.base_url)
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        self.check_and_click_element_by_xpath("(/html/body/div/div[3]/a)")
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, "(/html/body/div/div/h1)"), u"Ihr direkter Draht"))
        try:
            self.assertEqual("%sservice/ihr-direkter-Draht/" % self.links_base_url, driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    @unittest.skip("skipped until tests adapted to new IFRAME")
    def test_connect951_logged_in(self):
        driver = self.driver

        self.login_to_connect_vermittler(self.base_url)
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        self.check_and_click_element_by_xpath("(/html/body/div/div[2]/a)")
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, "(/html/body/div/div/h1)"), u"BD Stuttgart"))
        try:
            self.assertEqual("%sservice/ihr-kontakt-zu-uns/bezirksdirektionen/bd-stuttgart/" % self.links_base_url,
                             driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
__author__ = 'Jablonski'
