from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import phone
from time import sleep


class Citilink:
    def __init__(self, phone, driver):
        self.phone = phone[1::]
        self.driver = driver
        self.url = "https://www.citilink.ru/"

    def send_sms(self):
        entrance = self.driver.find_element(By.CLASS_NAME, "css-1vb2hqj.e38q5fc0")
        self.driver.implicitly_wait(2)  # gives an implicit wait for 20 seconds
        entrance.click()
        registration = self.driver.find_element(By.CLASS_NAME, "ewr1ly40.css-17dwi0d.e4mggex0")
        self.driver.implicitly_wait(2)  # gives an implicit wait for 20 seconds
        registration.click()
        input = self.driver.find_element(By.NAME, "auth-by-registration_phone")
        self.driver.implicitly_wait(2)
        input.send_keys(self.phone + Keys.RETURN)
        sleep(2)
        confirm = self.driver.find_element(By.CLASS_NAME, "e4uhfkv0.css-r11k3.e4mggex0")
        self.driver.implicitly_wait(2)
        confirm.click()
        sleep(2)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    citilink = Citilink(phone, driver)
    driver.get(citilink.url)
    citilink.send_sms()
