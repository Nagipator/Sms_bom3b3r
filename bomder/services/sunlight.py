from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import phone
from time import sleep


class Sunlight:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://sunlight.net/profile/login/"

    def send_sms(self):
        input_phone = self.driver.find_element(By.CLASS_NAME, "login__steps-phone-input.login__steps-phone-input_incomplete")
        self.driver.implicitly_wait(5)
        input_phone.send_keys(self.phone + Keys.RETURN)
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    sunlight = Sunlight(phone, driver)
    driver.get(sunlight.url)
    sunlight.send_sms()
