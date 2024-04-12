from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from config import phone
from time import sleep


class Askona:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://www.askona.ru/"

    def send_sms(self):
        btn = self.driver.find_element(By.CLASS_NAME, "button.btn.HeaderAuth_button__3y4DG")
        self.driver.implicitly_wait(5)
        btn.click()
        input_phone = self.driver.find_element(By.ID, "phone")
        self.driver.implicitly_wait(5)
        input_phone.send_keys(self.phone + Keys.RETURN)
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    askona = Askona(phone, driver)
    driver.get(askona.url)
    askona.send_sms()