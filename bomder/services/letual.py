from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from config import phone
from time import sleep


class Letual:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://www.letu.ru/"

    def send_sms(self):
        btn = self.driver.find_element(By.CLASS_NAME, "header-v4-box.header-v4-box--with-welcome")
        self.driver.implicitly_wait(5)
        ActionChains(self.driver).click(btn).perform()
        btn1 = self.driver.find_element(By.XPATH, f"""//*[@id="header"]/div[2]/div/div/div[3]/a/div[2]/div[1]/button/span/span""")
        self.driver.implicitly_wait(5)
        ActionChains(self.driver).click(btn1).perform()
        input_phone = self.driver.find_element(By.CLASS_NAME, "le-input__field-input")
        self.driver.implicitly_wait(5)
        ActionChains(self.driver).click(input_phone).perform()
        ActionChains(self.driver).send_keys_to_element(input_phone, self.phone).perform()
        sleep(10)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    letual = Letual(phone, driver)
    driver.get(letual.url)
    sleep(3)
    letual.send_sms()
