from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from Add_data_to_file import add_to_file


def get_internship_data():
    options_chrome=webdriver.ChromeOptions()
    options_chrome.add_argument("--headless=new")
    options_chrome.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options_chrome)
    driver.get("https://www.sunbeaminfo.in/internship")
    driver.implicitly_wait(5)
    time.sleep(2) 

    content = ""
    try:
        add=driver.find_element(By.CLASS_NAME, "df-btn-text-icon-only")
        if add:
            add.click()
        else :
            time.sleep(2)
            add=driver.find_element(By.CLASS_NAME, "df-btn-text-icon-only")
            add.click()   

    except Exception as e:
        print(f"Error clicking add button: {e}")

    try:
        main_info = driver.find_element(By.CLASS_NAME, "main_info")
        content += "--- OVERVIEW about Internship\n"
        content += str(main_info.get_attribute("innerText")) + "\n\n"
    except:
        print("Overview not found.")

    panels = driver.find_elements(By.CSS_SELECTOR, "#accordion .panel")
    for panel in panels:
            try:
                header = panel.find_element(By.CLASS_NAME, "panel-heading")
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", header)
                header.click()
                time.sleep(0.5) 

                content += f"\n--- {header.text} for Internship\n"

                list_items = panel.find_elements(By.TAG_NAME, "li")
                if list_items:
                    for item in list_items:
                        content += f"• {item.text}\n"

                table_rows = panel.find_elements(By.TAG_NAME, "tr")
                if table_rows:
                    headers = panel.find_elements(By.TAG_NAME, "th")
                    if headers:
                        header_names = [h.text.strip() for h in headers]
                        content += f"Columns for Internship: {header_names}\n"
                    for row in table_rows:
                        cols = row.find_elements(By.TAG_NAME, "td")
                        if cols:
                            row_data = [col.text.strip() for col in cols]
                            content += f"Row for Internship: {row_data}\n"

                paragraphs = panel.find_elements(By.TAG_NAME, "p")
                if paragraphs:
                    for p in paragraphs:
                        if p.text.strip(): 
                            content += f"{p.text}\n"
            except Exception as e:
                print(f"Error scraping a panel: {e}")
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2) 

        content += f"--- SCHEDULE for Internship \n"

        table_box = driver.find_element(By.CLASS_NAME, "table-responsive")
        
        rows = table_box.find_elements(By.TAG_NAME, "tr")
        
        for row in rows:
            cols = row.find_elements(By.XPATH, ".//td | .//th")

            row_data = []
            for col in cols:
                if col:
                    row_data.append(str(col.get_attribute("innerText")).strip())

            content += " | ".join(row_data) + "\n"

    except Exception as e:
        print(f"Error reading schedule table: {e}")
    add_to_file("\n \n # Internship \n")
    add_to_file(content)
    driver.quit()
    # return content

if __name__ == "__main__":
    data = get_internship_data()
    print(data)