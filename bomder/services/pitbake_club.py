from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import phone
from time import sleep


class PitbakeClub:
    def __init__(self, phone, driver):
        self.phone = "8" + phone[2::]
        self.driver = driver
        self.url = "https://pitbikeclub.ru/lk?act=reg"

    def send_sms(self):
        input_phone = self.driver.find_element(By.ID, "login")
        self.driver.implicitly_wait(5)
        input_phone.send_keys(self.phone + Keys.RETURN)
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    pit = PitbakeClub(phone, driver)
    driver.get(pit.url)
    pit.send_sms()
