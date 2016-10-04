# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from helpers import Helper


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
