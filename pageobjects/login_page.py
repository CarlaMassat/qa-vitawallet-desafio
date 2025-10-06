from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.allow_button = (AppiumBy.ID,"com.android.permissioncontroller:id/permission_allow_button")

        self.signin_button =(AppiumBy.ACCESSIBILITY_ID, "Iniciar sesión")

        self.email_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)' )
        self.password_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)' )

        self.submit_button = (AppiumBy.ACCESSIBILITY_ID, "Ingresar")



    def allow_permissions(self):
        try:
            btn = WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self.allow_button)
        )
            btn.click()
        except Exception:
            pass

    def click_signin(self):
        try:
            btn = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.signin_button)

        )
            btn.click()
        except Exception:
            pass

    # Primer login
    def login(self, email, password):

        self.allow_permissions()

        self.click_signin()


        email_field = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.email_field)
        )

        email_field.click()
        email_field.send_keys(email)

        password_field = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.password_field)
        )
        password_field.click()
        password_field.send_keys(password)

        try:
            self.driver.hide_keyboard()
        except Exception:
            self.driver.tap([(10, 10)])


        submit_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.submit_button)

        )
        submit_btn.click()