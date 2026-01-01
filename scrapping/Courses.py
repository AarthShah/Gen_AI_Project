from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
from Add_data_to_file import add_to_file_of_courses

def get_courses_link():
    options_chrome=webdriver.ChromeOptions()
    options_chrome.add_argument("--headless=new")
    options_chrome.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options_chrome)
    driver.get("https://www.sunbeaminfo.in/modular-courses-home")
    driver.implicitly_wait(5)

    boxes = driver.find_elements(By.CLASS_NAME, "c_cat_box")
    dic={}
    for box in boxes:
        try:
            title = box.find_element(By.TAG_NAME, "h4").text.strip()
        except:
            title = box.find_element(By.TAG_NAME, "h5").text.strip()

        url = box.find_element(By.CLASS_NAME, "c_cat_more_btn").get_attribute("href")

        print(f"{title} : {url}\n")
        dic[title]=url

    # content=get_all_courses_data(dic,driver)
    # add_to_file_of_courses("\n \n # Modular Courses \n")
    # add_to_file_of_courses(content)
    # return content
        

def get_all_courses_data(dic,driver):
    contents=""
    for key,value in dic.items():
        contents+=get_coures_data(value,driver,key)
    driver.quit()
    return contents
    


def get_coures_data(url,driver,key):
    driver.get(url)
    WebDriverWait(driver, 2)
    content=""
    content+=("="*50)
    content+=f"\n# {key} \n "
    time.sleep(3)
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
        course_info_box = driver.find_element(By.CLASS_NAME, "course_info")
        elements = course_info_box.find_elements(By.CSS_SELECTOR, "h3, p, li, span")
        if elements:
            content += f"\n--- Overview / Introduction about {key}\n"
            for info in elements:
                content += f"{info.text}\n"
    except Exception as e:
        print(f"Error scraping main info: {e}")

    panels = driver.find_elements(By.CSS_SELECTOR, "#accordion .panel")
    for panel in panels:
            try:
                header = panel.find_element(By.CLASS_NAME, "panel-heading")
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", header)
                header.click()
                time.sleep(0.5) 

                content += f"\n--- {header.text} for {key}\n"

                list_items = panel.find_elements(By.TAG_NAME, "li")
                if list_items:
                    for item in list_items:
                        content += f"• {item.text} for {key}\n"

                table_rows = panel.find_elements(By.TAG_NAME, "tr")
                if table_rows:
                    headers = panel.find_elements(By.TAG_NAME, "th")
                    if headers:
                        header_names = [h.text.strip() for h in headers]
                        content += f"Columns for {key}: {header_names}\n"
                    for row in table_rows:
                        cols = row.find_elements(By.TAG_NAME, "td")
                        if cols:
                            row_data = [col.text.strip() for col in cols]
                            content += f"Row for {key}: {row_data}\n"

                paragraphs = panel.find_elements(By.TAG_NAME, "p")
                if paragraphs:
                    for p in paragraphs:
                        if p.text.strip(): 
                            content += f"{p.text}\n"

            except Exception as e:
                print(f"Error scraping a panel: {e}")

    return content
if __name__ == "__main__":
    md=get_courses_link()
    # driver = webdriver.Chrome()
    # #md=get_coures_data("https://www.sunbeaminfo.in/modular-courses/apache-spark-mastery-data-engineering-pyspark",driver,"Apache Spark Mastery - Data Engineering with PySpark")
    # dic={"Apache Spark Mastery - Data Engineering with PySpark": 'https://www.sunbeaminfo.in/modular-courses/apache-spark-mastery-data-engineering-pyspark',
    #      "Data Science Mastery - Data Analysis & Visualization with Python": 'https://www.sunbeaminfo.in/modular-courses/data-science-mastery-data-analysis-visualization-python',
    #      "Full Stack Web Development Mastery - MERN Stack": 'https://www.sunbeaminfo.in/modular-courses/full-stack-web-development-mastery-mern-stack'}
    # md=get_all_courses_data(dic,driver)  
    # # md=get_coures_data("https://www.sunbeaminfo.in/internship",driver,"Internship")  
    print(md)
