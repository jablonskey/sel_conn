import unittest

from selenium import webdriver

from service import common_tasks


class Connect2508Test(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
        self.profile = webdriver.FirefoxProfile()
        self.profile.native_events_enabled = False
        self.driver = webdriver.Firefox(self.profile)
        self.driver.maximize_window()

        self.driver.implicitly_wait(2)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_connect2058(self):
        driver = self.driver
        self.go_to_external_page()
        self.driver.get(self.base_url + "ng/#/vermittler/login?showRechnerLink=true")
        self.check_if_on_vermittler_login_page(anonymus_info_visible=True)
        self.login_to_connect_vermittler(self.base_url, main_page_after_login=False)
        self.check_if_on_zielgruppe_page()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
__author__ = 'Jablonski'
