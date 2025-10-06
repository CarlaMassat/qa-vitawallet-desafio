import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

load_dotenv()

def create_driver():

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = os.getenv("APPIUM_DEVICE_PLATFORM")
    options.device_name = os.getenv("APPIUM_DEVICE_NAME")
    options.app = os.getenv("APPIUM_APP_PATH")
    options.automation_name = "UiAutomator2"
    options.app_package = os.getenv("APPIUM_APP_PACKAGE")
    options.app_activity = os.getenv("APPIUM_APP_ACTIVITY")

    options.no_reset = False


    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    return driver


