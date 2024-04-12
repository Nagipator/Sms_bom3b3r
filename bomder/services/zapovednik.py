from selenium import webdriver
from selenium.webdriver.common.by import By
from config import phone
from time import sleep


class Zapovednik:
    def __init__(self, phone, driver):
        self.phone = phone[3::]
        self.driver = driver
        self.mail = "elisa3@awgarstone.com"
        self.url = "https://perm.zapovednik96.ru/auth/"

    def send_sms(self):
        reg_btn = self.driver.find_element(By.ID, "tab-phone_login_method")
        self.driver.implicitly_wait(5)
        reg_btn.click()
        reg_btn1 = self.driver.find_element(By.CLASS_NAME, "site-link.text-branded.pointer")
        self.driver.implicitly_wait(5)
        reg_btn1.click()
        sleep(3)
        sms_btn = self.driver.find_element(By.CLASS_NAME, "auth-tabs_sms")
        self.driver.implicitly_wait(5)
        sms_btn.click()
        input_name = self.driver.find_element(By.XPATH,
                                              f"""//*[@id="__layout"]/div/main/div/div/div[1]/div/div[2]/form/div[1]/div/div/input""")
        self.driver.implicitly_wait(5)
        input_name.send_keys("Fuf Dad Bad")
        input_phone = self.driver.find_element(By.XPATH,
                                               f"""//*[@id="__layout"]/div/main/div/div/div[1]/div/div[2]/form/div[3]/div/div/input""")
        self.driver.implicitly_wait(5)
        input_phone.send_keys(self.phone)
        input_mail = self.driver.find_element(By.XPATH,
                                              f"""//*[@id="__layout"]/div/main/div/div/div[1]/div/div[2]/form/div[4]/div/div[1]/input""")
        self.driver.implicitly_wait(5)
        input_mail.send_keys(self.mail)
        send_sms_btn = self.driver.find_element(By.CLASS_NAME, "site-button.text-normal.default.responsive")
        self.driver.implicitly_wait(5)
        send_sms_btn.click()
        sleep(5)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    zap = Zapovednik(phone, driver)
    driver.get(zap.url)
    zap.send_sms()
