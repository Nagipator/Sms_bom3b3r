from selenium import webdriver
from selenium.webdriver.common.by import By
from config import phone
from time import sleep


class SportModa:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://perm.sportmoda.ru/"

    def send_sms(self):
        btn = self.driver.find_element(By.XPATH, f"""//*[@id="header"]/div[1]/div/div/div/div/div[2]/div/div/div/div/a""")
        self.driver.implicitly_wait(10)
        btn.click()
        sleep(5)
        reg_btn = self.driver.find_element(By.XPATH, f"""//*[@id="bxmaker-authuserphone-enter__ajax"]/div[1]/div[9]/a""")
        self.driver.implicitly_wait(5)
        reg_btn.click()
        input_phone = self.driver.find_element(By.XPATH, f"""//*[@id="bxmaker-authuserphone-enter__ajax"]/div[2]/div[2]/div/div/div[2]/input""")
        self.driver.implicitly_wait(10)
        input_phone.send_keys(self.phone)
        send_sms_btn = self.driver.find_element(By.XPATH, f"""//*[@id="bxmaker-authuserphone-enter__ajax"]/div[2]/div[2]/button/div""")
        self.driver.implicitly_wait(5)
        send_sms_btn.click()
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    sport = SportModa(phone, driver)
    driver.get(sport.url)
    sport.send_sms()
