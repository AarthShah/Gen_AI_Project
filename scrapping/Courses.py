from selenium import webdriver
from selenium.webdriver.common.by import By

def get_courses_link():
    driver = webdriver.Chrome()
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

    get_all_courses_data(dic,driver)
    return dic
        

    
    driver.quit()

def get_all_courses_data(dic,driver):
    for key,value in dic.iteams():
        get_coures_data(value,driver)


def get_coures_data(url,driver):
   
    doc=""
    driver.get(url)
    datas=driver.find_elements(By.TAG_NAME,"p")
    for data in datas:
        doc+=data.text
    print(doc)
    pannel=driver.find_elment(By.ID,"accordion")
if __name__ == "__main__":
    # get_courses_link()
    driver = webdriver.Chrome()
    get_coures_data("https://www.sunbeaminfo.in/modular-courses/apache-spark-mastery-data-engineering-pyspark",driver)
