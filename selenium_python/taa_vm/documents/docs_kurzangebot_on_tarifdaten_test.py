# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from service.common_tasks import CommonTasks
import unittest, time, re


class DocsKurzangebotOnTarifdaten(unittest.TestCase, CommonTasks):
    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = False
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(10)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_docs_kurzangebot_on_tarifdaten(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()

        Select(driver.find_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/div[4]/div/div/div[2]/table[1]/tbody/tr[1]/td[8]/select)")).select_by_visible_text(
            "ohne SB")
        self.check_and_click_element_by_name("rechtschutz")
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[5]/div/div/div[1]/h4)"), u"Ergänzungen"))

        self.documents_popup_generate_document((u"Kurzangebot", ))

        WebDriverWait(driver, 10).until_not(self.no_more_than_one_window_open)
        driver.switch_to.window(driver.window_handles[-1])

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[2])")))
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[2])"),
                                             u"Vorschlag für Ihre KS/AUXILIA Rechtsschutz-Versicherung"))

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[108])")))
        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[108])")))

        version = self.driver.find_element_by_xpath("(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[108])").text

        try:
            self.assertRegexpMatches(version, r"TAA Online")
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\ version number not shown on document")

        driver.close()
        driver.switch_to.window(driver.window_handles[0])






def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
