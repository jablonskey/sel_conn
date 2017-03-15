# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0

from service import common_tasks


class AdminBenutzerrolleTest(unittest.TestCase, common_tasks.CommonTasks):
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

    def test_admin_benutzerrolle(self):
        driver = self.driver
        self.login_to_admin_panel(self.base_url)
        driver.implicitly_wait(2)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div[1]/a)")))
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div[1]/a)")))
        driver.find_element_by_xpath("(/html/body/div/div/div/section/div/div[2]/div[1]/a)").click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.CURRENT_PAGE_MAIN_HEADER)))
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, self.CURRENT_PAGE_MAIN_HEADER),
                                             "Benutzer anlegen"))

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((
                By.NAME, "userType")))
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.NAME, "userType")))

        userTypecombo = Select(driver.find_element_by_name("userType"))

        try:
            self.assertEqual("", userTypecombo.first_selected_option.text)
        except AssertionError as e:
            self.verificationErrors.append("Benutzerrolle combo: %s instead of %s" % (
                userTypecombo.first_selected_option.text,
                ""))

        self.assertTrue(7, len(Select(driver.find_element_by_id("userType")).options))

        userTypelist = [u"",
                        u"Administrator",
                        u"Superuser",
                        u"Vermittler",
                        u"Mitarbeiter",
                        u"Orga",
                        u"Service"]

        for x in range(len(Select(driver.find_element_by_name("userType")).options)):
            try:
                self.assertEqual(userTypelist[x], userTypecombo.options[x].text)
            except AssertionError as e:
                self.verificationErrors.append("userTypecombo, present:%s expected:%s" % (
                    userTypecombo.options[x].text, userTypelist[x]))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
