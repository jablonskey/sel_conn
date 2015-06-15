# -*- coding: utf-8 -*-
import unittest
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from service.common_tasks import CommonTasks


class AntragstellerVorversicherungValidationTest(unittest.TestCase, CommonTasks):
    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = False
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(10)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None


    def test_antragsteller_vorversicherung_validation(self):
        driver = self.driver

        self.login_to_connect_vermittler(self.base_url)

        # region vermittler main page
        self.open_taa_vm()

        # endregion

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()
        # ### Antragstellerdaten ###

        self.assertTrue(driver.find_element_by_name("vorversicherung").is_selected())

        # region geselschaft
        try:
            self.assertRegexpMatches(driver.find_element_by_id("gesellschaft").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("gesellschaft")

        gesellschaftcombo = Select(driver.find_element_by_name("gesellschaft"))

        self.assertTrue(63, len(Select(driver.find_element_by_id("gesellschaft")).options))

        gesellschaftlist = [u"",
                            u"ACE",
                            u"ADAC",
                            u"KS-Gruppe",
                            u"AdvoCard",
                            u"AGRIPPINA",
                            u"ALBINGIA",
                            u"Allianz",
                            u"Allrecht",
                            u"ARAG",
                            u"ASPECTA",
                            u"Badische",
                            u"BBV",
                            u"BVB",
                            u"Bruderhilfe",
                            u"CONCORDIA",
                            u"DA",
                            u"DARAG",
                            u"DAS",
                            u"DBV",
                            u"Debeka",
                            u"DEURAG",
                            u"Herold",
                            u"DEVK",
                            u"DMB",
                            u"GEGENSEITIGKEIT",
                            u"Generali",
                            u"Gerling",
                            u"HM",
                            u"HDI",
                            u"HUK-COBURG",
                            u"Itzehoer",
                            u"Karlsruher",
                            u"KRAVAG",
                            u"LSH",
                            u"LVM",
                            u"Mecklenburgische",
                            u"MV",
                            u"NRV",
                            u"ÖRAG",
                            u"RU",
                            u"ROLAND",
                            u"R+V",
                            u"SECURITAS",
                            u"Uelzener",
                            u"VHV",
                            u"Vereinte",
                            u"VGH",
                            u"Württ. Gemeinde",
                            u"WüBa",
                            u"Württembergische",
                            u"Zürich",
                            u"Sparkassenversicherung",
                            u"Provinzial",
                            u"HRV",
                            u"Continentale",
                            u"JANITOS",
                            u"AUXILIA",
                            u"Domcura",
                            u"KS-Auxilia-Vorvers.",
                            u"Mig(s.KI206-Notiz)",
                            u"Alte Leipziger",
                            u"Sonstige"]

        for x in range(len(Select(driver.find_element_by_name("gesellschaft")).options)):
            try:
                self.assertEqual(gesellschaftlist[x], gesellschaftcombo.options[x].text)
            except AssertionError as e:
                self.verificationErrors.append("gesellschaftcombo, present:%s expected:%s" % (
                    gesellschaftcombo.options[x].text, gesellschaftlist[x]))

        Select(driver.find_element_by_id("gesellschaft")).select_by_index(1)
        self.assertTrue(62, len(Select(driver.find_element_by_id("gesellschaft")).options))

        gesellschaftlist = [u"ACE",
                            u"ADAC",
                            u"KS-Gruppe",
                            u"AdvoCard",
                            u"AGRIPPINA",
                            u"ALBINGIA",
                            u"Allianz",
                            u"Allrecht",
                            u"ARAG",
                            u"ASPECTA",
                            u"Badische",
                            u"BBV",
                            u"BVB",
                            u"Bruderhilfe",
                            u"CONCORDIA",
                            u"DA",
                            u"DARAG",
                            u"DAS",
                            u"DBV",
                            u"Debeka",
                            u"DEURAG",
                            u"Herold",
                            u"DEVK",
                            u"DMB",
                            u"GEGENSEITIGKEIT",
                            u"Generali",
                            u"Gerling",
                            u"HM",
                            u"HDI",
                            u"HUK-COBURG",
                            u"Itzehoer",
                            u"Karlsruher",
                            u"KRAVAG",
                            u"LSH",
                            u"LVM",
                            u"Mecklenburgische",
                            u"MV",
                            u"NRV",
                            u"ÖRAG",
                            u"RU",
                            u"ROLAND",
                            u"R+V",
                            u"SECURITAS",
                            u"Uelzener",
                            u"VHV",
                            u"Vereinte",
                            u"VGH",
                            u"Württ. Gemeinde",
                            u"WüBa",
                            u"Württembergische",
                            u"Zürich",
                            u"Sparkassenversicherung",
                            u"Provinzial",
                            u"HRV",
                            u"Continentale",
                            u"JANITOS",
                            u"AUXILIA",
                            u"Domcura",
                            u"KS-Auxilia-Vorvers.",
                            u"Mig(s.KI206-Notiz)",
                            u"Alte Leipziger",
                            u"Sonstige"]

        for x in range(len(Select(driver.find_element_by_name("gesellschaft")).options)):
            try:
                self.assertEqual(gesellschaftlist[x], gesellschaftcombo.options[x].text)
            except AssertionError as e:
                self.verificationErrors.append("gesellschaftcombo, present:%s expected:%s" % (
                    gesellschaftcombo.options[x].text, gesellschaftlist[x]))
        # endregion
        # region versicherungsscheinnummer
        try:
            self.assertRegexpMatches(driver.find_element_by_id("versicherungsscheinnummer").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Field versicherungsscheinnummer required but not invalid if empty")

        self.validate_element_by_id("versicherungsscheinnummer", ".", "valid")
        self.driver.find_element_by_id("versicherungsscheinnummer").clear()

        try:
            self.assertRegexpMatches(driver.find_element_by_id("versicherungsscheinnummer").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Field versicherungsscheinnummer required but not invalid if empty")

        self.validate_element_by_id("versicherungsscheinnummer", "vers1", "valid")
        # endregion
        # region Gekündigt durch
        try:
            self.assertRegexpMatches(driver.find_element_by_id("gekundig").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("gekundig")

        gekundigCombo = Select(driver.find_element_by_name("gekundig"))

        self.assertTrue(4, len(Select(driver.find_element_by_id("gekundig")).options))

        gekundigList = [u"",
                        u"Versicherungsnehmer",
                        u"Gesellschaft",
                        u"Ungekündigt"]

        for x in range(len(Select(driver.find_element_by_name("gekundig")).options)):
            try:
                self.assertEqual(gekundigList[x], gekundigCombo.options[x].text)
            except AssertionError as e:
                self.verificationErrors.append("gekundigCombo, present:%s expected:%s" % (
                    gekundigCombo.options[x].text, gekundigList[x]))

        Select(driver.find_element_by_id("gekundig")).select_by_index(1)

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("gekundig").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("field gekundig durch")

        self.assertTrue(3, len(Select(driver.find_element_by_id("gekundig")).options))
        gekundigList = [u"Versicherungsnehmer",
                        u"Gesellschaft",
                        u"Ungekündigt"]

        for x in range(len(Select(driver.find_element_by_name("gekundig")).options)):
            try:
                self.assertEqual(gekundigList[x], gekundigCombo.options[x].text)
            except AssertionError as e:
                self.verificationErrors.append("gekundigCombo, present:%s expected:%s" % (
                    gekundigCombo.options[x].text, gekundigList[x]))

        # endregion
        # region Beginn
        try:
            self.assertNotRegexpMatches(driver.find_element_by_name("beginn").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("field beginn invalid, empty but not required")

        self.validate_element_by_id("beginn", "xxxxxxxxx", "notaccepted")
        self.validate_element_by_id("beginn", "xx.xx.xxxx", "notaccepted")
        self.validate_element_by_id("beginn", "%s.%s.%s" % (
            str((datetime.datetime.today() + datetime.timedelta(days=1)).day).zfill(2),
            str((datetime.datetime.today() + datetime.timedelta(days=1)).month).zfill(2),
            str((datetime.datetime.today() + datetime.timedelta(days=1)).year).zfill(2)), "invalid")
        self.validate_element_by_id("beginn", "%s.%s.%s" % (
            str(datetime.datetime.now().day).zfill(2), str(datetime.datetime.now().month).zfill(2),
            str(datetime.datetime.now().year).zfill(2)), "invalid")
        self.validate_element_by_id("beginn", "%s.%s.%s" % (
            str((datetime.datetime.today() - datetime.timedelta(days=1)).day).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).month).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).year).zfill(2)), "valid")
        self.validate_element_by_id("beginn", "31.09.2013", "invalid")
        self.validate_element_by_id("beginn", "30.09.2013", "valid")
        self.validate_element_by_id("beginn", "29.02.2013", "invalid")
        self.validate_element_by_id("beginn", "28.02.2013", "valid")
        self.validate_element_by_id("beginn", "29.02.2012", "valid")
        self.driver.find_element_by_name("beginn").clear()

        try:
            self.assertNotRegexpMatches(driver.find_element_by_name("beginn").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("field beginn invalid, empty but not required")
        self.validate_element_by_id("beginn", "01.01.2014", "valid")
        # endregion
        # region Ende

        try:
            self.assertNotRegexpMatches(driver.find_element_by_name("ende").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("field ende invalid, empty but not required")

        self.validate_element_by_id("ende", "xxxxxxxxx", "notaccepted")
        self.validate_element_by_id("ende", "xx.xx.xxxx", "notaccepted")
        self.validate_element_by_id("ende", "%s.%s.%s" % (
            str((datetime.datetime.today() + datetime.timedelta(days=1)).day).zfill(2),
            str((datetime.datetime.today() + datetime.timedelta(days=1)).month).zfill(2),
            str((datetime.datetime.today() + datetime.timedelta(days=1)).year).zfill(2)), "valid")

        self.validate_element_by_id("ende", "31.09.2013", "invalid")
        self.validate_element_by_id("ende", "30.09.2013", "invalid")
        self.validate_element_by_id("ende", "29.02.2013", "invalid")
        self.validate_element_by_id("ende", "28.02.2013", "invalid")
        self.validate_element_by_id("ende", "01.01.2014", "invalid")

        self.validate_element_by_id("beginn", "%s.%s.%s" % (
            str((datetime.datetime.today() - datetime.timedelta(days=1)).day).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).month).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).year).zfill(2)), "invalid")

        self.validate_element_by_id("ende", "%s.%s.%s" % (
            str((datetime.datetime.today() - datetime.timedelta(days=1)).day).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).month).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).year).zfill(2)), "invalid")

        self.validate_element_by_id("ende", "%s.%s.%s" % (
            str(datetime.datetime.now().day).zfill(2), str(datetime.datetime.now().month).zfill(2),
            str(datetime.datetime.now().year).zfill(2)), "valid")

        self.validate_element_by_id("ende", "%s.%s.%s" % (
            str((datetime.datetime.today() - datetime.timedelta(days=2)).day).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=2)).month).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=2)).year).zfill(2)), "invalid")

        self.validate_element_by_id("beginn", "01.06.2014", "valid")
        self.validate_element_by_id("ende", "01.05.2014", "invalid")
        self.validate_element_by_id("ende", "01.06.2014", "invalid")
        self.validate_element_by_id("ende", "01.07.2014", "valid")
        self.driver.find_element_by_name("ende").clear()

        try:
            self.assertNotRegexpMatches(driver.find_element_by_name("ende").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("field ende invalid, empty but not required")

        # endregion

        # region versicherungsumfang

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("versicherungsumfang").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("field versicherungsumfang invalid, empty but not required")

        self.validate_element_by_id("versicherungsumfang", ".", "valid")
        self.driver.find_element_by_id("versicherungsumfang").clear()

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("versicherungsumfang").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("field versicherungsumfang invalid, empty but not required")

        # endregion

        # region vorversicherung plusminus

        # add vers2
        self.check_and_click_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[3]/a)")

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH,
             "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[3]/div/form/div[2]/div[2]/input)")))
        self.highlight(driver.find_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[3]/div/form/div[2]/div[2]/input)"))
        driver.find_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[3]/div/form/div[2]/div[2]/input)").send_keys(
            "vers2_umfang")
        vers2_umfang = driver.find_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[3]/div/form/div[2]/div[2]/input)").get_attribute(
            "value")

        # region Beginn
        beginn2_xpath = "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[3]/div/form/div[1]/div[4]/input)"

        try:
            self.assertNotRegexpMatches(driver.find_element_by_xpath(beginn2_xpath).get_attribute(
                "class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("field beginn invalid, empty but not required")

        # region dates validation
        self.validate_element_by_xpath(beginn2_xpath, "xxxxxxxxx", "notaccepted")
        self.validate_element_by_xpath(beginn2_xpath, "xx.xx.xxxx", "notaccepted")
        self.validate_element_by_xpath(beginn2_xpath, "%s.%s.%s" % (
            str((datetime.datetime.today() + datetime.timedelta(days=1)).day).zfill(2),
            str((datetime.datetime.today() + datetime.timedelta(days=1)).month).zfill(2),
            str((datetime.datetime.today() + datetime.timedelta(days=1)).year).zfill(2)), "invalid")
        self.validate_element_by_xpath(beginn2_xpath, "%s.%s.%s" % (
            str(datetime.datetime.now().day).zfill(2), str(datetime.datetime.now().month).zfill(2),
            str(datetime.datetime.now().year).zfill(2)), "invalid")
        self.validate_element_by_xpath(beginn2_xpath, "%s.%s.%s" % (
            str((datetime.datetime.today() - datetime.timedelta(days=1)).day).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).month).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).year).zfill(2)), "valid")
        self.validate_element_by_xpath(beginn2_xpath, "31.09.2013", "invalid")
        self.validate_element_by_xpath(beginn2_xpath, "30.09.2013", "valid")
        self.validate_element_by_xpath(beginn2_xpath, "29.02.2013", "invalid")
        self.validate_element_by_xpath(beginn2_xpath, "28.02.2013", "valid")
        self.validate_element_by_xpath(beginn2_xpath, "29.02.2012", "valid")
        self.validate_element_by_xpath(beginn2_xpath, "01.01.2014", "valid")
        # endregion
        # endregion
        # region Ende

        ende2_xpath = "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[3]/div/form/div[2]/div[1]/input)"

        try:
            self.assertNotRegexpMatches(driver.find_element_by_xpath(ende2_xpath).get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("field ende2 invalid, empty but not required")

        # region dates validation
        self.validate_element_by_xpath(ende2_xpath, "xxxxxxxxx", "notaccepted")
        self.validate_element_by_xpath(ende2_xpath, "xx.xx.xxxx", "notaccepted")
        self.validate_element_by_xpath(ende2_xpath, "%s.%s.%s" % (
            str((datetime.datetime.today() + datetime.timedelta(days=1)).day).zfill(2),
            str((datetime.datetime.today() + datetime.timedelta(days=1)).month).zfill(2),
            str((datetime.datetime.today() + datetime.timedelta(days=1)).year).zfill(2)), "valid")

        self.validate_element_by_xpath(ende2_xpath, "31.09.2013", "invalid")
        self.validate_element_by_xpath(ende2_xpath, "30.09.2013", "invalid")
        self.validate_element_by_xpath(ende2_xpath, "29.02.2013", "invalid")
        self.validate_element_by_xpath(ende2_xpath, "28.02.2013", "invalid")
        self.validate_element_by_xpath(ende2_xpath, "01.01.2014", "invalid")

        self.validate_element_by_xpath(beginn2_xpath, "%s.%s.%s" % (
            str((datetime.datetime.today() - datetime.timedelta(days=1)).day).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).month).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).year).zfill(2)), "invalid")
        self.validate_element_by_xpath(ende2_xpath, "%s.%s.%s" % (
            str((datetime.datetime.today() - datetime.timedelta(days=1)).day).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).month).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).year).zfill(2)), "invalid")
        self.validate_element_by_xpath(ende2_xpath, "%s.%s.%s" % (
            str(datetime.datetime.now().day).zfill(2), str(datetime.datetime.now().month).zfill(2),
            str(datetime.datetime.now().year).zfill(2)), "valid")
        self.validate_element_by_xpath(ende2_xpath, "%s.%s.%s" % (
            str((datetime.datetime.today() - datetime.timedelta(days=2)).day).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=2)).month).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=2)).year).zfill(2)), "invalid")

        self.validate_element_by_xpath(beginn2_xpath, "01.06.2014", "valid")
        self.validate_element_by_xpath(ende2_xpath, "01.05.2014", "invalid")
        self.validate_element_by_xpath(ende2_xpath, "01.06.2014", "invalid")
        self.validate_element_by_xpath(ende2_xpath, "01.07.2014", "valid")
        # endregion
        # endregion

        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        #     (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[4]/a)")))
        # self.highlight(driver.find_element_by_xpath(
        #     "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[4]/a)"))

        # plus vers3
        self.check_and_click_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[4]/a)")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,
             "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[4]/div/form/div[2]/div[2]/input)")))
        driver.find_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[4]/div/form/div[2]/div[2]/input)").send_keys(
            "vers3_umfang")

        # minus vers3
        self.check_and_click_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[4]/div/div/div/a)")

        try:
            self.assertEqual(driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[3]/div/form/div[2]/div[2]/input)").get_attribute(
                "value"),
                vers2_umfang)
        except AssertionError as e:
            self.verificationErrors.append("Field Versicherungsscheinnummer; present:" + driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[3]/div/form/div[2]/div[2]/input)").get_attribute(
                "value") + "\nexpected:" + vers2_umfang)

        # plus vers3
        self.check_and_click_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[4]/a)")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,
             "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[4]/div/form/div[2]/div[2]/input)")))
        try:
            self.assertEqual(driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[4]/div/form/div[2]/div[2]/input)").get_attribute(
                "value"),
                "")
        except AssertionError as e:
            self.verificationErrors.append("Field Versicherungsscheinnummer; present:" + driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[4]/div/form/div[2]/div[2]/input)").get_attribute(
                "value") + "\nexpected:" + "EMPTY")

        driver.find_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[4]/div/form/div[2]/div[2]/input)").send_keys(
            "vers3_umfang")

        # minus vers2 / vers3 goes to 2nd place
        self.check_and_click_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[3]/div/div/div/a)")
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH,
             "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[4]/div/form/div[2]/div[2]/input)")))
        try:
            self.assertEqual(driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[3]/div/form/div[2]/div[2]/input)").get_attribute(
                "value"),
                "vers3_umfang")
        except AssertionError as e:
            self.verificationErrors.append("Field Versicherungsscheinnummer; present:" + driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[3]/div/form/div[2]/div[2]/input)").get_attribute(
                "value") + "\nexpected:" + "vers3_umfang")

        # minus vers1 / vers3 goes to 1st place
        self.check_and_click_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[2]/div/div/div/a)")
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH,
             "(html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[4]/div/form/div[2]/div[2]/input)")))
        try:
            self.assertEqual(driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[2]/div/form/div[2]/div[2]/input)").get_attribute(
                "value"),
                "vers3_umfang")
        except AssertionError as e:
            self.verificationErrors.append("Field Versicherungsscheinnummer; present:" + driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[2]/div/form/div[2]/div[2]/input)").get_attribute(
                "value") + "\nexpected:" + "vers3_umfang")
            # endregion

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
