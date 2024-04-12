from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import phone
from time import sleep


class KB:
    def __init__(self, phone: str, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://krasnoeibeloe.ru/auth/?register=yes"

    def send_sms(self):
        input_phone = self.driver.find_element(By.CLASS_NAME, "phone-field__input")
        self.driver.implicitly_wait(5)
        input_phone.send_keys(self.phone + Keys.RETURN)
        yes_button = self.driver.find_element(By.CLASS_NAME, "btn.btn_red.age_popup_btn.age_popup_btn--agree")
        self.driver.implicitly_wait(5)
        yes_button.click()
        send_sms_button = self.driver.find_element(By.CLASS_NAME, "phone-field__send.phone-field__send--long")
        self.driver.implicitly_wait(5)
        send_sms_button.click()
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    kb = KB(phone, driver)
    driver.get(kb.url)
    kb.send_sms()
