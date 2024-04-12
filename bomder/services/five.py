from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from config import phone


class Five:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://5ka.ru/my"

    def send_sms(self):
        input_phone = self.driver.find_element(By.ID, "username")
        self.driver.implicitly_wait(5)
        input_phone.send_keys(self.phone + Keys.RETURN)
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    five = Five(phone, driver)
    driver.get(five.url)
    five.send_sms()
