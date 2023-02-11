from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium import webdriver

class homePage():

    # Homepage
    filter_select_xpath = '//select[@data-test="product_sort_container"]'
    open_menu_xpath = "//button[text()='Open Menu']"
    logout_link_id = 'logout_sidebar_link'
    appLogo_classname = 'app_logo'

    def __init__(self, driver):
       self.driver = driver

    def selectFilterOption(self,filterValue):
        dropdown = Select(self.driver.find_element(By.XPATH,self.filter_select_xpath))
        dropdown.select_by_visible_text(filterValue)

    def click_LogoutButton(self):
        pass


    def verifyAppLogo(self):
        return self.driver.find_element(By.CLASS_NAME,self.appLogo_classname).is_displayed()