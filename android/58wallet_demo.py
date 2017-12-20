

from appium import webdriver


desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = '/Users/xiongyang/Desktop/钱包项目/APP/58wallet_android_1.0.0/58wallet_1.0.0_official.apk'


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print(driver.install_app(desired_caps['app']))
