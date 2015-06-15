# -*- coding: utf-8 -*-
from binascii import a2b_base64
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from helpers import Helper
import time, sys, re

class SelectWithFooterSlide(Select):
    def __init__(self, webelement, driver):
        Select.__init__(self, webelement)
        self.driver = driver

    def _setSelected(self, option):
        if not option.is_selected():
            actions = ActionChains(self.driver)
            # actions.move_to_element(self.driver.find_element_by_xpath(Helper.FOOTER_SPAN_XPATH))
            # Helper.scroll_to_element(Helper(self.driver), self._el, 1000)
            actions.move_to_element(self._el)
            actions.click(option)
            actions.perform()

    def _unsetSelected(self, option):
        if option.is_selected():
            actions = ActionChains(self.driver)
            # actions.move_to_element(self.driver.find_element_by_xpath(Helper.FOOTER_SPAN_XPATH))
            Helper.scroll_to_element(Helper(self.driver), self._el)
            actions.click(option)
            actions.perform()
