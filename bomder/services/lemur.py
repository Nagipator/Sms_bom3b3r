from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import phone
from time import sleep


class Lemur:  # Тут надо ждать 1 минуту(
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://lemurrr.ru/registration-card"

    def send_sms(self):
        input_phone = self.driver.find_element(By.XPATH,
                                               f"""//*[@id="bonusCardsNumberForm"]/div[1]/div[2]/div/label[1]/input""")
        self.driver.implicitly_wait(5)
        input_phone.click()
        input_phone.send_keys(self.phone + Keys.RETURN)
        send_sms_button = self.driver.find_element(By.CLASS_NAME, "btn.btn_save_1")
        self.driver.implicitly_wait(5)
        send_sms_button.click()
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    lemur = Lemur(phone, driver)
    driver.get(lemur.url)
    lemur.send_sms()
