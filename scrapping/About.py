from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from Add_data_to_file import add_to_file

# TODO add headless to this 
def About_us():
    driver=webdriver.Chrome()
    driver.get("https://www.sunbeaminfo.in/about-us")
    driver.implicitly_wait(5)
    doucment=""
    wait=WebDriverWait(driver,5)

    wait.until(
        ec.presence_of_all_elements_located(
        ( By.CLASS_NAME,'panel-title')
            )
        )


    element=driver.find_element(By.CLASS_NAME,'panel-title')
    element.click()
    driver.execute_script("window.scrollBy(0, 300);")
    # element1=element.find_element(By.ID,'headingOne')
    sunbeam=driver.find_elements(By.TAG_NAME,"p")
    for i in sunbeam:
        text=i.text.strip()
        if text:
            doucment+=text
    # time.sleep(5)
    add_to_file("# About Sunbeam \n \n ")
    add_to_file(doucment)
    driver.quit()

if __name__=="__main__":
    About_us()