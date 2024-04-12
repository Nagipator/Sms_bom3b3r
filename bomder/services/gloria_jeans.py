from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import phone
from time import sleep


class GloriaJeans:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://www.gloria-jeans.ru/"

    def send_sms(self):
        button = self.driver.find_element(By.CLASS_NAME, "main-menu-mobile-user__icon")
        self.driver.implicitly_wait(5)
        button.click()
        input_phone = self.driver.find_element(By.CLASS_NAME, "input.input--phone")
        self.driver.implicitly_wait(5)
        input_phone.send_keys(self.phone + Keys.RETURN)
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    gloria = GloriaJeans(phone, driver)
    driver.get(gloria.url)
    gloria.send_sms()
