# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from service import common_tasks


class AntragstellerDefaultViewTest(unittest.TestCase, common_tasks.CommonTasks):
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
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_antragsteller_default_view(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)

        # region vermittler main page
        self.go_to_rechner()

        # endregion

        # region zielgruppe page

        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()

        self.antragsteller_check_default_antragstellerdaten()
        self.antragsteller_check_default_kontaktdaten()
        self.antragsteller_check_default_lebenspartner()
        self.antragsteller_check_default_zahlungsdaten()
        self.antragsteller_check_default_vorversicherung()

        self.check_and_click_element_by_xpath(
            self.ANTRAGSTELLER_VORVERSICHERUNG_J_N_HELPER["nein"]["radio_xpath"])

        # TODO
        # WebDriverWait(driver, 5).until_not(EC.visibility_of_element_located((By.XPATH,
        # "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[5]/div/div[2]/div[2]/div/form/div[1]/div[1]/select)")))
        #
        # WebDriverWait(driver, 5).until_not(EC.presence_of_element_located((By.XPATH,
        # "(html/body/div/div/div/section/div/div[2]/div/div[4]/div/p)")))
        # WebDriverWait(driver, 5).until_not(EC.visibility_of_element_located((By.XPATH,
        # "(html/body/div/div/div/section/div/div[2]/div/div[4]/div/p)")))
        #
        # WebDriverWait(driver, 5).until_not(EC.text_to_be_present_in_element((By.XPATH,
        # "(html/body/div/div/div/section/div/div[2]/div/div[4]/div/p)"), "* = Pflichtfeld"))



        # endregion
        # endregion
        # ERROR: Caught exception [unknown command []]

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
