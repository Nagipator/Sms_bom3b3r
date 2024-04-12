from selenium import webdriver
from selenium.webdriver.common.by import By
from config import phone
from selenium.webdriver import ActionChains
from time import sleep


class Miuz:
    def __init__(self, phone, driver):
        self.phone = "8" + phone[2::]
        self.driver = driver
        self.url = "https://miuz.ru/auth/"

    def send_sms(self):
        input_phone = self.driver.find_element(By.ID, "PERSONAL_PHONE")
        self.driver.implicitly_wait(5)
        input_phone.click()
        input_phone.send_keys(self.phone)
        send_sms_button = self.driver.find_element(By.XPATH, f"""//*[@id="register-phone"]/button""")
        self.driver.implicitly_wait(5)
        ActionChains(self.driver).click(send_sms_button).perform()
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    miuz = Miuz(phone, driver)
    driver.get(miuz.url)
    miuz.send_sms()
