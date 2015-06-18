from selenium import webdriver
import unittest, time, re
from service import common_tasks
from selenium.webdriver.support.ui import Select

class AnonymusVermittlerTest(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
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
        self.go_to_vermittler_portal_page(self.base_url)
        self.open_taa_vm()
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_zuruck_zielgruppe()

        try:
            self.assertEqual(self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).get_attribute("value"), vmnr_number)
        except AssertionError as e:
            self.verificationErrors.append("VMNR number not correct after zuruck")

        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_zuruck_tarifdaten()
        self.tarifdaten_zuruck_zielgruppe()

        try:
            self.assertEqual(self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).get_attribute("value"), vmnr_number)
        except AssertionError as e:
            self.verificationErrors.append("VMNR number not correct after zuruck")

        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_zuruck_antrastellerdaten()
        self.antragsteller_zuruck_tarifdaten()
        self.tarifdaten_zuruck_zielgruppe()

        try:
            self.assertEqual(self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).get_attribute("value"), vmnr_number)
        except AssertionError as e:
            self.verificationErrors.append("VMNR number not correct after zuruck")

        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_weiter_antrag()
        self.antrag_zuruck_zusatzdaten()
        self.zusatzdaten_zuruck_antrastellerdaten()
        self.antragsteller_zuruck_tarifdaten()
        self.tarifdaten_zuruck_zielgruppe()

        try:
            self.assertEqual(self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).get_attribute("value"), vmnr_number)
        except AssertionError as e:
            self.verificationErrors.append("VMNR number not correct after zuruck")

    def test_vmnr_remebered_after_login_on_tarifdaten(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_portal_page(self.base_url)
        self.open_taa_vm()
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.login_to_connect_vermittler(self.base_url, main_page_after_login=False)
        self.tarifdaten_zuruck_zielgruppe()

        try:
            self.assertEqual(Select(self.driver.find_element_by_xpath(self.ZIELGRUPPE_VMNR_COMBO_XPATH)).first_selected_option.text, vmnr_number)
        except AssertionError as e:
            self.verificationErrors.append("Wrong VMNR in combo box")

    def test_vmnr_remebered_after_login_on_antragstellerdaten(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_portal_page(self.base_url)
        self.open_taa_vm()
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()
        self.login_to_connect_vermittler(self.base_url, main_page_after_login=False)
        self.antragsteller_zuruck_tarifdaten()
        self.tarifdaten_zuruck_zielgruppe()

        try:
            self.assertEqual(Select(self.driver.find_element_by_xpath(self.ZIELGRUPPE_VMNR_COMBO_XPATH)).first_selected_option.text, vmnr_number)
        except AssertionError as e:
            self.verificationErrors.append("Wrong VMNR in combo box")

    def test_vmnr_remebered_after_login_on_zusatzdaten(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_portal_page(self.base_url)
        self.open_taa_vm()
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_weiter_zusatzdaten()
        self.login_to_connect_vermittler(self.base_url, main_page_after_login=False)
        self.zusatzdaten_zuruck_antrastellerdaten()
        self.antragsteller_zuruck_tarifdaten()
        self.tarifdaten_zuruck_zielgruppe()

        try:
            self.assertEqual(Select(self.driver.find_element_by_xpath(self.ZIELGRUPPE_VMNR_COMBO_XPATH)).first_selected_option.text, vmnr_number)
        except AssertionError as e:
            self.verificationErrors.append("Wrong VMNR in combo box")

    def test_vmnr_remebered_after_login_on_antrag(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_portal_page(self.base_url)
        self.open_taa_vm()
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_weiter_antrag()
        self.login_to_connect_vermittler(self.base_url, main_page_after_login=False)
        self.antrag_zuruck_zusatzdaten()
        self.zusatzdaten_zuruck_antrastellerdaten()
        self.antragsteller_zuruck_tarifdaten()
        self.tarifdaten_zuruck_zielgruppe()

        try:
            self.assertEqual(Select(self.driver.find_element_by_xpath(self.ZIELGRUPPE_VMNR_COMBO_XPATH)).first_selected_option.text, vmnr_number)
        except AssertionError as e:
            self.verificationErrors.append("Wrong VMNR in combo box")

    def test_login_with_no_rights_to_taa_after_zielgruppe(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_portal_page(self.base_url)
        self.open_taa_vm()
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)
        self.login_to_connect_vermittler(self.base_url, user="test2@ks", user_with_taa_rights=False)

    def test_login_with_no_rights_to_taa_after_tarifdaten(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_portal_page(self.base_url)
        self.open_taa_vm()
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()

        self.login_to_connect_vermittler(self.base_url, user="test2@ks", user_with_taa_rights=False)

    def test_login_with_no_rights_to_taa_after_antragstellerdaten(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_portal_page(self.base_url)
        self.open_taa_vm()
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()

        self.login_to_connect_vermittler(self.base_url, user="test2@ks", user_with_taa_rights=False)

    def test_login_with_no_rights_to_taa_after_zusatzdaten(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_portal_page(self.base_url)
        self.open_taa_vm()
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_weiter_zusatzdaten()

        self.login_to_connect_vermittler(self.base_url, user="test2@ks", user_with_taa_rights=False)

    def test_login_with_no_rights_to_taa_after_antrag(self):
        driver = self.driver
        vmnr_number = "100063"
        self.go_to_vermittler_portal_page(self.base_url)
        self.open_taa_vm()
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_ANON_VMNR_FORM_XPATH).send_keys(vmnr_number)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_weiter_antrag()

        self.login_to_connect_vermittler(self.base_url, user="test2@ks", user_with_taa_rights=False)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()