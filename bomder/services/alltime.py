from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import phone
from time import sleep


class Alltime:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://www.alltime.ru/"

    def send_sms(self):
        button = self.driver.find_element(By.XPATH, f"""/html/body/div[2]/header/div[3]/div/div/div[2]/div/span/span""")
        self.driver.implicitly_wait(5)
        button.click()
        input_phone = self.driver.find_element(By.NAME, "phone")
        self.driver.implicitly_wait(5)
        input_phone.send_keys(self.phone)
        send_sms_btn = self.driver.find_element(By.XPATH, f"""//*[@id="frmPhoneRegister"]/div[3]/button""")
        self.driver.implicitly_wait(5)
        send_sms_btn.click()
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    alltime = Alltime(phone, driver)
    driver.get(alltime.url)
    alltime.send_sms()
