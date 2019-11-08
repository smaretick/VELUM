# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class KOMPARTMENT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://kompartment.io/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_k_o_m_p_a_r_t_m_e_n_t(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_xpath("//section[2]/button").click()
        driver.find_element_by_xpath("//input[@type='email']").clear()
        driver.find_element_by_xpath("//input[@type='email']").send_keys("scottmaretick51@gmail.com")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("sm110751")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("sm110751")
        driver.find_element_by_css_selector("div.checkbox-icon").click()
        driver.find_element_by_xpath("//form[@id='register-form']/label[2]/ion-checkbox/div").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("SCOTT MARETICK")
        driver.find_element_by_xpath("//ion-icon").click()
        driver.find_element_by_xpath("//main/button[2]").click()
        driver.find_element_by_xpath("//input[@type='email']").clear()
        driver.find_element_by_xpath("//input[@type='email']").send_keys("scottmaretick51@gmail.com")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("sm110751")
        driver.find_element_by_css_selector("button.confirm-btn.activated").click()
        driver.find_element_by_css_selector("main.purple > main").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t0-0']/ng-component[2]/ion-content/div[2]/kompartment-details/div/div/kompartment-preview/notes-preview/notes-list/ka-card/ion-card/ion-card-header/ion-buttons/button").click()
        driver.find_element_by_xpath("//textarea").clear()
        driver.find_element_by_xpath("//textarea").send_keys("DAILY WORK OUT XSPORT NAPERVILLE")
        driver.find_element_by_id("dt-13-0").click()
        driver.find_element_by_css_selector("button.picker-opt.activated").click()
        driver.find_element_by_css_selector("button.picker-opt.activated").click()
        driver.find_element_by_xpath("//div[2]/button").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        driver.find_element_by_xpath("//div[3]/div/button").click()
        driver.find_element_by_xpath("//div[4]/button[2]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t0-0']/ng-component[2]/ion-content/div[2]/kompartment-details/div/div/kompartment-preview/files-preview/files-list/ka-card/ion-card/ion-card-header/ion-icon").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t0-0']/ng-component[2]/ion-content/div[2]/kompartment-details/div/div/kompartment-preview/files-preview/files-list/ka-card/ion-card/ion-card-header/ion-icon").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t0-0']/ng-component[2]/ion-content/div[2]/kompartment-details/div/div/kompartment-preview/files-preview/files-list/ka-card/ion-card/ion-card-header/ion-buttons/button").click()
        driver.find_element_by_xpath("//div[3]/button[2]").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t0-0']/ng-component[2]/ion-content/div[2]/kompartment-details/div/div/kompartment-preview/files-preview/files-list/ka-card/ion-card/ion-card-header/ion-buttons/button").click()
        driver.find_element_by_xpath("//div[3]/button[2]").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t0-0']/ng-component[2]/ion-header/ion-navbar/ion-buttons/button").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t0-0']/ng-component[3]/ion-header/ion-navbar/ion-buttons[2]/button").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t0-0']/ng-component[2]/ion-header/ion-navbar/button").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t0-0']/ng-component/ion-header/ion-navbar/button[2]").click()
        driver.find_element_by_xpath("//button[7]").click()
        driver.find_element_by_xpath("//main/button[2]").click()
        driver.find_element_by_xpath("//input[@type='email']").clear()
        driver.find_element_by_xpath("//input[@type='email']").send_keys("scottmaretick51@gmail.com")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("sm110751")
        driver.find_element_by_css_selector("button.confirm-btn.activated").click()
        driver.find_element_by_css_selector("main.purple > main").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t1-0']/ng-component[2]/ion-content/div[2]/kompartment-details/div/div/kompartment-preview/files-preview/files-list/ka-card/ion-card/ion-card-header/ion-buttons/button").click()
        driver.find_element_by_xpath("//div[3]/button[2]").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t1-0']/ng-component[2]/ion-content/div[2]/kompartment-details/div/div/kompartment-preview/files-preview/files-list/ka-card/ion-card/ion-card-header/ion-buttons/button").click()
        driver.find_element_by_xpath("//div[3]/button").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t1-0']/ng-component[2]/ion-header/ion-navbar/button").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t1-0']/ng-component/ion-header/ion-navbar/button[2]").click()
        driver.find_element_by_xpath("//button[7]").click()
        driver.find_element_by_xpath("//main/button[2]").click()
        driver.find_element_by_xpath("//input[@type='email']").clear()
        driver.find_element_by_xpath("//input[@type='email']").send_keys("scottmaretick51@gmail.com")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("sm110751")
        driver.find_element_by_css_selector("button.confirm-btn.activated").click()
        driver.find_element_by_css_selector("main.purple > main").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t2-0']/ng-component[2]/ion-content/div[2]/kompartment-details/div/div/kompartment-preview/files-preview/files-list/ka-card/ion-card/ion-card-header/ion-buttons/button").click()
        driver.find_element_by_xpath("//file-input/button").click()
        driver.find_element_by_css_selector("input[type=\"file\"]").click()
        driver.find_element_by_css_selector("input[type=\"file\"]").clear()
        driver.find_element_by_css_selector("input[type=\"file\"]").send_keys("/Users/scottmaretick/Desktop/java/java.readme.rtf")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t2-0']/ng-component[2]/ion-content/div[2]/kompartment-details/div/div/kompartment-preview/files-preview/files-list/ka-card[2]/ion-card/ion-card-header/ion-buttons/button").click()
        driver.find_element_by_xpath("//file-input/button").click()
        driver.find_element_by_css_selector("input[type=\"file\"]").click()
        driver.find_element_by_css_selector("input[type=\"file\"]").clear()
        driver.find_element_by_css_selector("input[type=\"file\"]").send_keys("/Users/scottmaretick/Desktop/Simulaor-iPhone8.png")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t2-0']/ng-component[2]/ion-header/ion-navbar/button").click()
        driver.find_element_by_css_selector("span.secondary").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t2-0']/ng-component[2]/ion-header/ion-navbar/button").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t2-0']/ng-component/ion-content/div[2]/kompartments-list/ion-grid/ion-row/add-new-card/section/main/section/ion-icon").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("IOS")
        driver.find_element_by_id("sel-40-0").click()
        driver.find_element_by_id("alert-input-5-10").click()
        driver.find_element_by_xpath("//div[4]/button[2]").click()
        driver.find_element_by_id("sel-42-0").click()
        driver.find_element_by_id("alert-input-6-6").click()
        driver.find_element_by_xpath("//div[4]/button[2]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        driver.find_element_by_css_selector("input.searchbar-input").clear()
        driver.find_element_by_css_selector("input.searchbar-input").send_keys("scottmaretick51@gmail.com")
        driver.find_element_by_xpath("//ion-segment-button[@value='users']").click()
        driver.find_element_by_xpath("//ion-toolbar/ion-buttons/button").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t2-0']/ng-component[2]/ion-header/ion-navbar/ion-buttons/button").click()
        driver.find_element_by_xpath("//div[3]/button[2]").click()
        driver.find_element_by_xpath("//ion-tab[@id='tabpanel-t2-0']/ng-component/ion-header/ion-navbar/button[2]").click()
        driver.find_element_by_xpath("//button[7]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
