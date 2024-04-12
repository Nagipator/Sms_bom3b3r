from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import phone
from time import sleep


class Polaris:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://shop-polaris.ru/"

    def send_sms(self):
        button = self.driver.find_element(By.CLASS_NAME, "d-none.d-lg-inline-block")
        self.driver.implicitly_wait(5)
        button.click()
        input_phone = self.driver.find_element(By.CLASS_NAME, "auth__input")
        self.driver.implicitly_wait(5)
        input_phone.send_keys(self.phone + Keys.RETURN)
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    polaris = Polaris(phone, driver)
    driver.get(polaris.url)
    polaris.send_sms()
