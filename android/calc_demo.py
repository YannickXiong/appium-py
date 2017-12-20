from appium import webdriver

desired_caps = dict()
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "5.1.1"
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# by id
driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
driver.find_element_by_id("com.android.calculator2:id/digit_5").click()
driver.find_element_by_id("com.android.calculator2:id/digit_9").click()
driver.find_element_by_id("com.android.calculator2:id/del").click()
driver.find_element_by_id("com.android.calculator2:id/digit_9").click()
driver.find_element_by_id("com.android.calculator2:id/digit_5").click()
driver.find_element_by_id("com.android.calculator2:id/op_add").click()
driver.find_element_by_id("com.android.calculator2:id/digit_6").click()
driver.find_element_by_id("com.android.calculator2:id/eq").click()

# by class, return single element
# bt = driver.find_element_by_class_name("android.widget.Button")

# by class, return multi elements
# bt = driver.find_elements_by_class_name("android.widget.Button")
# for n in bt:
#     print("this is number : ", n.get_attribute("name"))

# # by xpath，根据xpath + tag定位具体元素
# # text充当tag
# driver.find_element_by_xpath("//android.widget.Button[contains(@text, '1')]").click()
# # resource-id充当tag
# driver.find_element_by_xpath("//android.widget.Button[contains(@resource-id, 'com.android.calculator2:id/digit_5')]").click()
# driver.find_element_by_xpath("//android.widget.Button[contains(@index, '2')]").click()
# driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc, 'delete')]").click()
# # 不能使用bounds充当tag
# # driver.find_element_by_xpath("//android.widget.Button[contains(@text, '[0,842][1440,2712]')]").click()
# driver.find_element_by_xpath("//android.widget.Button[contains(@text, '9')]").click()
# driver.find_element_by_xpath("//android.widget.Button[contains(@text, '5')]").click()
# driver.find_element_by_xpath("//android.widget.Button[contains(@text, '+')]").click()
# driver.find_element_by_xpath("//android.widget.Button[contains(@text, '6')]").click()
# driver.find_element_by_xpath("//android.widget.Button[contains(@text, '=')]").click()

# # by Accessibility ID
#
# # 数字1-9的context-desc为空
# driver.find_element_by_id("com.android.calculator2:id/digit_9").click()
#
# # by accessibility id，实际上是context-desc
# driver.find_element_by_accessibility_id("plus").click()
# driver.find_element_by_id("com.android.calculator2:id/digit_4").click()
# driver.find_element_by_accessibility_id("times").click()
# driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
# driver.find_element_by_id("com.android.calculator2:id/digit_0").click()
# driver.find_element_by_accessibility_id("equals").click()

# # by uiautomator 方法定位
#
# # by text
# driver.find_element_by_android_uiautomator('new UiSelector().text("9")').click()
#
# # by index
# # 直接使用index可能出现问题，因为父级别有index 0，子级别也有index 0
# # driver.find_element_by_android_uiautomator('new UiSelector().index(0)').click()
# # 先通过唯一的text定位到9，再定位9的同级元素的index 0，这回是7唯一了。实际上这里也有一些问题，即如果上面先执行了
# # 'new UiSelector().text("9")'，则不会在计算器上显示7，但是如果上面注释了，这句显示7是正常的
# driver.find_element_by_android_uiautomator('new UiSelector().text("9").fromParent(new UiSelector().index(0))').click()
#
# # by resource-id error
# # Could not parse UiSelector argument: UiSelector has no resource-id method"}
# # driver.find_element_by_android_uiautomator('new UiSelector().resource-id("com.android.calculator2:id/digit_4")').click()
#
# # by description, actually is context-desc
# driver.find_element_by_android_uiautomator('new UiSelector().description("times")').click()
#
# # UiSelector() no bounds method
# # driver.find_element_by_android_uiautomator('new UiSelector().bounds("[56,1776][352,2187]")').click()
#
# driver.find_element_by_android_uiautomator('new UiSelector().text("7")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().text("0")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().text("=")').click()

# get result
# by xpath
result = driver.find_element_by_id("com.android.calculator2:id/formula").get_attribute("name")
# fromParent是根据同级元素查找，所以实际输出的是result = 7，而不是想要的result
# result = driver.find_element_by_android_uiautomator('new UiSelector().text("7").fromParent(new UiSelector().index(0))').get_attribute("name")

# 改为根据父级元素定位，这里有一些问题，一直取不到结果
# result = driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.FrameLayout").childSelector(new UiSelector().index(0))').get_attribute("name")

print("result = ", result)
assert int(result) == 1601
# driver.quit()
