from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from config import phone
from time import sleep


class ChetireLapy:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://4lapy.ru/personal/register/"

    def send_sms(self):
        reg_btn = self.driver.find_element(By.ID, "websiteElement-start-registration-by-phone")
        self.driver.implicitly_wait(5)
        reg_btn.click()
        input_phone = self.driver.find_element(By.ID, "phone-number")
        self.driver.implicitly_wait(5)
        input_phone.send_keys(self.phone)
        send_sms_btn = self.driver.find_element(By.ID, "websiteElement-send-phone-button")
        self.driver.implicitly_wait(5)
        ActionChains(self.driver).click(send_sms_btn).perform()   #Это реально работает!!!!
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    lapy = ChetireLapy(phone, driver)
    driver.get(lapy.url)
    lapy.send_sms()

