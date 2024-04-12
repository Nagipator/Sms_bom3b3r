from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import phone
from time import sleep


class CleverFish:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://clever-fish.ru/"

    def send_sms(self):
        btn = self.driver.find_element(By.CLASS_NAME, "s1enqr8f")
        self.driver.implicitly_wait(5)
        btn.click()
        input_phone = self.driver.find_element(By.XPATH,
                                               f"""//*[@id="modal-container"]/div[2]/div/div/div[2]/form/label/input""")
        self.driver.implicitly_wait(10)
        input_phone.click()
        input_phone.send_keys(self.phone + Keys.RETURN)
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    cleverfish = CleverFish(phone, driver)
    driver.get(cleverfish.url)
    cleverfish.send_sms()
