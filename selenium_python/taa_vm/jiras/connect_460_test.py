# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, sys
from service import common_tasks


class Connect460Test(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
        print os.environ.get('SELENIUM_BROWSER')
        if os.environ.has_key("SELENIUM_BROWSER"):
            if os.environ['SELENIUM_BROWSER'] == "chrome":
                self.driver = webdriver.Chrome()
            elif os.environ['SELENIUM_BROWSER'] == "ie":
                self.driver = webdriver.Ie()
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

    def test_connect460(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)

        # region vermittler main page
        self.open_taa_vm()

        # endregion

        # region zielgruppe page

        self.zielgruppe_btrklasse_select_by_name(u"familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_select_produkt_from_mitgliedschaft(u"KS-Mitgliedschaft für die Familie")
        self.tarifdaten_weiter_antrastellerdaten()

        try:
            self.assertEqual(len(driver.find_elements_by_xpath(self.PRODUKTAUSWAHL_ELEMENTS_LABEL_XPATH)), 1)
        except AssertionError as e:
            self.verificationErrors(str(e))

        self.documents_popup_generate_document((u"Kurzangebot", u"Langangebot"))

        WebDriverWait(driver, 10).until_not(self.no_more_than_one_window_open)
        driver.switch_to.window(driver.window_handles[-1])

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div[1]/div[2]/div)")))

        text_divs_on_document = driver.find_elements_by_xpath("(/html/body/div[1]/div[2]/div[4]/div/div[1]/div[2]/div)")
        for text in text_divs_on_document:
            try:
                self.assertNotEqual(text.text, "KS-Mitgliedschaft")
            except AssertionError as e:
                self.verificationErrors.append("KS-Mitgliedschaft present on document")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

