# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from service import common_tasks


class Connect939Test(unittest.TestCase, common_tasks.CommonTasks):
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

    def test_zahlweise_jahrlich(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.go_to_rechner()
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_fill_data_lebenspartner(selected_radiobutton="nein")
        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_weiter_antrag()
        self.antrag_antragsteller_check_text(u"Zahlungsweise: jährlich")

    def test_zahlweise_halbjahrlich(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.go_to_rechner()
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_select_zahlweise("halbjahrlich")
        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_fill_data_lebenspartner(selected_radiobutton="nein")
        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_weiter_antrag()
        self.antrag_antragsteller_check_text(u"Zahlungsweise: halbjährlich")

    def test_zahlweise_vierteljahrlich(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.go_to_rechner()
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_select_zahlweise("vierteljahrlich")
        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_fill_data_lebenspartner(selected_radiobutton="nein")
        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_weiter_antrag()
        self.antrag_antragsteller_check_text(u"Zahlungsweise: vierteljährlich")

    def test_zahlweise_monatlich(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.go_to_rechner()
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_select_zahlweise("monatlich")
        self.tarifdaten_weiter_antrastellerdaten()

        self.antragsteller_fill_data_lebenspartner(selected_radiobutton="nein")
        self.antragsteller_fill_data_antragstellerdaten()
        self.driver.find_element_by_id("iban").send_keys("DE88300606010301156608")
        self.antragsteller_fill_data_vorversicherung()

        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_weiter_antrag()
        self.antrag_antragsteller_check_text(u"Zahlungsweise: monatlich")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
