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
        caps.setCapability("appPackage", "com.example.myapp");
        caps.setCapability("appActivity", "com.example.myapp.MainActivity");

        driver = new AndroidDriver<>(
                new URL("http://127.0.0.1:4723/wd/hub"),
                caps
        );
    }

    @Test
    public void loginTest() {
        MobileElement username = driver.findElementById("com.example.myapp:id/username");
        username.sendKeys("testuser");

        MobileElement password = driver.findElementById("com.example.myapp:id/password");
        password.sendKeys("Password123");

        driver.findElementById("com.example.myapp:id/loginBtn").click();

        MobileElement welcomeText =
                driver.findElementById("com.example.myapp:id/welcomeText");

        Assert.assertTrue(welcomeText.isDisplayed(), "Login not successful");
    }

    @AfterClass
    public void tearDown() {
        driver.quit();
    }
}
