from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import phone
from time import sleep


class Sokolov:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://sokolov.ru/"

    def send_sms(self):
        sleep(3)
        button = self.driver.find_elements(By.CLASS_NAME,
                                           "ButtonDeprecated_sklv-button__Wy8xr.ButtonTemplate_button__mMa6w.HeaderTop_header-top_right-icon__tvD5b")
        self.driver.implicitly_wait(5)
        button[2].click()
        input_phone = self.driver.find_element(By.CLASS_NAME, "_Input_input__7xcBD._Input_input_normal__YCHcN")
        self.driver.implicitly_wait(5)
        input_phone.click()
        input_phone.send_keys(self.phone + Keys.RETURN)
        send_sms_button = self.driver.find_element(By.CLASS_NAME,
                                                   "Button_button__ZFztY.Button_primary__GMkKG.Button_main__3GiUm.Button_m__97u33.LoginPhone_auth-btn__1ZgRw")
        self.driver.implicitly_wait(5)
        send_sms_button.click()
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    sokolov = Sokolov(phone, driver)
    driver.get(sokolov.url)
    sokolov.send_sms()
