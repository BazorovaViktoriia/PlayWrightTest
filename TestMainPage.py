import time
import configparser

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

config = configparser.ConfigParser()
config.read("settings.ini")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(config.get("Settings", "url"))

try:
    wait = WebDriverWait(driver, 2)
    buttonAuthoriz = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/header/div[1]/article/button[1]"))).click()

    time.sleep(2)
    assert driver.current_url == config.get('Settings', 'url_login'), (f"Текущий URL ({driver.current_url}) не "
                                                                       f"соответствует ожидаемому ({config.get('Settings', 'url_login')})")

    wait = WebDriverWait(driver, 5)
    inputMail = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/section/div[1]/div[2]/form/fieldset/fieldset[1]/fieldset/div/div/input")))
    inputMail.send_keys(config.get("Settings", "e_mail"))

    inputPassword = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/section/div[1]/div[2]/form/fieldset/fieldset[2]/fieldset/div/div[1]/input")))
    inputPassword.send_keys(config.get("Settings", "password"))

    buttonEntryToSystem = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/section/div[1]/div[2]/form/div[2]/button"))).click()
    buttonChooseFilial = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/section/div[1]/div[2]/form/div/div/buttonvv"))).click()

    time.sleep(6)
    assert driver.current_url == config.get('Settings', 'url_myAccount'), (f"Текущий URL ({driver.current_url}) не "
                                                                       f"соответствует ожидаемому ({config.get('Settings', 'url_myAccount')})")

except TimeoutException as e:
    print("Произошла ошибка ожидания при поиске элемента:", e)

finally:
    driver.quit()
