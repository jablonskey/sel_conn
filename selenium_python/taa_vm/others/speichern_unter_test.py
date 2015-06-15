# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from service.common_tasks import CommonTasks


class SpeichernUnterTest(unittest.TestCase, CommonTasks):


    def setUp(self):

        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = False
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(10)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_specihern_unter_abbrechen_on_all_tabs(self):

        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.speichern_unter_helper(button_to_click="abbrechen")
        self.tarifdaten_weiter_antrastellerdaten()
        self.speichern_unter_helper(button_to_click="abbrechen")
        self.antragsteller_fill_data()
        self.antragsteller_weiter_zusatzdaten()
        self.speichern_unter_helper(button_to_click="abbrechen")
        self.zusatzdaten_weiter_antrag()
        self.speichern_unter_helper(button_to_click="abbrechen")


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
