from selenium import webdriver
from selenium.webdriver.common.by import By
from config import phone
from time import sleep


class Donatello:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://donatello-pizza.ru/"

    def send_sms(self):
        menu_button = self.driver.find_element(By.CLASS_NAME, "top-line__burger-svg-wrap")
        self.driver.implicitly_wait(5)
        menu_button.click()
        entrance_button = self.driver.find_element(By.CLASS_NAME, "g-button.g-button_size_m.g-button_view_primary")
        self.driver.implicitly_wait(5)
        entrance_button.click()
        input_phone = self.driver.find_element(By.CLASS_NAME, "g-input__input")
        self.driver.implicitly_wait(5)
        input_phone.send_keys(self.phone)
        call_button = self.driver.find_element(By.CLASS_NAME, "g-tabs-tab.g-tabs-tab_authorization")
        self.driver.implicitly_wait(5)
        call_button.click()
        send_sms_button = self.driver.find_element(By.CLASS_NAME, "g-button.g-button_size_l.g-button_view_primary")
        self.driver.implicitly_wait(5)
        send_sms_button.click()
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    donatello = Donatello(phone, driver)
    driver.get(donatello.url)
    donatello.send_sms()
