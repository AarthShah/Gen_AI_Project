from About import About_us
from intership import get_internship_data
from Courses import get_courses_link



def reload_scrapping():
    try:
        About_us()
        get_internship_data()
        get_courses_link()
        return "Scrapping Completed" 
    except Exception as e:
        return f"An error occurred: {e}"
    

