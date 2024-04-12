from bomder.functions.config import sites_for_main_users, sites_for_premium_users
from selenium import webdriver


async def send_sms(phone, user_role):
    driver = webdriver.Chrome()
    driver.maximize_window()
    ready_services = []
    if user_role == "premium_user":
        for servis in sites_for_premium_users:
            ready_services.append(servis(phone, driver))
    else:
        for servis in sites_for_main_users:
            ready_services.append(servis(phone, driver))
    for site in ready_services:
        try:
            driver.get(site.url)
            site.send_sms()
        except:
            print("Неудача", type(site))
    driver.quit()
    driver.close()
