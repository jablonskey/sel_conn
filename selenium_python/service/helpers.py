# -*- coding: utf-8 -*-
import re
import sys

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0


class Helper(object):
    def __init__(self, driver):
        self.driver = driver

    VERMITTLER_LOGIN_PAGE_ADDRESS_COMPLETION = "ng/#/vermittler/login"
    ADMIN_LOGIN_PAGE_ADDRESS_COMPLETION = "ng/#/admin/login"
    AKTSERVICE_LOGIN_PAGE_ADDRES_COMPLETION = "ng/#/aktualisierung/login"
    SECURE_EMAIL_LOGIN_PAGE_ADDRES_COMPLETION = "ng/#/dokumente/login"

    # for deep links
    STARTSEITE_ADDRES_COMPLETION = "ng/#/vermittler/startseite"
    ZIELGRUPPE_ADDRES_COMPLETION = "ng/#/taa//zielgruppe"
    KUNDENSUCHE_ADDRES_COMPLETION = "ng/#/vermittler/kundensuche"
    MITGLIEDSCHAFT_ADDRES_COMPLETION = "ng/#/vermittler/mitgliedschaft/"
    MEINE_ANGEBOTE_ADDRES_COMPLETION = "ng/#/vermittler/angebote"
    MEIN_PROFIL_ADDRESS_COMPLETION = "ng/#/vermittler/nutzerprofil"

    ADMIN_USER_LOGIN = "admin@ks"
    ADMIN_USER_PASSWORD = "dupa"

    VERMITTLER_USER_LOGIN = "test@ks"
    VERMITTLER_USER_PASSWORD = "Aa111111"

    AKTSERVICE_USER_LOGIN = "3092998800"
    AKTSERVICE_USER_PASSWORD = "85622"

    SECURE_EMAIL_USER_LOGIN = "ses_test@ks"
    SECURE_EMAIL_USER_PASSWORD = "Aa111111"

    ERGEBNIS_OPTIONEN_SPEICHERN_UNTER_LINK_XPATH = "(//ergebnis-optionen/div/a[2])"

    VERMITTLER_LOGIN_BUTTON_XPATH = "(/html/body/div/div/div/section/div/div[2]/form/button)"
    VERMITTLER_IFRAME_ANMELDEN_XPATH = "(.//*[@id='login'])"
    VERMITTLER_IFRAME_ABMELDEN_XPATH = "(.//*[@id='logout'])"

    ADMIN_LOGIN_BUTTON_XPATH = "(/html/body/div/div/div/section/div/div[2]/form/button)"
    ADMIN_LOGOUT_LINK_XPATH = "(/html/body/header/div/div/div[2]/ul/li/a)"

    AKTSERVICE_LOGIN_BUTTON_XPATH = "(/html/body/div/div/div/section/div/div[2]/form/button)"
    AKTSERVICE_LOGOUT_LINK_XPATH = "(/html/body/header/div/div/div[2]/ul/li/a)"

    ADMIN_IFRAME_LOGIN_XPATH = "(/html/body/div/div[1]/ul[2]/li/a)"
    ADMIN_IFRAME_LOGOUT_XPATH = "(/html/body/div[1]/div[1]/ul[1]/li[2]/a)"

    SECURE_EMAIL_LOGIN_BUTTON_XPATH = "(/html/body/div/div/div/section/div/div[2]/form/button)"

    ADMIN_BENUTZER_ANLEGEN_BUTTON_XPATH = "(/html/body/div/div/div/section/div/div[2]/div[1]/a)"

    BENUTZER_ANLEGEN_BENUTZERROLLE_COMBO_XPATH = "(/html/body/div/div/div/section/div/div[2]/form/div[1]/div/div/table/tbody/tr/td[2]/select"

    FOOTER_SPAN_XPATH = "(/html/body/span)"

    CURRENT_PAGE_MAIN_HEADER = "(/html/body/div/div/div/div[2]/div[1]/ng-include/h1|html/body/div/div/div/div/div/ng-include/h1)"

    NEUE_DOKUMENTE_PAGINATION_XPATH = "(/html/body/div/div/div/section/div/div[2]/div/div[1]/div/div/ul)"

    ZIELGRUPPE_PAGE_ADDRESS_COMPLETION = "ng/#/taa//zielgruppe"
    ZIELGRUPPE_PRIVATKUNDEN_HEADER_XPATH = "(/html/body/div/div/div/section/div/div[2]/div/form/div/div[1]/div/div[1]/h4)"
    ZIELGRUPPE_GESCHAFTSKUNDEN_XPATH = "(/html/body/div/div/div/section/div/div[2]/div/form/div/div[2]/div/div[1]/h4)"
    ZIELGRUPPE_ELEMENTS_LABELS_XPATH = "(/html/body/div[1]/div/div/section/div/div[2]/div/form[1]/div/div[*]/div/div[2]/div/div[*]/label)"
    ZIELGRUPPE_ELEMENTS_INPUTS_XPATH = "(/html/body/div[1]/div/div/section/div/div[2]/div/form[1]/div/div[*]/div/div[2]/div/div[*]/label/input)"

    ZIELGRUPPE_VMNR_COMBO_BEFORE_CLICK_XPATH = "(.//*[@id='berechnen-fur']/div/span)"
    ZIELGRUPPE_VMNR_COMBO_FORM_CLICK_XPATH = "(.//*[@id='berechnen-fur']/input[1])"
    ZIELGRUPPE_VMNR_COMBO_FORM_AFTER_CLICK_XPATH = "(.//*[@id='berechnen-fur']/div/span/span[2]/span)"

    ZIELGRUPPE_VMNR_COMBO_WARNING_XPATH = "(/html/body/div/div/div/section/div/div[2]/div/div[1]/div/div/div/div[2]/div/p)"
    ZIELGRUPPE_ANON_VMNR_FORM_XPATH = "(.//*[@id='enter-vmnr'])"

    ZIELGRUPPE_BETRIEBSFLAECHE_FORM_XPATH = "(/html/body/div/div/div/section/div/div[2]/div/div[5]/div/form/div/div[2]/div[2]/div/input)"
    ZIELGRUPPE_ANZAHL_BESCHAEFTIGEN_SELBSTAENDIGE_FORM_XPATH = "(/html/body/div/div/div/section/div/div[2]/div/div[3]/div/form/div/div[2]/div[2]/div[2]/input)"

    ZIELGRUPPE_BTRKLASSES_HELPER_LIST = {
        "familien": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[1]/div/div[2]/div/div[1]/label)",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[1]/div/div[2]/div/div[1]/label/input)",
            "header_text": "Familien"},
        "singles": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[1]/div/div[2]/div/div[2]/label)",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[1]/div/div[2]/div/div[2]/label/input)",
            "header_text": "Singles"},
        "beamte": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[1]/div/div[2]/div/div[3]/label)",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[1]/div/div[2]/div/div[3]/label/input)",
            "header_text": "Beamte"},
        "senioren": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[1]/div/div[2]/div/div[4]/label)",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[1]/div/div[2]/div/div[4]/label/input)",
            "header_text": "Senioren"},
        "selbstandige": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[2]/div/div[2]/div/div[1]/label)",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[2]/div/div[2]/div/div[1]/label/input)",
            "header_text": u"Selbständige / Firmen / Freiberufler",
            "header_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[2]/div/div[1]/h4)",
            "anzahl_form_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[2]/div/div[2]/span[1]/data-ng-form/div[1]/div/table/tbody/tr/td[2]/input)",
            "jahresbrutto_form_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[2]/div/div[2]/span[2]/data-ng-form/div[1]/div/table/tbody/tr/td[2]/input)"},
        "arzte": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[2]/div/div[2]/div/div[2]/label)",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[2]/div/div[2]/div/div[2]/label/input)",
            "header_text": u"Ärzte / Heilwesenberufe",
            "header_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[2]/div/div[1]/h4)",
            "form_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[2]/div/div[2]/span/data-ng-form/div[1]/div/table/tbody/tr/td[2]/input)"},
        "steuerberater": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[2]/div/div[2]/div/div[3]/label)",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[2]/div/div[2]/div/div[3]/label/input)",
            "header_text": u"Steuerberater / Wirtschaftsprüfer",
            "header_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[2]/div/div[1]/h4)",
            "form1_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[2]/div/div[2]/span[1]/data-ng-form/div[1]/div/table/tbody/tr/td[2]/input)",
            "form2_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[2]/div/div[2]/span[2]/data-ng-form/div[1]/div/table/tbody/tr/td[2]/input)"},
        "landwirte": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[2]/div/div[2]/div/div[4]/label)",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[2]/div/div[2]/div/div[4]/label/input)",
            "header_text": u"Landwirte",
            "header_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[2]/div/div[1]/h4)",
            "form_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[2]/div/div[2]/span/data-ng-form/div[2]/div/input)"},
        "vereine": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[2]/div/div[2]/div/div[5]/label)",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[1]/div/div[2]/div/div[2]/div/div[5]/label/input)",
            "header_text": u"Vereine",
            "header_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[2]/div/div[1]/h4)",
            "form_xpath": "(/html/body/div/div/div/section/div/div[2]/div/form[2]/div/div[2]/span/data-ng-form/div[1]/div/input)"}
    }

    ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER = {
        "vollzeitmitarbeiter": {"form_xpath": "(/html/body/div[3]/div/div/div[2]/form/div[1]/div/input)"},
        "teilzeitmitarbeiter": {"form_xpath": "(/html/body/div[3]/div/div/div[2]/form/div[2]/div/input)"},
        "auszubildende": {"form_xpath": "(/html/body/div[3]/div/div/div[2]/form/div[3]/div/input)"},
        "geringfugig": {"form_xpath": "(/html/body/div[3]/div/div/div[2]/form/div[4]/div/input)"},
        "saisonmitarbeiter": {"form_xpath": "(/html/body/div[3]/div/div/div[2]/form/div[5]/div/input)"},
        "heimarbeiter": {"form_xpath": "(/html/body/div[3]/div/div/div[2]/form/div[6]/div/input)"},
        "leiharbeiter ": {"form_xpath": "(/html/body/div[3]/div/div/div[2]/form/div[7]/div/input)"},
        "inhaber": {"form_xpath": "(/html/body/div[3]/div/div/div[2]/form/div[8]/div/input)"},
        "anzahl": {"form_xpath": "(/html/body/div[3]/div/div/div[2]/form/div[9]/div/div/input)"}
    }

    ZIELGRUPPE_LANDWIRTE_POPUP_LEFT_BUTTON_XPATH = "(/html/body/div[3]/div/div/div[3]/div/div[1]/button)"
    ZIELGRUPPE_LANDWIRTE_POPUP_RIGHT_BUTTON_XPATH = "(/html/body/div[3]/div/div/div[3]/div/div[3]/button)"
    ZIELGRUPPE_LANDWIRTE_INPUTS_XPATH = {
        "landwirte_mitglied_ja": {
            "radio_xpath": "(.//*[@id='rechner-section']/div/div[2]/div/form[2]/div/div[2]/span/data-ng-form/div[1]/div[1]/div[2]/div[1]/label/input)",
            "label_xpath": "(.//*[@id='rechner-section']/div/div[2]/div/form[2]/div/div[2]/span/data-ng-form/div[1]/div[1]/div[2]/div[1]/label)"
        },
        "landwirte_mitglied_nein": {
            "radio_xpath": "(.//*[@id='rechner-section']/div/div[2]/div/form[2]/div/div[2]/span/data-ng-form/div[1]/div[1]/div[2]/div[2]/label/input)",
            "label_xpath": "(.//*[@id='rechner-section']/div/div[2]/div/form[2]/div/div[2]/span/data-ng-form/div[1]/div[1]/div[2]/div[2]/label)"
        },
        "landwirte_gewerbe_ja": {
            "radio_xpath": "(.//*[@id='rechner-section']/div/div[2]/div/form[2]/div/div[2]/span/data-ng-form/div[1]/div[2]/div[2]/div[1]/label/input)",
            "label_xpath": "(.//*[@id='rechner-section']/div/div[2]/div/form[2]/div/div[2]/span/data-ng-form/div[1]/div[2]/div[2]/div[1]/label)"
        },
        "landwirte_gewerbe_nein": {
            "radio_xpath": "(.//*[@id='rechner-section']/div/div[2]/div/form[2]/div/div[2]/span/data-ng-form/div[1]/div[2]/div[2]/div[2]/label/input)",
            "label_xpath": "(.//*[@id='rechner-section']/div/div[2]/div/form[2]/div/div[2]/span/data-ng-form/div[1]/div[2]/div[2]/div[2]/label)"
        }

    }
    ZIELGRUPPE_LANDWIRTE_POPUP_XPATH = "(/html/body/div[3]/div/div)"
    ZIELGRUPPE_LANDWIRTE_BETRIEBSFLACHE_FORM_XPATH = "(.//*[@id='betriebsflaeche'])"

    PAGES_TABS_ELEMENTS_XPATH = "(/html/body/div[1]/div/div/section/div/div[2]/div/span/ul/li[*]/a)"

    ADMIN_SPINNER_XPATH = "(/html/body/div/div/div/section/div/div[2]/div[2]/table/div[*][contains(@class,\"cg-busy-animation\")])"

    NEUEDOKUMENTE_SPINNER_XPATH = "(/html/body/div[1]/div/div/section/div/div[2]/div[2]/div[2]/div[*][contains(@class,\"cg-busy-animation\")])"

    TARIFDATEN_SPINNER_XPATH = "(/html/body/div/div/div/section/div/div[2]/div/div[4]/div[last()][@class=\"cg-busy cg-busy-animation ng-scope\"])"

    PDF_ERSTELLEN_SPINNER_XPATH = "(/html/body/div[3]/div/div/div[2]/div[*][contains(@class,\"cg-busy-animation\")])"

    TARIFDATEN_PRODUKT_ELEMENTS_LABELS_MITGLIEDSCHAFT_XPATH = "(.//*[@id='rechner-section']/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[*]/td[1]/div/label)"
    TARIFDATEN_PRODUKT_ELEMENTS_LABELS_RECHTSCHUTZ_XPATH = "(.//*[@id='rechner-section']/div/div[2]/div/div[3]/div[1]/div/div/div[2]/table[1]/tbody/tr[*]/td[1]/div/label)"
    TARIFDATEN_PRODUKT_ELEMENTS_INPUTS_RECHTSCHUTZ_XPATH = "(.//*[@id='rechner-section']/div/div[2]/div/div[3]/div[1]/div/div/div[2]/table[1]/tbody/tr[*]/td[1]/div/label/input)"
    TARIFDATEN_PRODUKT_ELEMENTS_LABELS_ERGANZUNGEN_XPATH = "(.//*[@id='rechner-section']/div/div[2]/div/div[4]/div[1]/div/div/div[2]/table/tbody/tr[*]/td[1]/ng-include/div/label)"
    TARIFDATEN_PRODUKT_ELEMENTS_INPUTS_ERGANZUNGEN_XPATH = "(.//*[@id='rechner-section']/div/div[2]/div/div[4]/div[1]/div/div/div[2]/table/tbody/tr[*]/td[1]/ng-include/div/label/input)"
    TARIFDATEN_PRODUKT_ELEMENTS_LABELS_SCHUTZBRIEF_XPATH = "(.//*[@id='rechner-section']/div/div[2]/div/div[4]/div[2]/div/div/div[2]/table/tbody/tr[*]/td[1]/ng-include/div/label)"
    TARIFDATEN_PRODUKT_ELEMENTS_SB_COMBOS_RECHTSCHUTZ_XPATH = "(.//*[@id='rechner-section']/div/div[2]/div/div[4]/div[1]/div/div/div[2]/table[1]/tbody/tr[*]/td[8]/select)"
    TARIFDATEN_GESAMTBTR_LABEL_XPATH = "(.//*[@id='rechner-section']/div/div[2]/div/div[4]/div[*]/div/div/div[2]/div/div[3]/div/div)"

    TARIFDATEN_RECHTSCHUTZ_LABEL_XPATH = "(.//*[@id='rechner-section']/div/div[2]/div/div[4]/div[1]/div/div/div[1]/div/h4/label)"

    TARIFDATEN_ZAHLWEISE_INPUTS_XPATH = {
        "jahrlich": {
            "radio_xpath": "(.//*[@id='rechner-section']/div/div[2]/div/div[4]/div[*]/div/div/div[2]/div/div[2]/div/div/div[1]/div/label/input)",
            "label_xpath": "(.//*[@id='rechner-section']/div/div[2]/div/div[4]/div[*]/div/div/div[2]/div/div[2]/div/div/div[1]/div/label)",
            "text": u"jährlich: 27,00 €"},
        "halbjahrlich": {
            "radio_xpath": "(.//*[@id='rechner-section']/div/div[2]/div/div[4]/div[*]/div/div/div[2]/div/div[2]/div/div/div[2]/div/label/input)",
            "label_xpath": "(.//*[@id='rechner-section']/div/div[2]/div/div[4]/div[*]/div/div/div[2]/div/div[2]/div/div/div[2]/div/label",
            "text": u"jährlich: 27,00 €"},
        "vierteljahrlich": {
            "radio_xpath": "(.//*[@id='rechner-section']/div/div[2]/div/div[4]/div[*]/div/div/div[2]/div/div[2]/div/div/div[3]/div/label/input)",
            "label_xpath": "(.//*[@id='rechner-section']/div/div[2]/div/div[4]/div[*]/div/div/div[2]/div/div[2]/div/div/div[3]/div/label)",
            "text": u"jährlich: 27,00 €"},
        "monatlich": {
            "radio_xpath": "(.//*[@id='rechner-section']/div/div[2]/div/div[4]/div[*]/div/div/div[2]/div/div[2]/div/div/div[4]/div/label/input)",
            "label_xpath": "(.//*[@id='rechner-section']/div/div[2]/div/div[4]/div[*]/div/div/div[2]/div/div[2]/div/div/div[4]/div/label)",
            "text": u"jährlich: 27,00 €"}
    }

    TARIFDATEN_SB_POPUP_SB_400 = ("0 EUR fallend",
                                  "100 EUR fallend",
                                  "200 EUR fallend",
                                  "400 EUR fallend")
    TARIFDATEN_SB_POPUP_SB_1000 = ("300 EUR fallend",
                                   "400 EUR fallend",
                                   "500 EUR fallend",
                                   "600 EUR fallend",
                                   "700 EUR fallend",
                                   "800 EUR fallend",
                                   "1.000 EUR fallend")
    TARIFDATEN_SB_POPUP_ABBRECHEN_BUTTON_XPATH = "(/html/body/div[3]/div/div/div[3]/div/div[1]/button)"
    TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH = "(/html/body/div[3]/div/div/div[3]/div/div[3]/button)"
    TARIFDATEN_SB_POPUP_RADIOS_XPATH = "(/html/body/div[3]/div/div/div[2]/div[*]/label/input[@type='radio'])"

    PRODUKTAUSWAHL_ELEMENTS_LABEL_XPATH = "(/html/body/div[1]/div/div/section/div/div[2]/div/div[1]/div/div/div[2]/div/div[*]/div[1])"

    ANTRAGSTELLERDATEN_SECTIONS_HEADERS_XPATH = "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[*]/div/div[1])"

    ANTRAGSTELLERDATEN_SECTION_HEADER_XPATH = "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[1])"

    ANTRAGSTELLER_ANTRAGSTELLERDATEN_FORMS = {
        "anrede": {
            "xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[2]/form/div[1]/div[1]/select)"},
        "titel": {
            "xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[2]/form/div[1]/div[2]/select)"},
        "name": {
            "xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[2]/form/div[1]/div[3]/input)"},
        "vorname": {
            "xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[2]/form/div[1]/div[4]/input)"},
        "namenszusatz": {
            "xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[2]/form/div[1]/div[5]/input)"},
        "strasse": {
            "xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[2]/form/div[2]/div[1]/input)"},
        "hausnummer": {
            "xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[2]/form/div[2]/div[2]/input)"},
        "plz": {
            "xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[2]/form/div[2]/div[3]/input)"},
        "ort": {
            "xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[2]/form/div[2]/div[4]/input)"},
        "geburtsdatum": {
            "xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[2]/form/div[3]/div[1]/input)"},
        "taetigkeit": {
            "xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[2]/form/div[3]/div[2]/select)"},
        "berufsgruppe": {
            "xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div/div[2]/form/div[3]/div[3]/select)"}
    }

    ANTRAGSTELLER_LEBENSPARTNER_J_N_HELPER = {
        "ja": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/form/div/div/div[2]/div[1]/div/label[1])",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/form/div/div/div[2]/div[1]/div/label[1]/input)"},
        "nein": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/form/div/div/div[2]/div[1]/div/label[2])",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/form/div/div/div[2]/div[1]/div/label[2]/input)"}
    }

    ANTRAGSTELLER_LEBENSPARTNER_ABWEICHENDE_ANSCHRIFT_J_N_HELPER = {
        "ja": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/form/div/div/div[2]/div[4]/div/label[1])",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/form/div/div/div[2]/div[4]/div/label[1]/input)"},
        "nein": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/form/div/div/div[2]/div[4]/div/label[2])",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/form/div/div/div[2]/div[4]/div/label[2]/input)"}
    }

    ANTRAGSTELLER_ZAHLUNGSDATEN_ZAHLUNGSART_HELPER = {
        "lastschrift": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[3]/div/div[2]/form[1]/div/div/div[1]/label)",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[3]/div/div[2]/form[1]/div/div/div[1]/label/input)"},
        "uberweisung": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[3]/div/div[2]/form[1]/div/div/div[2]/label)",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[3]/div/div[2]/form[1]/div/div/div[2]/label/input)"}
    }

    ANTRAGSTELLER_ZAHLUNGSDATEN_KONTOINHABER_HELPER = {
        "versicherungsnehmer": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[3]/div/div[2]/form[2]/div[2]/div/div[1]/label)",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[3]/div/div[2]/form[2]/div[2]/div/div[1]/label/input)"},
        "anderer": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[3]/div/div[2]/form[2]/div[2]/div/div[2]/label)",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[3]/div/div[2]/form[2]/div[2]/div/div[2]/label/input)"}
    }

    ANTRAGSTELLER_VORVERSICHERUNG_J_N_HELPER = {
        "ja": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[1]/div/label[1])",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[1]/div/label[1]/input)"},
        "nein": {
            "label_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[1]/div/label[2])",
            "radio_xpath": "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[4]/div/div[2]/div[1]/div/label[2]/input)"}
    }

    ANTRAGSTELLER_ZAHLUNGSDATEN_INSTITUT_FORM_XPATH = "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[3]/div/div[2]/form[2]/div[1]/div[3]/input)"
    ANTRAGSTELLER_ZAHLUNGSDATEN_ANDERER_INHABER_ANREDE_COMBO_XPATH = "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[3]/div/div[2]/form[3]/div[1]/div[1]/select)"

    ANTRAG_ZUSATZDATEN_HEADER = "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/h4)"
    ANTRAG_ANTRAGSTELLER_JA_PARAGRAPH = "(.//*[@id='rechner-section']/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/p[2]/span[2])"
    ANTRAG_ANTRAGSTELLER_NEIN_PARAGRAPH = "(.//*[@id='rechner-section']/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/p[2]/span[1])"

    ANTRAG_LEBENSPARTNER_JA_PARAGRAPH = "(.//*[@id='rechner-section']/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/p[3]/span[2])"
    ANTRAG_LEBENSPARTNER_NEIN_PARAGRAPH = "(.//*[@id='rechner-section']/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/p[3]/span[1])"

    ZUSATZDATEN_REQUIERD_INPUTS = "(//*[@id='rechner-section']/div/div[2]/div/form/descendant::*/input[@required='required'])"
    ZUSATZDATEN_REQUIERD_SELECTS = "(//*[@id='rechner-section']/div/div[2]/div/form/descendant::*/select[@required='required'])"

    AKTSERVICE_COMPARE_HEADER = "(/html/body/div/div/div/section/div/div[2]/div[1]/div/div/div[1]/h4)"

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def check_if_on_admin_main_page(self):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, self.CURRENT_PAGE_MAIN_HEADER)))
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, self.CURRENT_PAGE_MAIN_HEADER),
                                             "Benutzerverwaltung"))
        WebDriverWait(self.driver, 20).until_not(
            EC.visibility_of_element_located((By.XPATH, self.ADMIN_SPINNER_XPATH)))

    def check_if_on_vermittler_login_page(self, user_with_taa_rights=True, anonymus_info_visible=False):
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, Helper.CURRENT_PAGE_MAIN_HEADER), "Login"))
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "username")))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "username")))
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "password")))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "password")))
        if anonymus_info_visible:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Rechner ohne Anmeldung")))
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Rechner ohne Anmeldung")))

    def check_if_on_vermittler_main_page(self, user_with_taa_rights=True):
        WebDriverWait(self.driver, 20).until_not(
            EC.presence_of_element_located((By.XPATH, self.NEUEDOKUMENTE_SPINNER_XPATH)))
        # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
        #     (By.XPATH, Helper.NEUE_DOKUMENTE_PAGINATION_XPATH)))
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
        #     (By.XPATH, Helper.NEUE_DOKUMENTE_PAGINATION_XPATH)))
        # self.check_vermittler_menu_links(user_with_taa_rights=user_with_taa_rights)

    def check_if_on_kundensuche_page(self):
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, Helper.CURRENT_PAGE_MAIN_HEADER), "Kundensuche Ergebnisse"))

    def check_if_on_mitgliedschaft_page(self, mnr_number):
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, "(/html/body/div/div/div/div/div[1]/ng-include/h3)"), mnr_number))

    def check_if_on_aktservice_page(self):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, self.CURRENT_PAGE_MAIN_HEADER)))
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, self.CURRENT_PAGE_MAIN_HEADER),
                                             "Vergleich"))

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, Helper.NEUE_DOKUMENTE_PAGINATION_XPATH)))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, Helper.NEUE_DOKUMENTE_PAGINATION_XPATH)))

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.AKTSERVICE_COMPARE_HEADER)))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.AKTSERVICE_COMPARE_HEADER)))
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.XPATH, self.AKTSERVICE_COMPARE_HEADER),
                                             u"Folgende Verträge können auf den Leistungsumfang des aktuellen Tarifs 2016 umgestellt werden:"))

    def check_if_on_meine_angebote_page(self):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, self.CURRENT_PAGE_MAIN_HEADER)))
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, self.CURRENT_PAGE_MAIN_HEADER),
                                             "Meine Angebote"))

    def check_if_on_mein_profil_page(self):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, self.CURRENT_PAGE_MAIN_HEADER)))
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, self.CURRENT_PAGE_MAIN_HEADER),
                                             "Meine Daten"))

    def check_vermittler_menu_links(self, user_with_taa_rights=True):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[2]/a[1])")))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[2]/a[1])")))
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[2]/a[1])"),
                                             u"Über uns"))

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[3]/a[1])")))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[3]/a[1])")))
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[3]/a[1])"),
                                             u"Unterlagen"))

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[4]/a[1])")))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[4]/a[1])")))
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[4]/a[1])"),
                                             u"Produkte"))

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[5]/a[1])")))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[5]/a[1])")))
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[5]/a[1])"),
                                             u"Service"))

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[6]/a)")))
        if user_with_taa_rights:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[6]/a)")))
            WebDriverWait(self.driver, 20).until(
                EC.text_to_be_present_in_element((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[6]/a)"),
                                                 u"Rechner"))
        else:
            WebDriverWait(self.driver, 20).until_not(
                EC.visibility_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[6]/a)")))

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[7]/a[1])")))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[7]/a[1])")))
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[7]/a[1])"),
                                             u"Mein Archiv"))

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[8]/a)")))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[8]/a)")))
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[8]/a)"),
                                             u"Mein Bestand"))

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[9]/a)")))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[9]/a)")))
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.XPATH, "(.//*[@id='nav-main']/div/ul/li[9]/a)"),
                                             u"Mein Profil"))

    def check_if_on_secure_email_page(self):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, self.CURRENT_PAGE_MAIN_HEADER)))
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, self.CURRENT_PAGE_MAIN_HEADER),
                                             "Dokumente"))

    def get_tarifdaten_erganzungen_label_xpath(self, erganzungen_no):
        if erganzungen_no in range(1, len(
                self.driver.find_elements_by_xpath(Helper.TARIFDATEN_PRODUKT_ELEMENTS_LABELS_ERGANZUNGEN_XPATH)) + 1):
            return "(/html/body/div/div/div/section/div/div[2]/div/div[5]/div[1]/div/div[2]/table/tbody/tr[%s]/td[1]/ng-include/div/label)" % (
                erganzungen_no)

    def tarifdaten_wait_for_price_reload(self):
        WebDriverWait(self.driver, 20).until_not(
            EC.presence_of_element_located((By.XPATH, self.TARIFDATEN_SPINNER_XPATH)))

    def get_price_from_table_text(self, table_name, row_no="*"):
        if table_name == "mitgliedschaft":
            price_xpath = "(.//*[@id='rechner-section']/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[3])" % (
                str(row_no))

            WebDriverWait(self.driver, 10).until_not(
                EC.text_to_be_present_in_element((By.XPATH, price_xpath), u"0,00 €"))

        if table_name == "rechtschutz":
            price_xpath = "(.//*[@id='rechner-section']/div/div[2]/div/div[3]/div[1]/div/div/div[2]/table[1]/tbody/tr[%s]/td[last()])" % (
                str(row_no))

            WebDriverWait(self.driver, 10).until_not(
                EC.text_to_be_present_in_element((By.XPATH, price_xpath), u"0,00 €"))


        elif table_name == "erganzungen":
            price_xpath = "(.//*[@id='rechner-section']/div/div[2]/div/div[4]/div[1]/div/div/div[2]/table/tbody/tr[%s]/td[4]/div/div)" % (
                str(row_no))

            WebDriverWait(self.driver, 10).until_not(
                EC.text_to_be_present_in_element((By.XPATH, price_xpath), u"0,00 €"))

        elif table_name == "schutzbrief":
            if len(self.driver.find_element_by_xpath("//h3[contains(.,'Ergänzungen')]")) != 0:
                if self.driver.find_element_by_xpath("//h3[contains(.,'Ergänzungen')]").is_displayed():
                    return 1
                    # TODO check xpath below after Mr Wasak fix the schutzbrief prices
                    # price = "(/html/body/div[1]/div/div/section/div/div[2]/div/div[5]/div/div/div[2]/table/tbody/tr[1]/td[%s]/div/div)" % (str(row_no))
                    # WebDriverWait(self.driver, 10).until_not(EC.text_to_be_present_in_element((By.XPATH, price)), u"0,00 €")
                else:
                    return 1
                    # TODO add xpath for price in schutzbrief table
                    # price = "(/html/body/div[1]/div/div/section/div/div[2]/div/div[5]/div/div/div[2]/table/tbody/tr[1]/td[%s]/div/div)" % (str(row_no))
                    # WebDriverWait(self.driver, 10).until_not(EC.text_to_be_present_in_element((By.XPATH, price)), u"0,00 €")

        price = self.driver.find_element_by_xpath(price_xpath).text

        return price

    def get_price_from_table_num(self, table_name, row_no="*"):
        price_text = self.get_price_from_table_text(table_name, row_no)
        regex = re.compile("\d+", re.UNICODE)
        if regex.search(price_text):
            price_num = float(regex.findall(price_text)[0]) + 0.01 * float(regex.findall(price_text)[1])
            return price_num
        else:
            return None

    def get_tarifdaten_table_xpath(self, table_no):
        table = "(///table[%s])" % (str(table_no))

    def get_tarifdaten_zahlweise_label_xpath(self, zahlweise):
        zahlweise_tuple = (u"jahrlich", u"halbjahrlich", u"vierteljahrlich", u"monatlich")

        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(By.XPATH, "//h3[contains(.,'Ergänzungen')]"))
        except Exception:
            pass
            return "(/html/body/div/div/div/section/div/div[2]/div/div[6]/div/div/div[2]/div/div[2]/div/div/div[%s]/div/label)" % (
                zahlweise_tuple.index(zahlweise) + 1)

        if self.driver.find_element_by_xpath("//h3[contains(.,'Ergänzungen')]").is_displayed():
            return "(/html/body/div/div/div/section/div/div[2]/div/div[7]/div/div/div[2]/div/div[2]/div/div/div[%s]/div/label)" % (
                zahlweise_tuple.index(zahlweise) + 1)

    def get_tarifdaten_gesambeitrag_price(self):
        gesambtr_text = self.driver.find_element_by_xpath(self.TARIFDATEN_GESAMTBTR_LABEL_XPATH).text

        regex = re.compile("\d+", re.UNICODE)
        if regex.search(gesambtr_text):
            gesambtr_num = float(regex.findall(gesambtr_text)[0]) + 0.01 * float(regex.findall(gesambtr_text)[1])
            return gesambtr_num

    def get_tarifdaten_gesambeitrag_zahlweise(self):
        gesambtr_text = self.driver.find_element_by_xpath(self.TARIFDATEN_GESAMTBTR_LABEL_XPATH).text
        gesambtr_text = str(gesambtr_text).split(":")
        return gesambtr_text[0]

    def set_tarifdaten_zahlweise(self, zahlweise):
        gesambtr = self.driver.find_element_by_xpath(self.TARIFDATEN_GESAMTBTR_LABEL_XPATH).text
        self.check_and_click_element_by_xpath(self.get_tarifdaten_zahlweise_label_xpath(zahlweise))
        WebDriverWait(self.driver, 10).until_not(
            EC.text_to_be_present_in_element((By.XPATH, self.TARIFDATEN_GESAMTBTR_LABEL_XPATH), gesambtr))

    def get_tarifdaten_visible_anzahl_field_on_erganzungen_popup(self):
        visible_anzahl_fields = []
        for el in self.driver.find_elements_by_name("intItem"):
            if el.is_displayed():
                visible_anzahl_fields.append(el)

        return visible_anzahl_fields

    ERGANZUNGEN_POPUP_XPATH = "(/html/body/div[3]/div/div)"
    ERGANZUNGEN_HEADER_XPATH = "(.//*[@id='rechner-section']/div/div[2]/div/div[4]/div[1]/div/div/div[1]/h4)"
    ERGANZUNGEN_POPUP_PRODUKT_LABELS_XPATH = "(//div[@data-ng-repeat=\"produkt in modalProdukte\"]/descendant::div[@class=\"checkbox\"]/descendant::label)"
    ERGANZUNGEN_POPUP_PRODUKT_INPUTS_XPATH = "(//div[@data-ng-repeat=\"produkt in modalProdukte\"]/descendant::div[@class=\"checkbox\"]/descendant::label/input)"
    ERGANZUNGEN_CHECKBOX_XPATH = "(/html/body/div[3]/div/div/form/div[2]/div/div/div[1]/div/div/div/label/input)"
    ERGANZUNGEN_POPUP_OK_BUTTON_XPATH = "//div[3]/button"
    ERGANZUNGEN_POPUP_VALIDATION_ALERT = "(/html/body/div[3]/div/div/form/div[2]/div[1]/p)"

    ANTRAG_ANTRAGSTELLER_TEXTS_ELEMENTS_XPATH = "(/html/body/div[1]/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/descendant::*[normalize-space(text())='Zahlung per Lastschrift'])"

    def get_antrag_antragsteller_text(self, text):
        return self.driver.find_elements_by_xpath(
            "(/html/body/div[1]/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/descendant::*[normalize-space(text())='%s'])" % (
                text))

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def check_and_click_element_by_xpath(self, xpath, scroll_to_footer="no"):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, xpath)))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, xpath)))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, xpath)))
        self.highlight(self.driver.find_element_by_xpath(xpath))
        self.driver.find_element_by_xpath(xpath).click()

    def check_and_click_element_by_link_text(self, linktext):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.LINK_TEXT, linktext)))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.LINK_TEXT, linktext)))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.LINK_TEXT, linktext)))
        self.highlight(self.driver.find_element_by_link_text(linktext))

        self.driver.find_element_by_link_text(linktext).click()

    def check_and_click_element_by_id(self, element_id):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.ID, id)))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.ID, id)))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.ID, id)))
        self.highlight(self.driver.find_element_by_id(element_id))
        self.driver.find_element_by_id(id).click()

    def check_and_click_element_by_name(self, name):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.NAME, name)))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.NAME, name)))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.NAME, name)))
        self.highlight(self.driver.find_element_by_name(name))
        self.driver.find_element_by_name(name).click()

    def enter_text_and_check_validation_in_element_by_id(self, id, entered_text, desired_validation):
        self.driver.find_element_by_id(id).clear()
        self.driver.find_element_by_id(id).send_keys(entered_text)

        if desired_validation == 'invalid':
            try:
                self.assertRegexpMatches(self.driver.find_element_by_id(id).get_attribute("class"),
                                         r"ng-invalid")
            except AssertionError as e:
                self.verificationErrors.append(
                    "Field " + id + " not " + desired_validation + " after " + entered_text + " entered / line %s" % (
                        sys.exc_info()[-1].tb_lineno))
                # TODO Add border-color check for invalidated fields.
                # try:
                # self.assertEqual("rgba(169, 68, 66, 1)", self.driver.find_element_by_id(id).value_of_css_property("border-color"))
                # except AssertionError:
                # self.verificationErrors.append(
                # "Field %s border-color:%s / line %d" % (id, self.driver.find_element_by_id(id).value_of_css_property("border-color"), sys.exc_info()[-1].tb_lineno))
        elif desired_validation == 'valid':
            try:
                self.assertNotRegexpMatches(self.driver.find_element_by_id(id).get_attribute("class"),
                                            r"ng-invalid")
            except AssertionError as e:
                self.verificationErrors.append(
                    "Field " + id + " not " + desired_validation + " after " + entered_text + " entered / line %s" % (
                        sys.exc_info()[-1].tb_lineno))
        elif desired_validation == 'notaccepted':
            try:
                self.assertNotEqual(self.driver.find_element_by_id(id).text,
                                    entered_text)
            except AssertionError as e:
                self.verificationErrors.append(
                    "Unaccepted text \"" + entered_text + "\" allowed in field" + id + " / line %s" % (
                        sys.exc_info()[-1].tb_lineno))
                # self.highlight(self.driver.find_element_by_id(id))

    def enter_text_and_check_validation_in_element_by_xpath(self, xpath, entered_text, desired_validation):
        element = self.driver.find_element_by_xpath(xpath)

        element.clear()
        element.send_keys(entered_text)

        if desired_validation == 'invalid':
            try:
                self.assertRegexpMatches(element.get_attribute("class"),
                                         r"ng-invalid")
            except AssertionError as e:
                self.verificationErrors.append(
                    "Field " + element.get_attribute(
                        "id") + " not " + desired_validation + " after " + entered_text + " entered / line %s" % (
                        sys.exc_info()[-1].tb_lineno))
                # TODO Add border-color check for invalidated fields.
                # try:
                # self.assertEqual("rgba(169, 68, 66, 1)", self.driver.find_element_by_id(id).value_of_css_property("border-color"))
                # except AssertionError:
                # self.verificationErrors.append(
                # "Field %s border-color:%s / line %d" % (id, self.driver.find_element_by_id(id).value_of_css_property("border-color"), sys.exc_info()[-1].tb_lineno))
        elif desired_validation == 'valid':
            try:
                self.assertNotRegexpMatches(element.get_attribute("class"),
                                            r"ng-invalid")
            except AssertionError as e:
                self.verificationErrors.append(
                    "Field " + element.get_attribute(
                        "id") + " not " + desired_validation + " after " + entered_text + " entered / line %s" % (
                        sys.exc_info()[-1].tb_lineno))
        elif desired_validation == 'notaccepted':
            try:
                self.assertNotEqual(element.text,
                                    entered_text)
            except AssertionError as e:
                self.verificationErrors.append(
                    "Unaccepted text \"" + entered_text + "\" allowed in field" + element.get_attribute(
                        "id") + " / line %s" % (
                        sys.exc_info()[-1].tb_lineno))
                # self.highlight(self.driver.find_element_by_id(id))

    def validate_date_field_by_id_not_refreshing(self, id):
        self.enter_text_and_check_validation_in_element_by_id(id, "31.09.2013", desired_validation="invalid")

        self.driver.find_element_by_id(id).send_keys(Keys.ARROW_LEFT)
        self.driver.find_element_by_id(id).send_keys(Keys.ARROW_LEFT)
        self.driver.find_element_by_id(id).send_keys(Keys.ARROW_LEFT)
        self.driver.find_element_by_id(id).send_keys(Keys.ARROW_LEFT)
        self.driver.find_element_by_id(id).send_keys(Keys.ARROW_LEFT)
        self.driver.find_element_by_id(id).send_keys(Keys.ARROW_LEFT)
        self.driver.find_element_by_id(id).send_keys("\b")
        self.driver.find_element_by_id(id).send_keys("0")

        try:
            self.assertNotRegexpMatches(self.driver.find_element_by_id(id).get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(
                "Field " + id + " not valid after 30.09.2013 entered // field not refreshing / / line %s" % (
                    sys.exc_info()[-1].tb_lineno))

        self.enter_text_and_check_validation_in_element_by_id(id, "31.09.2013", desired_validation="invalid")
        self.driver.find_element_by_id(id).send_keys("\b\b\b\b\b\b\b")
        self.driver.find_element_by_id(id).send_keys("0092013")
        try:
            self.assertNotRegexpMatches(self.driver.find_element_by_id(id).get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(
                "Field " + id + " not valid after deleting date with [backspace] // field not refreshing / line %s" % (
                    sys.exc_info()[-1].tb_lineno))

    def no_more_than_one_window_open(self, driver):
        return len(driver.window_handles) == 1

    def is_elements_color(self, elements, color):
        for element in elements:
            try:
                self.assertEqual(color, element.value_of_css_property("color"))
            except AssertionError:
                self.verificationErrors.append("Label isLandwirteMitglied color:%s / line %d" % (
                    element.value_of_css_property("color"), sys.exc_info()[-1].tb_lineno))

    def is_not_elements_color(self, elements, color):
        for element in elements:
            try:
                self.assertFalse(color, element.value_of_css_property("color"))
            except AssertionError:
                self.verificationErrors.append("Label isLandwirteMitglied color:%s / line %d" % (
                    element.value_of_css_property("color"), sys.exc_info()[-1].tb_lineno))

    def highlight(self, element):
        """Highlights (blinks) a Selenium Webdriver element"""
        driver = element._parent

        # self.scroll_to_element(element)

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                  element, s)

        original_style = element.get_attribute('style')
        apply_style("background: yellow; ")
        # time.sleep(.2)
        apply_style(original_style)

    def scroll_to_element(self, element, y_pos=400, x_pos=0):
        self.driver.execute_script(
            "window.scrollTo(%d, %d);" % (element.location["x"] + x_pos, element.location["y"] + y_pos))

    def wait_for_pdf_spinner(self):
        WebDriverWait(self.driver, 5).until_not(
            EC.visibility_of_element_located((By.XPATH, self.PDF_ERSTELLEN_SPINNER_XPATH)))

    def hide_drop_down_menu(self):
        self.driver.execute_script(
            "document.getElementById('megadropdown-main-div').style.display = 'none';")

    def wait_for_landwirte_popup_show(self):
        WebDriverWait(self.driver, 4).until(
            EC.visibility_of_element_located((By.XPATH, self.ZIELGRUPPE_LANDWIRTE_POPUP_XPATH)))
        WebDriverWait(self.driver, 4).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
        self.assertEqual("Hinweis zu den Tarifierungsdaten",
                         self.driver.find_element_by_xpath("(/html/body/div[3]/div/div/div[1]/h3)").text)

    def wait_for_landwirte_popup_hide(self):
        WebDriverWait(self.driver, 4).until(
            EC.invisibility_of_element_located((By.XPATH, self.ZIELGRUPPE_LANDWIRTE_POPUP_XPATH)))
