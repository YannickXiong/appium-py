from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = dict()

desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "5.1.1"
desired_caps['deviceName'] = '58 Wallet'
desired_caps['appPackage'] = 'io.hx58wallet'
desired_caps['appActivity'] = 'io.hx58wallet.MainActivity'
desired_caps['resetKeyboard'] = True    #
desired_caps['unicodeKeyboard'] = True  # 中文输入
desired_caps['automationName'] = 'Uiautomator2'

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.launch_app()
print("1 current_activity : ", driver.current_activity)
print("1 contexts : ", driver.contexts)
print("1 current_context : ", driver.current_context)

# return 404
# print("1 current_url : ", driver.current_url)

# 加载需要时间，否则定位不到元素

sleep(3)
# # "Add Card".click()
# add_card_button = driver.find_element_by_android_uiautomator('new UiSelector().text("Add Card")').click()

# "+".click()
add_card_button = driver.find_element_by_android_uiautomator('new UiSelector().text("添加卡片").'
                                                             'fromParent(new UiSelector().index(0))')
add_card_button.click()

sleep(3)
print("2 current_activity : ", driver.current_activity)
print("2 contexts : ", driver.contexts)
print("2 current_context : ", driver.current_context)

import_card_str = '//android.widget.TextView[contains(@text, "导入卡片")]'
import_card_btn = driver.find_element_by_xpath(import_card_str)
card_name_input = driver.find_element_by_xpath(import_card_str +
                                               '/../../android.view.View[1]/android.widget.EditText')
card_pwd_input = driver.find_element_by_xpath(import_card_str +
                                              '/../../android.view.View[2]/android.widget.EditText')
card_repeat_pwd_input = driver.find_element_by_xpath(import_card_str +
                                                     '/../../android.view.View[3]/android.widget.EditText')
card_hint_input = driver.find_element_by_xpath(import_card_str +
                                               '/../../android.view.View[4]/android.widget.EditText')
# 根据父亲关系定位，简写
# card_create_btn = driver.find_element_by_xpath(import_card_str +
#                                               '/../../android.view.View[5]/android.widget.TextView')

# 根据父子关系定位，全写
# card_create_btn = driver.find_element_by_xpath(import_card_str +
#                                                '/parent::android.view.View'
#                                                '/parent::android.view.View'
#                                                '/android.view.View[5]/android.widget.TextView')

# 根据兄弟关系定位
card_create_btn = driver.find_element_by_xpath(import_card_str +    # 定位儿子
                                               '/..'                # 根据儿子定位父亲
                                               '/preceding-sibling::android.view.View' # 根据父亲定位父亲的哥哥
                                               '/android.widget.TextView') # 哥哥的儿子

# 对于py-client来说，send_keys是模拟键盘输入，set_text是直接给值，没有按键过程
# card_name_input.send_keys("First Test Card")

# 因为Uiautomator2的问题，先click激活控件，再输入，否则输入不生效。不使用Uiautomator2则不需要多此一举。
card_name_input.click()
card_name_input.set_text("First Test Card")
card_pwd_input.click()
card_pwd_input.send_keys("123")
card_repeat_pwd_input.click()
card_repeat_pwd_input.send_keys("123123")
card_hint_input.click()
card_hint_input.send_keys("123123")
# 第一次click()是从输入框切换到相应的按钮，等于激活按钮，第二次才是真正的点击事件
card_create_btn.click()
card_create_btn.click()

toast_loc = ("xpath", ".//*[contains(@text,'卡片密码长度不应少于6个字符')]")
errMsg = WebDriverWait(driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc))

print("Msg is :", errMsg)

