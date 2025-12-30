from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Chrome()

driver.get("https://www.sunbeaminfo.in/")
driver.implicitly_wait(5)
wait=WebDriverWait(driver,5)

# <a href="pre-cat" >
driver.execute_script("window.scrollBy(0, 800);")
driver.find_element(By.XPATH, "//a[@href='pre-cat'][normalize-space()='View More']").click()


time.sleep(5)
driver.close()




