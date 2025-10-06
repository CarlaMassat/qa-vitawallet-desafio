from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CryptoPage:
    def __init__(self, driver):
        self.driver = driver
        self.close = (AppiumBy.ACCESSIBILITY_ID, "Entendido")
        self.crypto_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Cripto")')
        self.crypto_exchange_ars = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(6)')
        self.crypto_exchange_usdt = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").instance(10)')
        self.crypto_exchange_popup_ars = (AppiumBy.ACCESSIBILITY_ID,'ARS,   -  Peso Argentino')
        self.crypto_exchange_popup_usdt = (AppiumBy.ACCESSIBILITY_ID, 'USDT,   -  USD Tether')
        self.crypto_exchange_input = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="ARS, Monto mínimo: 1.000 ARS"]//android.widget.EditText')
        self.crypto_continue = (AppiumBy.ACCESSIBILITY_ID, 'Continuar')
        self.crypto_confirm = (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "Confirmar")]')
        self.crypto_start = (AppiumBy.XPATH, '//android.widget.TextView[@text="Ir al inicio"]')
        self.crypto_exchange_history = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Intercambio USDT").instance(0)')
        self.crypto_exchange_history_popup = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(4)')




    def close_popup(self):
        try:
            close_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.close)
            )
            close_btn.click()
        except Exception:
            pass

    def goto_crypto(self):
        crypto_btn = WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self.crypto_button)
        )
        crypto_btn.click()

        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.crypto_exchange_ars)
        )

        exchange_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.crypto_exchange_ars)
        )
        exchange_btn.click()

        popup_option = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.crypto_exchange_popup_ars)
        )

        popup_option.click()

        crypto_btn = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.crypto_button)
        )
        crypto_btn.click()



        exchange_btn_usdt = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.crypto_exchange_usdt)
        )
        exchange_btn_usdt.click()


        popup_btn_usdt = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.crypto_exchange_popup_usdt)
        )
        popup_btn_usdt.click()


    def set_exchange_amount(self, amount):
        input_field = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.crypto_exchange_input)
        )
        input_field.clear()
        input_field.send_keys(str(amount))


    def continue_crypto(self):
        continue_btn = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.crypto_continue)
        )
        continue_btn.click()

    def confirm_crypto(self):
        confirm_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.crypto_confirm)
        )
        confirm_btn.click()

    def goto_start(self):
        start_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.crypto_start)
        )
        start_btn.click()

    def goto_history(self):
        history_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.crypto_exchange_history)
        )
        history_btn.click()
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.crypto_exchange_history_popup)
        )