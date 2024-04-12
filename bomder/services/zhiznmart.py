from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import phone
from time import sleep


class Zhiznmart:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://lifemart.ru/ekb/blyuda/10000"

    def send_sms(self):
        sleep(8)
        yes_button = self.driver.find_element(By.CLASS_NAME,
                                              "default-button.city-select-first-step__button.primary.size-m")
        self.driver.implicitly_wait(5)
        yes_button.click()
        auth_button = self.driver.find_element(By.CLASS_NAME, "auth")
        self.driver.implicitly_wait(5)
        auth_button.click()
        input_phone = self.driver.find_element(By.CLASS_NAME, "input-form__input.phone")
        self.driver.implicitly_wait(5)
        input_phone.send_keys(self.phone + Keys.RETURN)
        call_button = self.driver.find_element(By.CLASS_NAME, "confirm-phone__btn.confirm-phone__call")
        self.driver.implicitly_wait(5)
        call_button.click()
        send_sms_button = self.driver.find_element(By.CLASS_NAME, "default-button.primary.size-m")
        self.driver.implicitly_wait(5)
        send_sms_button.click()
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    zhizn = Zhiznmart(phone, driver)
    driver.get(zhizn.url)
    zhizn.send_sms()
