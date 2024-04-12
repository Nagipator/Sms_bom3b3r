from selenium import webdriver
from selenium.webdriver.common.by import By
from config import phone
from time import sleep


class MirHvostatih:
    def __init__(self, phone, driver):
        self.phone = phone[2::]
        self.driver = driver
        self.url = "https://ekb.mirhvost.ru/auth/?register=yes#"

    def send_sms(self):
        reg_btn = self.driver.find_element(By.XPATH,
                                           f"""//*[@id="bxmaker-authuserphone-call--tQqfSa"]/div[3]/div[1]/div[5]/div""")
        self.driver.implicitly_wait(5)
        reg_btn.click()
        input_phone = self.driver.find_element(By.XPATH,
                                               f"""//*[@id="bxmaker-authuserphone-call__input-register_phonetQqfSa"]""")
        self.driver.implicitly_wait(5)
        input_phone.click()
        input_phone.send_keys(self.phone)
        send_sms_btn = self.driver.find_element(By.XPATH,
                                                f"""//*[@id="bxmaker-authuserphone-call--tQqfSa"]/div[3]/div[2]/div[5]/div/div""")
        self.driver.implicitly_wait(5)
        send_sms_btn.click()
        yes_btn = self.driver.find_element(By.XPATH, f"""/html/body/div[1]/div/div[3]/span[2]""")
        self.driver.implicitly_wait(5)
        yes_btn.click()
        sleep(3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    mir = MirHvostatih(phone, driver)
    driver.get(mir.url)
    mir.send_sms()
