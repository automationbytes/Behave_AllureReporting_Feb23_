import allure
from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from PageObjects.homePage import homePage
from PageObjects.LoginPage import LoginPage


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.implicitly_wait(30)
driver.maximize_window()
hp = homePage(driver)
lp = LoginPage(driver)

@given(u'the user launches the application')
def the_user_launches_the_application(context):
    context.driver = driver
    context.driver.get("https://www.saucedemo.com/")

@when(u'the user verifies the logo')
def the_user_verifies_the_logo(context):
    context.driver = driver
    logo = context.driver.find_element(By.XPATH, '//div[@class="login_logo"]')
    assert logo.is_displayed() is True

@then(u'the user enters valid credentials')
def the_user_enters_valid_credentials(context):
    context.driver = driver
    lp.enterUserName("standard_user")
    lp.enterPassWord("secret_sauce")
    lp.clickLogin()


@given(u'the user verifies the homepage logo')
def the_user_verifies_the_homepage_logo(context):
    context.driver = driver
    logo = context.driver.find_element(By.XPATH, '//div[@class="app_logo"]')
    assert logo.is_displayed() is False



@then(u'the user filters high to low')
def the_user_filters_high_to_low(context):
    context.driver =driver
    hp.selectFilterOption("Price (high to low)")

@then(u'the user filters low to high')
def the_user_filters_high_to_low(context):
    context.driver =driver
    hp.selectFilterOption("Price (low to high)")
    Capture_Screensht(context)
#
def after_step(context,step):
     if step.status == "failed":
         Capture_Screensht(context)

@then(u'the user clicks on Add to cart button')
def step_impl(context):
    pass



def Capture_Screensht(context):
    context.driver = driver
    allure.attach(context.driver.get_screenshot_as_file(),name=step.name,attachment_type=allure.attachment_type.PNG)


@when(u'the user enters "{username}" in username field')
def enter_username(context,username):
    context.driver = driver
    lp.enterUserName(username)



@then(u'the user enters "{password}" in password field')
def step_impl(context,password):
    context.driver = driver
    lp.enterPassWord(password)


@then(u'the user clicks on login button')
def step_impl(context):
    context.driver = driver
    lp.clickLogin()

