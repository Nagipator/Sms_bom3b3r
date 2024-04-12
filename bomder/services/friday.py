from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import phone
from time import sleep


class Friday:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://fridaywear.ru/auth/"

    def send_sms(self):
        sleep(2)
        input_phone = self.driver.find_element(By.ID, "phone-number")
        self.driver.implicitly_wait(5)
        input_phone.send_keys(self.phone + Keys.RETURN)
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    friday = Friday(phone, driver)
    driver.get(friday.url)
    friday.send_sms()
