python_appium/test_login.py

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "Android Emulator",
            "appPackage": "com.saucelabs.mydemoapp.android",
            "appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
        }

        self.driver = webdriver.Remote(
            "http://127.0.0.1:4723/wd/hub",
            desired_caps
        )
        self.driver.implicitly_wait(10)

    def test_login_flow(self):
        # Navigate to login
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "open menu").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "menu item log in").click()

        # Type username & password
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Username input field").send_keys("bob@example.com")
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Password input field").send_keys("10203040")

        # Submit login
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login button").click()

        # Verify login
        success = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "products screen")
        self.assertTrue(success.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
