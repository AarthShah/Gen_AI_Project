from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
import time
from Add_data_to_file import add_to_file
# TODO add headless to this 
def get_pre_cat_data():
    doc=""
    options_chrome=webdriver.ChromeOptions()
    options_chrome.add_argument("--headless=new")
    options_chrome.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options_chrome)
    driver.get("https://www.sunbeaminfo.in/pre-cat")
    driver.implicitly_wait(5)

    wait=WebDriverWait(driver,2)

    adds=driver.find_element(By.XPATH,"//div[@class='df-btn-text df-btn-text-icon-only']")
    adds.click()

    items=["Course Contents","Eligibility Criteria","Pre-CAT Batches schedule"]

    for item in items:
        element = driver.find_element(By.LINK_TEXT, item)
        element.click()
        # time.sleep(1)

        data = driver.find_elements(
                By.XPATH, "//div[contains(@class,'collapse in')]//li"
            )
        if data:
            doc+=(f" \n --- {item} for Pre-Cat: \n ")
            for i in data:
                
                doc+=(f"{i.text}\n")

        else:
            table = driver.find_element(
                By.XPATH, "//div[contains(@class,'collapse in')]//table"
            )
            headers = table.find_elements(By.TAG_NAME, "th")
            header_names = [h.text.strip() for h in headers]
            doc+=(f"{item}:\n")
            doc+=(f"\ncolumes Per-cat : {header_names}\n ")

            rows = table.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                cols = row.find_elements(By.TAG_NAME, "td")
                if cols:
                    doc += f"row Per-cat : {[col.text.strip() for col in cols]}\n"




    add_to_file("\n \n # Pre-Cat(Preparatory Course for Entrance)\n")
    add_to_file(doc)

    # time.sleep(5)
    driver.quit()


if __name__=="__main__":
    get_pre_cat_data()