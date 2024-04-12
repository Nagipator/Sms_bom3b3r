from selenium import webdriver
from selenium.webdriver.common.by import By
from config import phone
from time import sleep


class VkusVill:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.mail = "elisa3@awgarstone.com"
        self.url = "https://prm.vkusvill.ru/"

    def send_sms(self):
        btn = self.driver.find_element(By.XPATH, f"""//*[@id="js-header"]/div/div[2]/div/div/div[6]/a""")
        self.driver.implicitly_wait(5)
        btn.click()
        input_phone = self.driver.find_element(By.NAME, "USER_PHONE")
        self.driver.implicitly_wait(5)
        input_phone.send_keys(self.phone)
        send_sms_btn = self.driver.find_element(By.XPATH, f"""//*[@id="js-user-form-login-api"]/div[5]/button""")
        self.driver.implicitly_wait(5)
        send_sms_btn.click()
        try:
            input_name = self.driver.find_element(By.XPATH, f"""//*[@id="js-user-name-form-login-api-value"]""")
            self.driver.implicitly_wait(10)
            input_name.send_keys("Пётр")
            input_mail = self.driver.find_element(By.XPATH,
                                                  f"""//*[@id="js-user-name-form-login-api"]/div[3]/div/div/input""")
            self.driver.implicitly_wait(10)
            input_mail.send_keys(self.mail)
            reg_btn = self.driver.find_element(By.XPATH, f"""//*[@id="js-user-name-form-login-api"]/div[5]/button""")
            self.driver.implicitly_wait(5)
            reg_btn.click()
        except:
            pass
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    vkusvill = VkusVill(phone, driver)
    driver.get(vkusvill.url)
    vkusvill.send_sms()
