from appium import webdriver
from time import sleep

desired_caps = dict()

desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "5.1.1"
desired_caps['deviceName'] = '58 Wallet'
desired_caps['appPackage'] = 'io.hx58wallet'
desired_caps['appActivity'] = 'io.hx58wallet.MainActivity'


driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.launch_app()
# 加载需要时间，否则定位不到元素
sleep(3)
# # "Add Card".click()
# add_card_button = driver.find_element_by_android_uiautomator('new UiSelector().text("Add Card")').click()

# "+".click()
add_card_button = driver.find_element_by_android_uiautomator('new UiSelector().text("Add Card").'
                                                             'fromParent(new UiSelector().index(0))')

# full xpath
add_card_button = driver.find_element_by_xpath('//android.widget.FrameLayout'
                                               '/android.widget.LinearLayout'
                                               '/android:id/content'
                                               '/android.widget.FrameLayout'
                                               '/android.view.View'
                                               '/android.view.View'
                                               '/android.view.View'
                                               '/android.view.View'
                                               '/android.support.v4.widget.DrawerLayout'
                                               '/android.view.View'
                                               '/android.view.View'
                                               '/android.view.View[3]'
                                               '/android.view.View'
                                               '/android.view.View'
                                               '/android.view.View'
                                               '/android.view.View'
                                               '/android.view.View'
                                               '/android.widget.TextView')
add_card_button.click()

# card_name = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "Create Card")]../android.view.View../android.widget.ScrollView/android.view.View/android.widget.EditText')
sleep(3)
# card_name = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "Import Card")]/../../android.view.View[5]').click()
# card_name = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "Import Card")]/../../android.view.View[5]/android.widget.TextView')
card_name = driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "Import Card")]/parent::android.view.View/parent::android.widget.ScrollView/android.view.View[5]/android.widget.TextView')
card_name.click()

# card_name.send_keys("8888")