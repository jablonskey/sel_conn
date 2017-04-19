# -*- coding: utf-8 -*-
import os
import sys
import unittest
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from service import common_tasks


class AntragstellerKontaktdatenValidationTest(unittest.TestCase, common_tasks.CommonTasks):
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

    def test_antragsteller_kontaktdaten_validation(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)

        # region vermittler main page
        self.go_to_rechner()

        # endregion

        # region zielgruppe page

        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()
        # ### Kontaktdaten ###
        # -- Telefon INVALID
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("telefon").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("telefon").clear()
        driver.find_element_by_id("telefon").send_keys(".")
        try:
            self.assertRegexpMatches(driver.find_element_by_id("telefon").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("telefon").clear()
        driver.find_element_by_id("telefon").send_keys("*")
        try:
            self.assertRegexpMatches(driver.find_element_by_id("telefon").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        # -- Telefon VALID
        driver.find_element_by_id("telefon").clear()
        driver.find_element_by_id("telefon").send_keys("-")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("telefon").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("telefon").clear()
        driver.find_element_by_id("telefon").send_keys("/")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("telefon").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("telefon").clear()
        driver.find_element_by_id("telefon").send_keys("123")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("telefon").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("telefon").clear()
        driver.find_element_by_id("telefon").send_keys("123/-")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("telefon").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("telefon").clear()
        driver.find_element_by_id("telefon").send_keys("123-123")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("telefon").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("telefon").clear()
        driver.find_element_by_id("telefon").send_keys("123 123")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("telefon").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        # -- Mobil INVALID
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("mobil").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("mobil").clear()
        driver.find_element_by_id("mobil").send_keys(".")
        try:
            self.assertRegexpMatches(driver.find_element_by_id("mobil").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("mobil").clear()
        driver.find_element_by_id("mobil").send_keys("*")
        try:
            self.assertRegexpMatches(driver.find_element_by_id("mobil").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        # -- Mobil VALID
        driver.find_element_by_id("mobil").clear()
        driver.find_element_by_id("mobil").send_keys("-")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("mobil").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("mobil").clear()
        driver.find_element_by_id("mobil").send_keys("/")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("mobil").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("mobil").clear()
        driver.find_element_by_id("mobil").send_keys("123")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("mobil").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("mobil").clear()
        driver.find_element_by_id("mobil").send_keys("123/-")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("mobil").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("mobil").clear()
        driver.find_element_by_id("mobil").send_keys("123-123")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("mobil").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("mobil").clear()
        driver.find_element_by_id("mobil").send_keys("123 123")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("mobil").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        # -- Fax INVALID
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("fax").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("fax").clear()
        driver.find_element_by_id("fax").send_keys(".")
        try:
            self.assertRegexpMatches(driver.find_element_by_id("fax").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("fax").clear()
        driver.find_element_by_id("fax").send_keys("*")
        try:
            self.assertRegexpMatches(driver.find_element_by_id("fax").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        # -- Fax VALID
        driver.find_element_by_id("fax").clear()
        driver.find_element_by_id("fax").send_keys("-")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("fax").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("fax").clear()
        driver.find_element_by_id("fax").send_keys("/")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("fax").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("fax").clear()
        driver.find_element_by_id("fax").send_keys("123")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("fax").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("fax").clear()
        driver.find_element_by_id("fax").send_keys("123/-")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("fax").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("fax").clear()
        driver.find_element_by_id("fax").send_keys("123-123")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("fax").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("fax").clear()
        driver.find_element_by_id("fax").send_keys("123 123")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("fax").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        # -- Email INVALID
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("email").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(".")
        try:
            self.assertRegexpMatches(driver.find_element_by_id("email").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("*")
        try:
            self.assertRegexpMatches(driver.find_element_by_id("email").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("add@")
        try:
            self.assertRegexpMatches(driver.find_element_by_id("email").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(u"für@de")
        try:
            self.assertRegexpMatches(driver.find_element_by_id("email").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("@")
        try:
            self.assertRegexpMatches(driver.find_element_by_id("email").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("\\@de")
        try:
            self.assertRegexpMatches(driver.find_element_by_id("email").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("_sth_@domain_")
        try:
            self.assertRegexpMatches(driver.find_element_by_id("email").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        # -- Email VALID
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("sth@de")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("email").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("_sth@de")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("email").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("_sth@domain.de")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("email").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("sth@domain.de")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("email").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(".@de")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("email").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("_@de")
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("email").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

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
