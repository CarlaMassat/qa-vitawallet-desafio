import time
import os
from dotenv import load_dotenv
from utils.driver_factory import create_driver
from pageobjects.login_page import LoginPage
from pageobjects.cripto_page import  CryptoPage

load_dotenv()

def test_exchange_ars_to_usdt():
    driver = create_driver()


    login = LoginPage(driver)
    crypto = CryptoPage(driver)

    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    login.allow_permissions()
    login.login(email, password)


    crypto.close_popup()
    crypto.goto_crypto()
    crypto.set_exchange_amount(2000)
    crypto.continue_crypto()
    crypto.confirm_crypto()
    crypto.goto_start()
    crypto.goto_history()


    driver.quit()