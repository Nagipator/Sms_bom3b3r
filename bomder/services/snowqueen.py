from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import phone
from time import sleep


class Snowqueen:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://snowqueen.ru/registration/"

    def send_sms(self):
        sleep(5)
        input_phone = self.driver.find_element(By.ID, "telephone")
        self.driver.implicitly_wait(5)
        input_phone.send_keys(self.phone + Keys.RETURN)
        send_sms_button = self.driver.find_element(By.CLASS_NAME,
                                              "no-outline.button-full.block.w-100.py15.weight-400.white-button.col-xs-6.h50.fs16.relative")
        self.driver.implicitly_wait(5)
        send_sms_button.click()
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    snow = Snowqueen(phone, driver)
    driver.get(snow.url)
    snow.send_sms()
