from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from config import phone
from time import sleep


class FitFormula:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://perm.24ff.ru/"

    def send_sms(self):
        btn = self.driver.find_element(By.CLASS_NAME, "user-info.profile.js-popup")
        self.driver.implicitly_wait(5)
        btn.click()
        reg_btn = self.driver.find_element(By.XPATH, f"""//*[@id="fancybox-container-1"]/div[2]/div[4]/div/div/form/div[4]/a[1]""")
        self.driver.implicitly_wait(5)
        reg_btn.click()
        input_phone = self.driver.find_element(By.ID, "phone_1")
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).send_keys_to_element(input_phone, self.phone).perform()
        consent_btn = self.driver.find_element(By.NAME, "policy")
        self.driver.implicitly_wait(5)
        ActionChains(self.driver).click(consent_btn).perform()
        send_sms_btn = self.driver.find_element(By.XPATH, f"""//*[@id="fancybox-container-2"]/div[2]/div[4]/div/div/form/div[4]/button""")
        self.driver.implicitly_wait(5)
        send_sms_btn.click()
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    formula = FitFormula(phone, driver)
    driver.get(formula.url)
    formula.send_sms()
