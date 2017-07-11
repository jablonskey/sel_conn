# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from service import common_tasks


class AnonymusVermittlerTest(unittest.TestCase, common_tasks.CommonTasks):
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

    def test_vmnr_remebered_after_weiter_zuruck(self):
        driver = self.driver
        vmnr_number = "100065"
        self.go_to_vermittler_login_page(self.base_url)
        self.check_and_click_element_by_link_text("Rechner")
        self.check_if_on_vermittler_login_page(anonymus_info_visible=True)
        self.check_and_click_element_by_link_text("Rechner ohne Anmeldung")
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)

        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.click_zuruck_on_tarifdaten_go_to_zielgruppe()
        self.check_if_text_is_present_in_anon_vmnr_form(vmnr_number)

        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.click_weiter_on_tarifdaten_go_to_antragstellerdaten()
        self.click_zuruck_on_antragsteller_go_tarifdaten()
        self.tarifdaten_wait_for_price_reload()
        self.click_zuruck_on_tarifdaten_go_to_zielgruppe()
        self.check_if_text_is_present_in_anon_vmnr_form(vmnr_number)

        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.click_weiter_on_tarifdaten_go_to_antragstellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_fill_data_lebenspartner(selected_radiobutton="nein")
        self.click_weiter_on_antragsteller_go_to_zusatzdaten()
        self.click_zuruck_on_zusatzdaten_and_go_to_antragstellerdaten()
        self.click_zuruck_on_antragsteller_go_tarifdaten()
        self.tarifdaten_wait_for_price_reload()
        self.click_zuruck_on_tarifdaten_go_to_zielgruppe()
        self.check_if_text_is_present_in_anon_vmnr_form(vmnr_number)

        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.click_weiter_on_tarifdaten_go_to_antragstellerdaten()
        self.click_weiter_on_antragsteller_go_to_zusatzdaten()
        self.click_weiter_on_zusatzdaten_go_to_antrag()
        self.click_zuruck_on_antrag_and_go_to_zusatzdaten()
        self.click_zuruck_on_zusatzdaten_and_go_to_antragstellerdaten()
        self.click_zuruck_on_antragsteller_go_tarifdaten()
        self.tarifdaten_wait_for_price_reload()
        self.click_zuruck_on_tarifdaten_go_to_zielgruppe()
        self.check_if_text_is_present_in_anon_vmnr_form(vmnr_number)

    def test_vmnr_remebered_after_login_on_tarifdaten(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_login_page(self.base_url)
        self.check_and_click_element_by_link_text("Rechner")
        self.check_if_on_vermittler_login_page(anonymus_info_visible=True)
        self.check_and_click_element_by_link_text("Rechner ohne Anmeldung")
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.login_to_connect_vermittler(self.base_url, main_page_after_login=False)
        self.tarifdaten_wait_for_price_reload()
        self.click_zuruck_on_tarifdaten_go_to_zielgruppe()

        self.check_if_text_is_present_in_vmnr_combo(vmnr_number)

    def test_vmnr_remebered_after_login_on_antragstellerdaten(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_login_page(self.base_url)
        self.check_and_click_element_by_link_text("Rechner")
        self.check_if_on_vermittler_login_page(anonymus_info_visible=True)
        self.check_and_click_element_by_link_text("Rechner ohne Anmeldung")
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.click_weiter_on_tarifdaten_go_to_antragstellerdaten()
        self.login_to_connect_vermittler(self.base_url, main_page_after_login=False)
        self.click_zuruck_on_antragsteller_go_tarifdaten()
        self.click_zuruck_on_tarifdaten_go_to_zielgruppe()

        self.check_if_text_is_present_in_vmnr_combo(vmnr_number)

    def test_vmnr_remebered_after_login_on_zusatzdaten(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_login_page(self.base_url)
        self.check_and_click_element_by_link_text("Rechner")
        self.check_if_on_vermittler_login_page(anonymus_info_visible=True)
        self.check_and_click_element_by_link_text("Rechner ohne Anmeldung")
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.click_weiter_on_tarifdaten_go_to_antragstellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_fill_data_lebenspartner(selected_radiobutton="nein")
        self.click_weiter_on_antragsteller_go_to_zusatzdaten()
        self.login_to_connect_vermittler(self.base_url, main_page_after_login=False)
        self.click_zuruck_on_zusatzdaten_and_go_to_antragstellerdaten()
        self.click_zuruck_on_antragsteller_go_tarifdaten()
        self.click_zuruck_on_tarifdaten_go_to_zielgruppe()

        self.check_if_text_is_present_in_vmnr_combo(vmnr_number)

    def test_vmnr_remebered_after_login_on_antrag(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_login_page(self.base_url)
        self.check_and_click_element_by_link_text("Rechner")
        self.check_if_on_vermittler_login_page(anonymus_info_visible=True)
        self.check_and_click_element_by_link_text("Rechner ohne Anmeldung")
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.click_weiter_on_tarifdaten_go_to_antragstellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_fill_data_lebenspartner(selected_radiobutton="nein")
        self.click_weiter_on_antragsteller_go_to_zusatzdaten()
        self.click_weiter_on_zusatzdaten_go_to_antrag()
        self.login_to_connect_vermittler(self.base_url, main_page_after_login=False)
        self.click_zuruck_on_antrag_and_go_to_zusatzdaten()
        self.click_zuruck_on_zusatzdaten_and_go_to_antragstellerdaten()
        self.click_zuruck_on_antragsteller_go_tarifdaten()
        self.click_zuruck_on_tarifdaten_go_to_zielgruppe()

        self.check_if_text_is_present_in_vmnr_combo(vmnr_number)

    def test_login_with_no_rights_to_taa_after_zielgruppe(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_login_page(self.base_url)
        self.check_and_click_element_by_link_text("Rechner")
        self.check_if_on_vermittler_login_page(anonymus_info_visible=True)
        self.check_and_click_element_by_link_text("Rechner ohne Anmeldung")
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)
        self.login_to_connect_vermittler(self.base_url, user="test2@ks", user_with_taa_rights=False)

    def test_login_with_no_rights_to_taa_after_tarifdaten(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_login_page(self.base_url)
        self.check_and_click_element_by_link_text("Rechner")
        self.check_if_on_vermittler_login_page(anonymus_info_visible=True)
        self.check_and_click_element_by_link_text("Rechner ohne Anmeldung")
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten(hide_menu=False)

        self.login_to_connect_vermittler(self.base_url, user="test2@ks", user_with_taa_rights=False)

    def test_login_with_no_rights_to_taa_after_antragstellerdaten(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_login_page(self.base_url)
        self.check_and_click_element_by_link_text("Rechner")
        self.check_if_on_vermittler_login_page(anonymus_info_visible=True)
        self.check_and_click_element_by_link_text("Rechner ohne Anmeldung")
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten(hide_menu=False)
        self.click_weiter_on_tarifdaten_go_to_antragstellerdaten(hide_menu=False)

        self.login_to_connect_vermittler(self.base_url, user="test2@ks", user_with_taa_rights=False)

    def test_login_with_no_rights_to_taa_after_zusatzdaten(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_login_page(self.base_url)
        self.check_and_click_element_by_link_text("Rechner")
        self.check_if_on_vermittler_login_page(anonymus_info_visible=True)
        self.check_and_click_element_by_link_text("Rechner ohne Anmeldung")
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten(hide_menu=False)
        self.click_weiter_on_tarifdaten_go_to_antragstellerdaten(hide_menu=True)
        self.antragsteller_fill_data()
        self.antragsteller_fill_data_lebenspartner(selected_radiobutton="nein")
        self.click_weiter_on_antragsteller_go_to_zusatzdaten(hide_menu=False)

        self.login_to_connect_vermittler(self.base_url, user="test2@ks", user_with_taa_rights=False)

    def test_login_with_no_rights_to_taa_after_antrag(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_login_page(self.base_url)
        self.check_and_click_element_by_link_text("Rechner")
        self.check_if_on_vermittler_login_page(anonymus_info_visible=True)
        self.check_and_click_element_by_link_text("Rechner ohne Anmeldung")
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten(hide_menu=False)
        self.click_weiter_on_tarifdaten_go_to_antragstellerdaten(hide_menu=True)
        self.antragsteller_fill_data()
        self.antragsteller_fill_data_lebenspartner(selected_radiobutton="nein")
        self.click_weiter_on_antragsteller_go_to_zusatzdaten(hide_menu=False)
        self.click_weiter_on_zusatzdaten_go_to_antrag(hide_menu=False)

        self.login_to_connect_vermittler(self.base_url, user="test2@ks", user_with_taa_rights=False)

    def test_vermittler_login_with_no_rights_to_vmnr_after_tarifdaten(self):
        driver = self.driver
        vmnr_number = "102313"
        self.go_to_vermittler_login_page(self.base_url)
        self.check_and_click_element_by_link_text("Rechner")
        self.check_if_on_vermittler_login_page(anonymus_info_visible=True)
        self.check_and_click_element_by_link_text("Rechner ohne Anmeldung")
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()

        self.login_to_connect_vermittler(self.base_url, main_page_after_login=False)
        self.check_if_on_zielgruppe_page()
        self.check_if_warning_for_ivalid_vmnr_is_visible()
        self.check_if_vmnr_combo_is_empty()
        self.zielgruppe_enter_vmnr("100065")
        self.zielgruppe_btrklasse_select_by_name("singles")
        self.check_if_text_is_present_in_vmnr_combo("100065")

    def test_mitarbeiter_login_with_no_rights_to_vmnr_after_tarifdaten(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_login_page(self.base_url)
        self.check_and_click_element_by_link_text("Rechner")
        self.check_if_on_vermittler_login_page(anonymus_info_visible=True)
        self.check_and_click_element_by_link_text("Rechner ohne Anmeldung")
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()

        self.login_to_connect_vermittler(self.base_url, user="test3@ks", main_page_after_login=False)
        self.check_if_on_zielgruppe_page()
        self.check_if_warning_for_ivalid_vmnr_is_visible()
        self.check_if_vmnr_combo_is_empty()

        self.zielgruppe_enter_vmnr("100065")
        self.zielgruppe_btrklasse_select_by_name("singles")
        self.check_if_text_is_present_in_vmnr_combo("100065")

    def check_if_warning_for_ivalid_vmnr_is_visible(self):
        try:
            self.assertEqual(self.driver.find_element_by_xpath(self.ZIELGRUPPE_VMNR_COMBO_WARNING_XPATH).text,
                             u"Die von Ihnen eingegebene VMNR stimmt nicht mit der für diesen Account hinterlegten VMNR überein.")
        except AssertionError as e:
            self.verificationErrors.append("NO or WRONG warning under VMNR combo")

    def check_if_vmnr_combo_is_empty(self):
        try:
            self.assertEqual(self.driver.find_element_by_xpath(self.ZIELGRUPPE_VMNR_COMBO_BEFORE_CLICK_XPATH).text, "")
        except AssertionError as e:
            self.verificationErrors.append("VMNR combo box not empty")

    def check_if_text_is_present_in_vmnr_combo(self, text):
        try:
            text_to_check = self.driver.find_element_by_xpath(self.ZIELGRUPPE_VMNR_COMBO_BEFORE_CLICK_XPATH).text
            self.assertEqual(text_to_check,
                             text)
        except AssertionError as e:
            if (text_to_check == ""):
                self.verificationErrors.append("No VMNR selected in vmnr combo. Expected: %s" % (text))
            else:
                self.verificationErrors.append(
                    "Wrong VMNR in vmnr combo. Expected: %s / Present: %s" % (text, text_to_check))

    def check_if_text_is_present_in_anon_vmnr_form(self, text):
        try:
            text_to_check = self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).get_attribute(
                "value")
            self.assertEqual(text_to_check, text)
        except AssertionError as e:
            if (text_to_check == ""):
                self.verificationErrors.append("No VMNR selected in anon vmnr form. Expected: %s" % (text))
            else:
                self.verificationErrors.append(
                    "Wrong VMNR in anon mnr form. Expected: %s / Present: %s" % (text, text_to_check))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
