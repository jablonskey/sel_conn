# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0

from helpers import Helper
from overriders import SelectWithFooterSlide


class CommonTasks(Helper):
    def decrease_zoom(self, percent):
        for x in range((100 - percent) % 10):
            self.driver.find_element_by_tag_name("html").send_keys(Keys.CONTROL, Keys.SUBTRACT)

    def increase_zoom(self, percent):
        for x in range((percent - 100) % 10):
            self.driver.find_element_by_tag_name("html").send_keys(Keys.CONTROL, Keys.ADD)

    def reset_zoom(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.CONTROL, Keys.NUMPAD0)

    def go_to_vermittler_login_page(self, base_url):
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get(base_url + Helper.VERMITTLER_LOGIN_PAGE_ADDRESS_COMPLETION)
        self.check_if_on_vermittler_login_page()

    def go_to_external_page(self):
        self.driver.get("http://ks-software.com")
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, "(html/body/div/div/div/section/div/div[2]/div/div[1]/ng-include/h1)"), "Witaj!"))

    def go_to_aktservice_login_page(self, base_url):
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get(base_url + Helper.AKTSERVICE_LOGIN_PAGE_ADDRES_COMPLETION)
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, Helper.CURRENT_PAGE_MAIN_HEADER), "Login"))

    def login_to_aktservice(self, base_url, user=Helper.AKTSERVICE_USER_LOGIN,
                            password=Helper.AKTSERVICE_USER_PASSWORD):
        self.go_to_aktservice_login_page(base_url)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "mnr")))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "mnr")))
        self.driver.find_element_by_id("mnr").clear()
        self.driver.find_element_by_id("mnr").send_keys(user)
        self.driver.find_element_by_id("plz").clear()
        self.driver.find_element_by_id("plz").send_keys(password)

        self.check_and_click_element_by_xpath(Helper.AKTSERVICE_LOGIN_BUTTON_XPATH)

        WebDriverWait(self.driver, 20).until_not(EC.text_to_be_present_in_element(
            (By.XPATH, Helper.CURRENT_PAGE_MAIN_HEADER), "Login"))

        self.check_if_on_aktservice_page()
        self.driver.implicitly_wait(2)

    def go_to_secure_email_login_page(self, base_url):
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get(base_url + Helper.SECURE_EMAIL_LOGIN_PAGE_ADDRES_COMPLETION)
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, Helper.CURRENT_PAGE_MAIN_HEADER), "Login"))

    def go_to_admin_panel_page(self, base_url):
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get(base_url + Helper.ADMIN_LOGIN_PAGE_ADDRESS_COMPLETION)
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, Helper.CURRENT_PAGE_MAIN_HEADER), "Login"))

    def login_to_admin_panel(self, base_url, user=Helper.ADMIN_USER_LOGIN, password=Helper.ADMIN_USER_PASSWORD):
        self.go_to_admin_panel_page(base_url)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "username")))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "username")))
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(user)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)

        self.check_and_click_element_by_xpath(Helper.ADMIN_LOGIN_BUTTON_XPATH)

        WebDriverWait(self.driver, 20).until_not(EC.text_to_be_present_in_element(
            (By.XPATH, Helper.CURRENT_PAGE_MAIN_HEADER), "Login"))

        self.check_if_on_admin_main_page()
        self.driver.implicitly_wait(2)

    def login_to_secure_email(self, base_url, user=Helper.SECURE_EMAIL_USER_LOGIN,
                              password=Helper.SECURE_EMAIL_USER_PASSWORD):
        self.go_to_secure_email_login_page(base_url)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "username")))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "username")))
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(user)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)

        self.check_and_click_element_by_xpath(Helper.SECURE_EMAIL_LOGIN_BUTTON_XPATH)

        WebDriverWait(self.driver, 20).until_not(EC.text_to_be_present_in_element(
            (By.XPATH, Helper.CURRENT_PAGE_MAIN_HEADER), "Login"))

        self.check_if_on_secure_email_page()
        self.driver.implicitly_wait(2)

    def logout_admin(self):
        self.check_and_click_element_by_xpath(self.ADMIN_LOGOUT_LINK_XPATH)
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, Helper.CURRENT_PAGE_MAIN_HEADER), "Login"))

    def login_to_connect_vermittler(self, base_url, user=Helper.VERMITTLER_USER_LOGIN,
                                    password=Helper.VERMITTLER_USER_PASSWORD, main_page_after_login=True,
                                    user_with_taa_rights=True):
        self.go_to_vermittler_login_page(base_url)

        self.driver.execute_script(
            "document.getElementById('megadropdown-main-div').style.display = 'inline';")

        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(user)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)

        self.check_and_click_element_by_xpath(Helper.VERMITTLER_LOGIN_BUTTON_XPATH)

        WebDriverWait(self.driver, 20).until_not(EC.text_to_be_present_in_element(
            (By.XPATH, Helper.CURRENT_PAGE_MAIN_HEADER), "Login"))
        if main_page_after_login:
            self.check_if_on_vermittler_main_page(user_with_taa_rights=user_with_taa_rights)
        self.driver.implicitly_wait(2)

    def zielgruppe_enter_vmnr(self, vmnr):
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_VMNR_COMBO_BEFORE_CLICK_XPATH)
        self.driver.find_element_by_xpath(self.ZIELGRUPPE_VMNR_COMBO_FORM_CLICK_XPATH).send_keys(vmnr, Keys.ENTER)

    def logout_vermittler(self):
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        self.check_and_click_element_by_xpath(self.VERMITTLER_IFRAME_LOGOUT_XPATH)
        self.driver.switch_to_default_content()

    def check_if_links_tab_visible(self):

        links_tab_elements = self.driver.find_elements_by_xpath(Helper.PAGES_TABS_ELEMENTS_XPATH)

        self.assertEqual(6, len(links_tab_elements),
                         "Number of links on links_tab:%d; expected:%d" % (len(links_tab_elements), 6))

    def check_if_on_zielgruppe_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Helper.CURRENT_PAGE_MAIN_HEADER)))
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Helper.CURRENT_PAGE_MAIN_HEADER)))
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, Helper.CURRENT_PAGE_MAIN_HEADER),
            u"Online-Rechner"))
        self.check_if_links_tab_visible()

        self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Helper.ZIELGRUPPE_PRIVATKUNDEN_HEADER_XPATH)))
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Helper.ZIELGRUPPE_PRIVATKUNDEN_HEADER_XPATH)))
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, Helper.ZIELGRUPPE_PRIVATKUNDEN_HEADER_XPATH),
            u"Privatkunden"))

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Helper.ZIELGRUPPE_GESCHAFTSKUNDEN_XPATH)))
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Helper.ZIELGRUPPE_GESCHAFTSKUNDEN_XPATH)))
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, Helper.ZIELGRUPPE_GESCHAFTSKUNDEN_XPATH),
            u"Geschäftskunden"))

        self.hide_drop_down_menu()

        # TODO
        # desired_zielgruppe_labels = (
        # "Familien", "Singles", "Beamte", "Senioren", u"Selbständige / Firmen / Freiberufler",
        # u"Ärzte / Heilwesenberufe", u"Steuerberater / Wirtschaftsprüfer", "Landwirte")
        #
        # zielgruppe_labels = self.driver.find_elements_by_xpath(
        # Helper.ZIELGRUPPE_ELEMENTS_LABELS)
        #
        # zielgruppe_inputs = self.driver.find_elements_by_xpath(
        # Helper.ZIELGRUPPE_ELEMENTS_INPUTS_XPATH)
        #
        # for zielgruppe_label in zielgruppe_labels:
        # try:
        # self.assertEqual(desired_zielgruppe_labels[zielgruppe_labels.index(zielgruppe_label)],
        # zielgruppe_label.text)
        # except AssertionError:
        # self.verificationErrors.append(
        # "Zielgruppe %s instead of %s on position %d / line %d" % (
        # zielgruppe_label.text, desired_zielgruppe_labels[zielgruppe_inputs.index(zielgruppe_label)],
        # zielgruppe_inputs.index(zielgruppe_label),
        # sys.exc_info()[-1].tb_lineno))

    def neues_angebot_helper(self, button_to_click):
        self.check_and_click_element_by_link_text("Neues Angebot")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)"), u"Neues Angebot"))
        if button_to_click == "ok":
            self.check_and_click_element_by_xpath("/html/body/div[3]/div/div/div[3]/div/div[3]/button")
            WebDriverWait(self.driver, 20).until_not(
                EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
            WebDriverWait(self.driver, 20).until_not(
                EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))
            self.check_if_on_zielgruppe_page()
        elif button_to_click == "abbrechen":
            self.check_and_click_element_by_xpath("/html/body/div[3]/div/div/div[3]/div/div[1]/button")
            WebDriverWait(self.driver, 20).until_not(
                EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
            WebDriverWait(self.driver, 20).until_not(
                EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))

    def speichern_unter_helper(self, button_to_click, angebot_name=None):
        self.check_and_click_element_by_xpath(self.ERGEBNIS_OPTIONEN_SPEICHERN_UNTER_LINK_XPATH)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)"), "Speichern unter"))

        if button_to_click == "abbrechen":
            self.check_and_click_element_by_xpath("(/html/body/div[3]/div/div/form/div[2]/div/div[1]/button)")
            WebDriverWait(self.driver, 10).until_not(
                EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
            WebDriverWait(self.driver, 10).until_not(
                EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))

    def go_to_rechner(self):

        self.driver.implicitly_wait(2)
        self.check_and_click_element_by_link_text("Rechner")

        self.check_if_on_zielgruppe_page()

        zielgruppe_labels = self.driver.find_elements_by_xpath(
            Helper.ZIELGRUPPE_ELEMENTS_LABELS_XPATH)

        zielgruppe_inputs = self.driver.find_elements_by_xpath(
            Helper.ZIELGRUPPE_ELEMENTS_INPUTS_XPATH)
        for zielgruppe_input in zielgruppe_inputs:
            try:
                self.assertFalse(zielgruppe_input.is_selected())
            except AssertionError:
                self.verificationErrors.append(
                    "Zielgruppe %s selected" % (
                        zielgruppe_labels[zielgruppe_inputs.index(zielgruppe_input)].text))
        self.driver.implicitly_wait(2)

    # region zielgruppe common tasks
    def zielgruppe_btrklasse_select_by_name(self, btrklasse_name, anzahl=None, jahresbrutto=None):
        # Helper.ZIELGRUPPE_BTRKLASSES_HELPER_LIST = {
        # 'familien': (
        # "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[1]/div/div[2]/div/div[1]/label",
        # "Familien"),
        # 'singles': (
        # "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[1]/div/div[2]/div/div[2]/label",
        # "Singles"),
        # 'beamte': (
        # "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[1]/div/div[2]/div/div[3]/label",
        # "Beamte"),
        # 'senioren': (
        # "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[1]/div/div[2]/div/div[4]/label",
        # "Senioren"),
        #     'selbstandige': (
        #         "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[2]/div/div[2]/div/div[1]/label",
        #         u"Selbständige / Firmen / Freiberufler",
        #         "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div/form/div/div[1]/h4)"),
        #     'arzte': ("(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[2]/div/div[2]/div/div[2]/label",
        #               u"Ärzte / Heilwesenberufe",
        #               "(/html/body/div/div/div/section/div/div[2]/div/div[1]/div/form/div/div[1]/h4)"),
        #     'steuerberater': (
        #         "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[2]/div/div[2]/div/div[3]/label",
        #         u"Steuerberater / Wirtschaftsprüfer",
        #         "(/html/body/div/div/div/section/div/div[2]/div/div[3]/div/form/div/div[1]/h4)"),
        #     'landwirte': (
        #         "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[2]/div/div[2]/div/div[4]/label",
        #         u"Landwirte", "(/html/body/div/div/div/section/div/div[2]/div/div[4]/div/form/div/div[1]/h4)")
        # }

        gescahftskunden_headers = [
            self.driver.find_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST['selbstandige']["header_xpath"]),
            self.driver.find_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST['arzte']["header_xpath"]),
            self.driver.find_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST['steuerberater']["header_xpath"]),
            self.driver.find_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST['landwirte']["header_xpath"])]

        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["label_xpath"])

        self.assertTrue(self.driver.find_element_by_xpath(
            self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["radio_xpath"]).is_selected())

        if btrklasse_name in ("familien", "singles", "beamte", "senioren"):
            for el in self.driver.find_elements_by_xpath(
                    "(/html/body/div/div/div/section/div/div[2]/div/div[*]/div/form/div/div[1]/h4)"):
                try:
                    self.assertFalse(el.is_displayed())
                except AssertionError:
                    self.verificationErrors.append(
                        "Section %s should not be displayed for zielgruppe %s" % (el.text, btrklasse_name))

        elif btrklasse_name == 'selbstandige':
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["header_xpath"])))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["header_xpath"])))
            try:
                self.assertEqual(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["header_text"],
                                 self.driver.find_element_by_xpath(
                                     Helper.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["header_xpath"]).text)
            except AssertionError as e:
                self.verificationErrors.append(str(e))
            if anzahl is not None:
                self.check_and_click_element_by_xpath(
                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["anzahl_form_xpath"])
                self.driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["anzahl_form_xpath"]).clear()
                self.driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["anzahl_form_xpath"]).send_keys(anzahl)
            if jahresbrutto is not None:
                self.check_and_click_element_by_xpath(
                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["jahresbrutto_form_xpath"])
                self.driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["jahresbrutto_form_xpath"]).clear()
                self.driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["jahresbrutto_form_xpath"]).send_keys(
                    jahresbrutto)

        elif btrklasse_name == 'arzte':
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, Helper.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["header_xpath"])))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, Helper.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["header_xpath"])))
            try:
                self.assertEqual(Helper.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["header_text"],
                                 self.driver.find_element_by_xpath(
                                     Helper.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["header_xpath"]).text)
            except AssertionError as e:
                self.verificationErrors.append(str(e))

            if anzahl is not None:
                self.check_and_click_element_by_xpath(
                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["form_xpath"])
                self.driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["form_xpath"]).clear()
                self.driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["form_xpath"]).send_keys(anzahl)

        elif btrklasse_name == 'steuerberater':
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, Helper.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["header_xpath"])))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, Helper.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["header_xpath"])))
            try:
                self.assertEqual(Helper.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["header_text"],
                                 self.driver.find_element_by_xpath(
                                     Helper.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["header_xpath"]).text)
            except AssertionError as e:
                self.verificationErrors.append(str(e))
            if anzahl is not None:
                self.check_and_click_element_by_xpath(
                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["form_xpath"])
                self.driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["form_xpath"]).clear()
                self.driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["form_xpath"]).send_keys(anzahl)

        elif btrklasse_name == 'landwirte':
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, Helper.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["header_xpath"])))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, Helper.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["header_xpath"])))
            try:
                self.assertEqual(Helper.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["header_text"],
                                 self.driver.find_element_by_xpath(
                                     Helper.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["header_xpath"]).text)
            except AssertionError as e:
                self.verificationErrors.append(str(e))
            if anzahl is not None:
                self.check_and_click_element_by_name("isLandwirteMitglied")
                self.check_and_click_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]")
                self.check_and_click_element_by_xpath(
                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["form_xpath"])
                self.driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["form_xpath"]).clear()
                self.driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST[btrklasse_name]["form_xpath"]).send_keys(anzahl)

    def zielgruppe_weiter_tarifdaten(self, hide_menu=True):
        self.check_and_click_element_by_link_text("Weiter")

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, "(.//*[@id='rechner-section']/div/div[2]/div/div[1]/div/div/div[1]/h4)")),
            "Tarifdaten not reached")

        self.assertEqual("Zielgruppe", self.driver.find_element_by_xpath(
            "(.//*[@id='rechner-section']/div/div[2]/div/div[1]/div/div/div[1]/h4)").text)
        self.assertEqual(self.base_url + "ng/#/taa//tarifdaten", self.driver.current_url)

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, "rechtschutz")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "rechtschutz")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, "schutzbrief")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "schutzbrief")))

        # endregion

        # TODO
        # def get_produkt_name_from_table(self, table_name, row_no):
        # if table_name == "erganzungen":

        # region tarifdaten common tasks
        self.tarifdaten_wait_for_price_reload()
        if hide_menu:
            self.hide_drop_down_menu()

    def tarifdaten_zuruck_zielgruppe(self, hide_menu=True):
        self.check_and_click_element_by_link_text(u"Zurück")
        self.check_if_on_zielgruppe_page()
        if hide_menu:
            self.hide_drop_down_menu()

    def tarifdaten_zuruck_by_link_zielgruppe(self, hide_menu=True):
        self.check_and_click_element_by_link_text("Zielgruppe")
        self.check_if_on_zielgruppe_page()
        if hide_menu:
            self.hide_drop_down_menu()

    def tarifdaten_select_produkt_from_mitgliedschaft(self, produkt_name):
        self.driver.implicitly_wait(2)
        gesambtr = self.driver.find_element_by_xpath(self.TARIFDATEN_GESAMTBTR_LABEL_XPATH).text

        produkt_label_list = self.driver.find_elements_by_xpath(
            Helper.TARIFDATEN_PRODUKT_ELEMENTS_LABELS_MITGLIEDSCHAFT_XPATH)

        for i in produkt_label_list:
            if i.text == produkt_name:
                i.click()

        WebDriverWait(self.driver, 20).until_not(
            EC.text_to_be_present_in_element_value((By.XPATH, self.TARIFDATEN_GESAMTBTR_LABEL_XPATH), gesambtr))
        self.driver.implicitly_wait(0)
        self.tarifdaten_wait_for_price_reload()

    def tarifdaten_select_produkt_from_rechtschutz(self, produkt_name):
        self.driver.implicitly_wait(2)
        gesambtr = self.driver.find_element_by_xpath(self.TARIFDATEN_GESAMTBTR_LABEL_XPATH).text
        produkt_label_list = self.driver.find_elements_by_xpath(
            Helper.TARIFDATEN_PRODUKT_ELEMENTS_LABELS_RECHTSCHUTZ_XPATH)

        for i in produkt_label_list:
            if i.text == produkt_name:
                i.click()
        WebDriverWait(self.driver, 20).until_not(
            EC.text_to_be_present_in_element_value((By.XPATH, self.TARIFDATEN_GESAMTBTR_LABEL_XPATH), gesambtr))
        self.driver.implicitly_wait(0)
        self.tarifdaten_wait_for_price_reload()

    def tarifdaten_select_produkt_from_schutzbrief(self, produkt_name):

        produkt_label_list = self.driver.find_elements_by_xpath(
            Helper.TARIFDATEN_PRODUKT_ELEMENTS_LABELS_SCHUTZBRIEF_XPATH)

        for i in produkt_label_list:
            if i.text == produkt_name:
                i.click()
        self.tarifdaten_wait_for_price_reload()

    def tarifdaten_select_produkt_from_erganzungen_by_name(self, produkt_name):

        produkts_labels_list = self.driver.find_elements_by_xpath(
            Helper.TARIFDATEN_PRODUKT_ELEMENTS_LABELS_ERGANZUNGEN_XPATH)

        produkts_inputs_list = self.driver.find_elements_by_xpath(
            Helper.TARIFDATEN_PRODUKT_ELEMENTS_INPUTS_ERGANZUNGEN_XPATH)

        for i in produkts_labels_list:
            if i.text == produkt_name:
                # produkts_inputs_list[produkts_labels_list.index(i)].click()
                i.click()

        return produkt_name

    def tarifdaten_select_produkt_from_erganzungen_by_list_position(self, list_position):

        produkts_labels_list = self.driver.find_elements_by_xpath(
            Helper.TARIFDATEN_PRODUKT_ELEMENTS_LABELS_ERGANZUNGEN_XPATH)

        produkts_inputs_list = self.driver.find_elements_by_xpath(
            Helper.TARIFDATEN_PRODUKT_ELEMENTS_INPUTS_ERGANZUNGEN_XPATH)

        produkts_inputs_list[list_position - 1].click()
        self.tarifdaten_wait_for_price_reload()

        return produkts_labels_list[list_position - 1].text

    def tarifdaten_select_produkt_on_daten_erfassen_popup_by_name(self, produkt_name):
        produkt_label_list = self.driver.find_elements_by_xpath(
            Helper.ERGANZUNGEN_POPUP_PRODUKT_LABELS_XPATH)
        produkt_input_list = self.driver.find_elements_by_xpath(
            Helper.ERGANZUNGEN_POPUP_PRODUKT_INPUTS_XPATH)

        for i in produkt_label_list:
            if i.text == produkt_name:
                produkt_input_list[produkt_label_list.index(i)].click()

        return produkt_name

    def tarifdaten_select_produkt_on_daten_erfassen_popup_by_list_position(self, list_position):
        produkt_label_list = self.driver.find_elements_by_xpath(
            Helper.ERGANZUNGEN_POPUP_PRODUKT_LABELS_XPATH)
        produkt_input_list = self.driver.find_elements_by_xpath(
            Helper.ERGANZUNGEN_POPUP_PRODUKT_INPUTS_XPATH)

        produkt_input_list[list_position - 1].click()

        return produkt_label_list[list_position - 1]

    def tarifdaten_select_sb_for_produkt_from_rechtschutz(self, produkt_name, sb):

        produkt_label_list = self.driver.find_elements_by_xpath(
            Helper.TARIFDATEN_PRODUKT_ELEMENTS_LABELS_RECHTSCHUTZ_XPATH)

        sb_select_list = self.driver.find_elements_by_xpath(
            Helper.TARIFDATEN_PRODUKT_ELEMENTS_SB_COMBOS_RECHTSCHUTZ_XPATH)

        for i in produkt_label_list:
            if i.text == produkt_name:
                Select(self.driver.find_element_by_xpath(
                    "(.//*[@id='rechner-section']/div/div[2]/div/div[3]/div[1]/div/div/div[2]/table[1]/tbody/tr[" + str(
                        produkt_label_list.index(i) + 1) + "]/td[last()-1]/select)")).select_by_visible_text(
                    sb)

        self.tarifdaten_wait_for_price_reload()

    def tarifdaten_ermittlung_alert_handler(self, button_to_click=None, ermittlung_type="400", selected_radio_no=None,
                                            is_checkbox_checked="unchecked"):

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))

        if ermittlung_type == "400":
            WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
                (By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)"),
                u"Ermittlung der Selbstbeteiligung (Start-SB)"))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, "(/html/body/div[3]/div/div/div[2]/div[8]/label/input)")))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, "(/html/body/div[3]/div/div/div[2]/div[8]/label/input)")))
            # try:
            # self.assertFalse(self.driver.find_element_by_xpath(
            # "(/html/body/div[3]/div/div/div[2]/div[8]/label/input)").is_selected())
            # except AssertionError as e:
            # self.verificationErrors.append(str(e))

        elif ermittlung_type == "1000":
            WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
                (By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)"), u"Ermittlung der Selbstbeteiligung (Start-SB)"))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, "(/html/body/div[3]/div/div/div[2]/div[9]/label/input)")))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, "(/html/body/div[3]/div/div/div[2]/div[9]/label/input)")))
            # try:
            # self.assertFalse(self.driver.find_element_by_xpath(
            # "(/html/body/div[3]/div/div/div[2]/div[9]/label/input)").is_selected())
            # except AssertionError as e:
            # self.verificationErrors.append(str(e))

        if selected_radio_no is not None:
            self.check_and_click_element_by_xpath(
                "(/html/body/div[3]/div/div/div[2]/div[%d]/label)" % (selected_radio_no + 3))

        if is_checkbox_checked != "unchecked":
            if ermittlung_type == "400":
                self.check_and_click_element_by_xpath("(/html/body/div[3]/div/div/div[2]/div[8]/label)")
            elif ermittlung_type == "1000":
                self.check_and_click_element_by_xpath("(/html/body/div[3]/div/div/div[2]/div[11]/label/input)")

        if button_to_click == "abbrechen":
            self.check_and_click_element_by_xpath(self.TARIFDATEN_SB_POPUP_ABBRECHEN_BUTTON_XPATH)
            WebDriverWait(self.driver, 4).until(EC.invisibility_of_element_located(
                (By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))

        elif button_to_click == "ubernahmen":
            self.check_and_click_element_by_xpath("(/html/body/div[3]/div/div/div[3]/div/div[3]/button)")

            # if selected_radio_no == None or is_checkbox_checked == "unchecked":
            # try:
            # WebDriverWait(self.driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
            # except AssertionError as e:
            # self.verificationErrors.append(str(e))
            #
            #
            #
            WebDriverWait(self.driver, 4).until(EC.invisibility_of_element_located(
                (By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
            self.tarifdaten_wait_for_price_reload()
            produkt_radios = self.driver.find_elements_by_xpath(
                self.TARIFDATEN_PRODUKT_ELEMENTS_INPUTS_RECHTSCHUTZ_XPATH)
            for i in produkt_radios:
                if i.is_selected():
                    if ermittlung_type == "400":
                        try:
                            self.assertEqual(self.TARIFDATEN_SB_POPUP_SB_400[selected_radio_no - 1],
                                             Select(self.driver.find_element_by_xpath(
                                                 "(.//*[@id='rechner-section']/div/div[2]/div/div[3]/div[1]/div/div/div[2]/table[1]/tbody/tr[%d]/td[last()-1]/select)" % (
                                                     produkt_radios.index(i) + 1))).first_selected_option.text)
                        except AssertionError as e:
                            self.verificationErrors.append(
                                ermittlung_type + "," + str(
                                    selected_radio_no) + "," + is_checkbox_checked + ": " + str(
                                    e))
                    if ermittlung_type == "1000":
                        try:
                            self.assertEqual(self.TARIFDATEN_SB_POPUP_SB_1000[selected_radio_no - 1],
                                             Select(self.driver.find_element_by_xpath(
                                                 "(.//*[@id='rechner-section']/div/div[2]/div/div[3]/div[1]/div/div/div[2]/table[1]/tbody/tr[%d]/td[11]/select)" % (
                                                     produkt_radios.index(i) + 1))).first_selected_option.text)
                        except AssertionError as e:
                            self.verificationErrors.append(
                                ermittlung_type + "," + str(
                                    selected_radio_no) + "," + is_checkbox_checked + ": " + str(
                                    e))
                            #
                            # if button_to_click == "abbrechen":
                            # self.check_and_click_element_by_xpath(self.TARIFDATEN_SB_POPUP_ABBRECHEN_BUTTON_XPATH)

    def tarifdaten_ermittlung_popup_abbrechen_click(self):
        self.check_and_click_element_by_xpath(self.TARIFDATEN_SB_POPUP_ABBRECHEN_BUTTON_XPATH)
        WebDriverWait(self.driver, 4).until(EC.invisibility_of_element_located(
            (By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
        self.tarifdaten_wait_for_price_reload()

    def tarifdaten_erganzungen_popup_ok_click(self):
        self.check_and_click_element_by_xpath(Helper.ERGANZUNGEN_POPUP_OK_BUTTON_XPATH)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, Helper.ERGANZUNGEN_POPUP_PRODUKT_LABELS_XPATH)))
        self.tarifdaten_wait_for_price_reload()

    def tarifdaten_weiter_antrastellerdaten(self, hide_menu=True):
        self.check_and_click_element_by_link_text("Weiter")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[1])")),
            "Antragstellerdaten page not reached")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[1])")))
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[1]/div/div/div[1])"),
            u"Produktauswahl"))
        self.assertEqual(self.base_url + "ng/#/taa//antragsteller", self.driver.current_url)

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.ANTRAGSTELLERDATEN_SECTION_HEADER_XPATH)))
        self.assertEqual("Antragstellerdaten", self.driver.find_element_by_xpath(
            self.ANTRAGSTELLERDATEN_SECTION_HEADER_XPATH).text)
        if hide_menu:
            self.hide_drop_down_menu()

    def tarifdaten_check_text_in_produkt_table(self, text, table_name, row_no):
        if table_name == "erganzungen":
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH,
                 "(/html/body/div/div/div/section/div/div[2]/div/div[5]/div/div/div[2]/table/tbody/tr[1]/td[2]/div/div)")))

            try:
                self.assertEqual(text, self.driver.find_element_by_xpath(
                    "(/html/body/div/div/div/section/div/div[2]/div/div[5]/div/div/div[2]/table/tbody/tr[" + str(
                        row_no) + "]/td[2]/div/div)").text)
            except AssertionError as e:
                self.verificationErrors.append(str(e), text + " not present in %s table" % table_name)

    def tarifdaten_check_price_in_produkt_table(self, text, table_name, row_no):
        if table_name == "rechtschutz":
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH,
                 "(/html/body/div/div/div/section/div/div[2]/div/div[5]/div/div/div[2]/table/tbody/tr[1]/td[2]/div/div)")))

            try:
                self.assertEqual(text, self.driver.find_element_by_xpath(
                    self.get_tarifdaten_produkt_table_price_elements_xpath(row_no)).text)
            except AssertionError as e:
                self.verificationErrors.append(str(e), text + " not present in %s table" % table_name)

    def tarifdaten_select_zahlweise(self, zahlweise):
        gesambtr_text = self.driver.find_element_by_xpath(self.TARIFDATEN_GESAMTBTR_LABEL_XPATH).text
        self.check_and_click_element_by_xpath(self.TARIFDATEN_ZAHLWEISE_INPUTS_XPATH[zahlweise]["radio_xpath"])
        WebDriverWait(self.driver, 20).until_not(EC.text_to_be_present_in_element_value((By.XPATH,
                                                                                         self.TARIFDATEN_GESAMTBTR_LABEL_XPATH),
                                                                                        gesambtr_text))

    # endregion
    # region antragstellerdaten common tasks

    def antragsteller_zuruck_tarifdaten(self, hide_menu=True):
        self.check_and_click_element_by_link_text(u"Zurück")

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, "(.//*[@id='rechner-section']/div/div[2]/div/div[1]/div/div/div[1]/h4)")))
        self.assertEqual("Zielgruppe", self.driver.find_element_by_xpath(
            "(.//*[@id='rechner-section']/div/div[2]/div/div[1]/div/div/div[1]/h4)").text)
        self.assertEqual(self.base_url + "ng/#/taa//tarifdaten", self.driver.current_url)

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, "rechtschutz")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "rechtschutz")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, "schutzbrief")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "schutzbrief")))
        self.assertEqual(self.base_url + "ng/#/taa//tarifdaten", self.driver.current_url)
        if hide_menu:
            self.hide_drop_down_menu()
        self.tarifdaten_wait_for_price_reload()

    def antragsteller_weiter_zusatzdaten(self, hide_menu=True):
        self.zusatzdaten_fill_required_fields()
        self.check_and_click_element_by_link_text(u"Weiter")

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[1]/div/div/div[1])")),
            "Zusatzdaten page not reached")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[1]/div/div/div[1])")))
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[1]/div/div/div[1])"),
            u"Produktauswahl"))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/h4)")),
            "Zusatzdaten page not reached")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/h4)")))
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/h4)"),
            u"Vertragsbeginn"))
        self.assertEqual(self.base_url + "ng/#/taa//zusatzdaten", self.driver.current_url)
        if hide_menu:
            self.hide_drop_down_menu()

    def zusatzdaten_weiter_antrag(self, hide_menu=True):
        self.zusatzdaten_fill_required_fields()
        self.check_and_click_element_by_link_text(u"Weiter")

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self.ANTRAG_ZUSATZDATEN_HEADER)),
            "Antrag page not reached")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, self.ANTRAG_ZUSATZDATEN_HEADER)))
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.ANTRAG_ZUSATZDATEN_HEADER),
            u"Zusatzdaten"))
        self.assertEqual(self.base_url + "ng/#/taa//antrag", self.driver.current_url)
        if hide_menu:
            self.hide_drop_down_menu()

    def zusatzdaten_zuruck_antrastellerdaten(self, hide_menu=True):
        self.check_and_click_element_by_link_text(u"Zurück")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[1])")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[1])")))
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[1]/div/div/div[1])"),
            u"Produktauswahl"))
        self.assertEqual(self.base_url + "ng/#/taa//antragsteller", self.driver.current_url)
        if hide_menu:
            self.hide_drop_down_menu()

    def antrag_zuruck_zusatzdaten(self, hide_menu=True):
        self.check_and_click_element_by_link_text(u"Zurück")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[1]/div/div/div[1])")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[1]/div/div/div[1])")))
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[1]/div/div/div[1])"),
            u"Produktauswahl"))
        self.assertEqual(self.base_url + "ng/#/taa//zusatzdaten", self.driver.current_url)
        if hide_menu:
            self.hide_drop_down_menu()

    def check_if_on_bestatigung_page(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[1]/div/div/div[1]/h4)")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[1]/div/div/div[1]/h4)")))
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[1]/div/div/div[1]/h4)"),
            u"Sendebestätigung"))
        self.assertEqual(self.base_url + "ng/#/taa//bestaetigung", self.driver.current_url)
        self.hide_drop_down_menu()

    def antragsteller_fill_data(self):
        self.antragsteller_fill_data_antragstellerdaten()
        self.antragsteller_fill_data_zahlungsdaten("lastschrift")
        self.antragsteller_fill_data_vorversicherung("nein")

    def antragsteller_fill_data_antragstellerdaten(self, taetigkeit="nichtselbständig",
                                                   berufsgruppe="Berufs-/Lizenzsportler / -trainer"):
        Select(self.driver.find_element_by_id("anrede")).select_by_visible_text("Herr")
        self.driver.find_element_by_id("name").clear()
        self.driver.find_element_by_id("name").send_keys(u"NameTEST")
        self.driver.find_element_by_id("vorname").clear()
        self.driver.find_element_by_id("vorname").send_keys(u"VornameTEST")
        self.driver.find_element_by_id("strasse").clear()
        self.driver.find_element_by_id("strasse").send_keys(u"StrasseTEST")
        self.driver.find_element_by_id("hausnummer").clear()
        self.driver.find_element_by_id("hausnummer").send_keys(u"12a")
        self.driver.find_element_by_id("plz").clear()
        self.driver.find_element_by_id("plz").send_keys(u"12345")
        self.driver.find_element_by_id("ort").clear()
        self.driver.find_element_by_id("ort").send_keys(u"OrtTEST")
        self.driver.find_element_by_id("geburtsdatum").clear()
        Select(self.driver.find_element_by_id("taetigkeit")).select_by_visible_text(taetigkeit)
        if taetigkeit != "nicht berufstätig":
            Select(self.driver.find_element_by_id("berufsgruppe")).select_by_visible_text(berufsgruppe)
        self.driver.find_element_by_id("geburtsdatum").send_keys("11.06.1958")

    def antragsteller_fill_data_kontaktdaten(self):
        self.driver.find_element_by_id("telefon").clear()
        self.driver.find_element_by_id("telefon").send_keys(u"49-500-300-500")
        self.driver.find_element_by_id("mobil").clear()
        self.driver.find_element_by_id("mobil").send_keys(u"49-666-777-666")
        self.driver.find_element_by_id("fax").clear()
        self.driver.find_element_by_id("fax").send_keys(u"49-888-999-888")
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys(u"email@domain.de")

    def antragsteller_fill_data_lebenspartner(self, selected_radiobutton="ja", anschrift="nein",
                                              taetigkeit="nichtselbständig",
                                              berufsgruppe="Berufs-/Lizenzsportler / -trainer"):

        if selected_radiobutton == "ja":
            self.check_and_click_element_by_xpath(self.ANTRAGSTELLER_LEBENSPARTNER_J_N_HELPER["ja"]["label_xpath"])
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "lebenspartner-anrede")))
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "lebenspartner-anrede")))
            # self.driver.find_element_by_id("lebenspartner-anrede").click()
            Select(self.driver.find_element_by_id("lebenspartner-anrede")).select_by_visible_text("Herr")
            Select(self.driver.find_element_by_id("lebenspartner-titel")).select_by_visible_text("Dr.")
            self.driver.find_element_by_id("lebenspartner-name").clear()
            self.driver.find_element_by_id("lebenspartner-name").send_keys(u"LebensNameTEST")
            self.driver.find_element_by_id("lebenspartner-vorname").clear()
            self.driver.find_element_by_id("lebenspartner-vorname").send_keys(u"LebensVornameTEST")
            self.driver.find_element_by_id("lebenspartner-geburtsdatum").clear()

            Select(self.driver.find_element_by_id("lebenspartner-taetigkeit")).select_by_visible_text(taetigkeit)
            Select(self.driver.find_element_by_id("lebenspartner-berufsgruppe")).select_by_visible_text(berufsgruppe)
            self.driver.find_element_by_id("lebenspartner-geburtsdatum").send_keys("22.04.1985")

        elif selected_radiobutton == "nein":
            self.check_and_click_element_by_xpath(
                self.ANTRAGSTELLER_LEBENSPARTNER_J_N_HELPER["nein"]["label_xpath"])

    def antragsteller_fill_data_zahlungsdaten(self, zahlungsart="lastschrift", iban="DE88300606010301156608", bic=None):
        if zahlungsart == "lastschrift":
            self.check_and_click_element_by_name("zahlungsart")
            self.check_and_click_element_by_xpath(
                self.ANTRAGSTELLER_ZAHLUNGSDATEN_ZAHLUNGSART_HELPER["lastschrift"]["radio_xpath"])
            self.driver.find_element_by_id("iban").send_keys(iban)
            if bic is not None:
                self.driver.find_element_by_id("bic").send_keys(bic)

        elif zahlungsart == "uberweisung":
            self.check_and_click_element_by_xpath(
                self.ANTRAGSTELLER_ZAHLUNGSDATEN_ZAHLUNGSART_HELPER["uberweisung"]["label_xpath"])
            self.check_and_click_element_by_xpath(
                self.ANTRAGSTELLER_ZAHLUNGSDATEN_ZAHLUNGSART_HELPER["uberweisung"]["radio_xpath"])

    def antragsteller_fill_data_vorversicherung(self, selected_radiobutton="nein"):
        if selected_radiobutton == "ja":
            self.check_and_click_element_by_name("vorverischerung")

            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "gesellschaft")))
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "gesellschaft")))
            self.driver.find_element_by_id("gesellschaft").click()
            SelectWithFooterSlide(self.driver.find_element_by_id("gesellschaft"),
                                  self.driver).select_by_visible_text("BVB")
            self.driver.find_element_by_id("versicherungsscheinnummer").send_keys(u"696969")
            self.driver.find_element_by_id("lebenspartner-name").send_keys(u"LebensNameTEST")
            self.driver.find_element_by_id("gekundig").click()
            SelectWithFooterSlide(self.driver.find_element_by_id("gekundig"),
                                  self.driver).select_by_visible_text("Versicherungsnehmer")
            self.driver.find_element_by_id("beginn").send_keys(u"11.07.2008")
            self.driver.find_element_by_id("ende").send_keys(u"15.06.2016")
            self.driver.find_element_by_id("versicherungsnehmer").send_keys(u"787878")
            self.driver.find_element_by_id("versicherungsumfang").send_keys(u"TESTumfang")

        elif selected_radiobutton == "nein":
            self.check_and_click_element_by_xpath(
                self.ANTRAGSTELLER_VORVERSICHERUNG_J_N_HELPER["nein"]["radio_xpath"])

    def antragsteller_check_default_antragstellerdaten(self):
        try:
            self.assertTrue(self.driver.find_element_by_id("anrede").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual("", Select(self.driver.find_element_by_id("anrede")).first_selected_option.text)
        except AssertionError as e:
            self.verificationErrors.append(str(e) + " Anrede combo: %s instead of %s" % (
                Select(self.driver.find_element_by_id("anrede")).first_selected_option.text,
                ""))
        try:
            self.assertTrue(self.driver.find_element_by_id("titel").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual("", Select(self.driver.find_element_by_id("titel")).first_selected_option.text)
        except AssertionError as e:
            self.verificationErrors.append(str(e) + " Titel combo: %s instead of %s" % (
                Select(self.driver.find_element_by_id("titel")).first_selected_option.text,
                ""))

        try:
            self.assertTrue(self.driver.find_element_by_id("name").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("name").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("vorname").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("vorname").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("strasse").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("strasse").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("hausnummer").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("hausnummer").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("plz").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("plz").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("ort").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("ort").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("geburtsdatum").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("geburtsdatum").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("taetigkeit").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual("", Select(self.driver.find_element_by_id("taetigkeit")).first_selected_option.text)
        except AssertionError as e:
            self.verificationErrors.append(str(e) + " Taetigkeit combo: %s instead of %s" % (
                Select(self.driver.find_element_by_id("taetigkeit")).first_selected_option.text,
                ""))
        try:
            self.assertTrue(self.driver.find_element_by_id("berufsgruppe").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual("", Select(self.driver.find_element_by_id("berufsgruppe")).first_selected_option.text)
        except AssertionError as e:
            self.verificationErrors.append(str(e) + " Berufsgruppe combo: %s instead of %s" % (
                Select(self.driver.find_element_by_id("berufsgruppe")).first_selected_option.text,
                ""))

    def antragsteller_check_default_kontaktdaten(self):
        try:
            self.assertTrue(self.driver.find_element_by_id("telefon").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("telefon").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("mobil").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("mobil").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("fax").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("fax").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("email").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("email").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def antragsteller_check_default_lebenspartner(self):
        self.assertTrue(self.driver.find_element_by_xpath(
            self.ANTRAGSTELLER_LEBENSPARTNER_J_N_HELPER["ja"]["radio_xpath"]).is_selected())

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "lebenspartner-anrede")))
        try:
            self.assertEqual("",
                             Select(self.driver.find_element_by_id("lebenspartner-anrede")).first_selected_option.text)
        except AssertionError as e:
            self.verificationErrors.append(str(e) + " lebenspartner-anrede combo: %s instead of %s" % (
                Select(self.driver.find_element_by_id("lebenspartner-anrede")).first_selected_option.text,
                ""))

        try:
            self.assertTrue(self.driver.find_element_by_id("lebenspartner-titel").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual("",
                             Select(self.driver.find_element_by_id("lebenspartner-titel")).first_selected_option.text)
        except self.AssertionError as e:
            self.verificationErrors.append(str(e) + " lebenspartner-titel combo: %s instead of %s" % (
                Select(self.driver.find_element_by_id("lebenspartner-titel")).first_selected_option.text,
                ""))

        try:
            self.assertTrue(self.driver.find_element_by_id("lebenspartner-name").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("lebenspartner-name").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("lebenspartner-vorname").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("lebenspartner-vorname").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("lebenspartner-geburtsdatum").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("lebenspartner-geburtsdatum").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("lebenspartner-taetigkeit").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual("", Select(
                self.driver.find_element_by_id("lebenspartner-taetigkeit")).first_selected_option.text)
        except AssertionError as e:
            self.verificationErrors.append(str(e) + " lebenspartner-taetigkeit combo: %s instead of %s" % (
                Select(self.driver.find_element_by_id("lebenspartner-taetigkeit")).first_selected_option.text,
                ""))

        try:
            self.assertTrue(self.driver.find_element_by_id("lebenspartner-berufsgruppe").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual("", Select(
                self.driver.find_element_by_id("lebenspartner-berufsgruppe")).first_selected_option.text)
        except AssertionError as e:
            self.verificationErrors.append(str(e) + " lebenspartner-berufsgruppe combo: %s instead of %s" % (
                Select(self.driver.find_element_by_id("lebenspartner-berufsgruppe")).first_selected_option.text,
                ""))

    def antragsteller_check_default_zahlungsdaten(self):
        try:
            self.assertTrue(self.driver.find_element_by_xpath(
                self.ANTRAGSTELLER_ZAHLUNGSDATEN_ZAHLUNGSART_HELPER["lastschrift"]["radio_xpath"]).is_selected())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ lastschrifft not selected")
        try:
            self.assertFalse(self.driver.find_element_by_xpath(
                self.ANTRAGSTELLER_ZAHLUNGSDATEN_ZAHLUNGSART_HELPER["uberweisung"]["radio_xpath"]).is_selected())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ uberweisung selected")

        self.check_and_click_element_by_xpath(
            self.ANTRAGSTELLER_ZAHLUNGSDATEN_ZAHLUNGSART_HELPER["uberweisung"]["radio_xpath"])

        try:
            self.assertTrue(self.driver.find_element_by_xpath(
                self.ANTRAGSTELLER_ZAHLUNGSDATEN_ZAHLUNGSART_HELPER["uberweisung"]["radio_xpath"]).is_selected())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ uberweisung not selected")

        try:
            self.assertFalse(self.driver.find_element_by_id("iban").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ iban")

        try:
            self.assertFalse(self.driver.find_element_by_id("bic").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ bic")

        try:
            self.assertFalse(self.driver.find_element_by_xpath(
                self.ANTRAGSTELLER_ZAHLUNGSDATEN_KONTOINHABER_HELPER["versicherungsnehmer"][
                    "label_xpath"]).is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ VERSICHERUNGSNEHMER_LABEL")

        self.check_and_click_element_by_xpath(
            self.ANTRAGSTELLER_ZAHLUNGSDATEN_ZAHLUNGSART_HELPER["lastschrift"]["radio_xpath"])

        try:
            self.assertTrue(self.driver.find_element_by_xpath(
                self.ANTRAGSTELLER_ZAHLUNGSDATEN_ZAHLUNGSART_HELPER["lastschrift"]["radio_xpath"]).is_selected())
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertTrue(self.driver.find_element_by_id("iban").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ iban")
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("iban").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("bic").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ bic")
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("bic").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_xpath(
                self.ANTRAGSTELLER_ZAHLUNGSDATEN_INSTITUT_FORM_XPATH).is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_xpath(
                self.ANTRAGSTELLER_ZAHLUNGSDATEN_KONTOINHABER_HELPER["versicherungsnehmer"][
                    "radio_xpath"]).is_selected())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ VERSICHERUNGSNEHMER_INPUT")
        try:
            self.assertFalse(self.driver.find_element_by_xpath(
                self.ANTRAGSTELLER_ZAHLUNGSDATEN_ANDERER_INHABER_ANREDE_COMBO_XPATH).is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ ANDERER_INHABER_ANREDE_COMBO")

        self.check_and_click_element_by_xpath(
            self.ANTRAGSTELLER_ZAHLUNGSDATEN_KONTOINHABER_HELPER["anderer"]["label_xpath"])

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "kontoinhaber-anrede")))
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "kontoinhaber-anrede")))
        try:
            self.assertEqual("",
                             Select(self.driver.find_element_by_id("kontoinhaber-anrede")).first_selected_option.text)
        except AssertionError as e:
            self.verificationErrors.append(str(e) + " kontoinhaber-anrede combo: %s instead of %s" % (
                Select(self.driver.find_element_by_id("kontoinhaber-anrede")).first_selected_option.text,
                ""))

        try:
            self.assertTrue(self.driver.find_element_by_id("kontoinhaber-titel").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ kontoinhaber-titel")
        try:
            self.assertEqual("",
                             Select(self.driver.find_element_by_id("kontoinhaber-titel")).first_selected_option.text)
        except AssertionError as e:
            self.verificationErrors.append(str(e) + " kontoinhaber-titel combo: %s instead of %s" % (
                Select(self.driver.find_element_by_id("kontoinhaber-titel")).first_selected_option.text,
                ""))

        try:
            self.assertTrue(self.driver.find_element_by_id("kontoinhaber-name").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ kontoinhaber-name")
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("kontoinhaber-name").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ kontoinhaber-name")

        try:
            self.assertTrue(self.driver.find_element_by_id("kontoinhaber-vorname").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ kontoinhaber-vorname")
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("kontoinhaber-vorname").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ kontoinhaber-vorname")

        try:
            self.assertTrue(self.driver.find_element_by_id("kontoinhaber-strasse").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ kontoinhaber-strasse")
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("kontoinhaber-strasse").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ kontoinhaber-strasse")

        try:
            self.assertTrue(self.driver.find_element_by_id("kontoinhaber-hausnummer").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ kontoinhaber-hausnummer")
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("kontoinhaber-hausnummer").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ kontoinhaber-hausnummer")

        try:
            self.assertTrue(self.driver.find_element_by_id("kontoinhaber-ort").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ kontoinhaber-ort")
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("kontoinhaber-ort").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ kontoinhaber-ort")

        self.check_and_click_element_by_xpath(
            self.ANTRAGSTELLER_ZAHLUNGSDATEN_KONTOINHABER_HELPER["versicherungsnehmer"]["label_xpath"])

        WebDriverWait(self.driver, 10).until_not(
            EC.visibility_of_element_located((By.ID, "kontoinhaber-anrede")))

        self.check_and_click_element_by_xpath(
            self.ANTRAGSTELLER_ZAHLUNGSDATEN_ZAHLUNGSART_HELPER["uberweisung"]["label_xpath"])

        WebDriverWait(self.driver, 10).until_not(
            EC.visibility_of_element_located((By.ID, "iban")))

    def antragsteller_check_default_vorversicherung(self):
        try:
            self.assertTrue(self.driver.find_element_by_xpath(
                self.ANTRAGSTELLER_VORVERSICHERUNG_J_N_HELPER["ja"]["radio_xpath"]).is_selected())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ vorversicherung")

        try:
            self.assertTrue(self.driver.find_element_by_id("gesellschaft").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ gesellschaft")
        try:
            self.assertEqual("", Select(self.driver.find_element_by_id("gesellschaft")).first_selected_option.text)
        except AssertionError as e:
            self.verificationErrors.append(str(e) + " gesellschaft combo: %s instead of %s" % (
                Select(self.driver.find_element_by_id("gesellschaft")).first_selected_option.text,
                ""))
        try:
            self.assertTrue(self.driver.find_element_by_id("versicherungsscheinnummer").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ versicherungsscheinnummer")
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("versicherungsscheinnummer").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("gekundig").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ gekundig")
        try:
            self.assertEqual("", Select(self.driver.find_element_by_id("gekundig")).first_selected_option.text)
        except AssertionError as e:
            self.verificationErrors.append(str(e) + " gekundig combo: %s instead of %s" % (
                Select(self.driver.find_element_by_id("gekundig")).first_selected_option.text,
                ""))

        try:
            self.assertTrue(self.driver.find_element_by_id("beginn").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ beginn")
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("beginn").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("ende").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ ende")
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("ende").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.driver.find_element_by_id("versicherungsumfang").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ versicherungsumfang")
        try:
            self.assertEqual(u"", self.driver.find_element_by_id("versicherungsumfang").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    # endregion
    # region antrag common tasks
    def zusatzdaten_fill_required_fields(self):
        required_inputs = self.driver.find_elements_by_xpath(self.ZUSATZDATEN_REQUIERD_INPUTS)

        if len(required_inputs) > 0:
            for input_element in required_inputs:
                if input_element.is_displayed() and input_element.is_enabled():
                    input_element.send_keys("10")

        required_selects = self.driver.find_elements_by_xpath(self.ZUSATZDATEN_REQUIERD_SELECTS)

        if len(required_selects) > 0:
            for select_element in required_selects:
                if select_element.is_displayed() and select_element.is_enabled():
                    Select(select_element).select_by_index(1)

    # endregion

    # region documents common tasks
    def documents_popup_generate_document(self, document_name):
        self.check_and_click_element_by_link_text("PDF erstellen")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
        self.wait_for_pdf_spinner()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "(/html/body/div[3]/div/div/div[2]/descendant::label)")))

        documents_label_list = self.driver.find_elements_by_xpath(
            "(/html/body/div[3]/div/div/div[2]/descendant::label[@data-ng-show=\"doc.IsVisible\"])")

        for i in documents_label_list:
            if i.text != u'' and i.text in document_name:
                i.click()

        self.check_and_click_element_by_xpath("(/html/body/div[3]/div/div/div[3]/div/div[3]/button)")
        # endregion

    def antrag_antragsteller_check_text(self, text):
        if self.get_antrag_antragsteller_text(text) is not None:
            return True
        else:
            return False
