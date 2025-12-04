import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import io.appium.java_client.android.AndroidDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.net.URL;

public class LoginTest {

    private AppiumDriver<MobileElement> driver;

    @BeforeClass
    public void setUp() throws Exception {
        DesiredCapabilities caps = new DesiredCapabilities();

        caps.setCapability("platformName", "Android");
        caps.setCapability("deviceName", "Android Emulator");
        caps.setCapability("automationName", "UiAutomator2");
        caps.setCapability("appPackage", "com.saucelabs.mydemoapp.android");
        caps.setCapability("appActivity", "com.saucelabs.mydemoapp.android.view.activities.SplashActivity");
        caps.setCapability("newCommandTimeout", 300);

        driver = new AndroidDriver<>(
                new URL("http://127.0.0.1:4723/wd/hub"),
                caps
        );
    }

    @Test
    public void loginTest() {
        try {
            // Try to open menu if present
            try {
                driver.findElementByAccessibilityId("open menu").click();
            } catch (Exception e) {
                // ignore
            }

            // Enter credentials (locators may vary)
            try {
                MobileElement username = driver.findElementByAccessibilityId("Username input field");
                username.clear();
                username.sendKeys("bob@example.com");
            } catch (Exception e) {
                MobileElement username = driver.findElementById("com.saucelabs.mydemoapp.android:id/username");
                username.clear();
                username.sendKeys("bob@example.com");
            }

            try {
                MobileElement password = driver.findElementByAccessibilityId("Password input field");
                password.clear();
                password.sendKeys("10203040");
            } catch (Exception e) {
                MobileElement password = driver.findElementById("com.saucelabs.mydemoapp.android:id/password");
                password.clear();
                password.sendKeys("10203040");
            }

            // Click login - try several locators
            try {
                driver.findElementByAccessibilityId("Login button").click();
            } catch (Exception e) {
                driver.findElementById("com.saucelabs.mydemoapp.android:id/loginButton").click();
            }

            // Verify products screen
            boolean found = false;
            try {
                MobileElement prod = driver.findElementByAccessibilityId("products screen");
                found = prod.isDisplayed();
            } catch (Exception e) {
                try {
                    MobileElement prod = driver.findElementById("com.saucelabs.mydemoapp.android:id/product_list");
                    found = prod.isDisplayed();
                } catch (Exception ex) {
                    // fallback
                }
            }

            Assert.assertTrue(found, "Products screen not found after login");

        } finally {
            // nothing
        }
    }

    @AfterClass
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
