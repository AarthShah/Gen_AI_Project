def add_to_file(data):
    with open("Scrapping.txt",mode="a") as f:
        f.write(data)

def delete_all_data_from_file():
    with open("Scrapping.txt",mode="w") as fp:
        fp.write("")

def get_all_data_from_file():
    with open("Scrapping.txt",mode="r") as f:
        text=f.read()   
    with open("Courses_Scrapping.txt",mode="r") as f:
        text_courses=f.read()
        return text , text_courses
    
def add_to_file_of_courses(data):
    with open("Courses_Scrapping.txt",mode="a") as f:
        f.write(data)

def get_all_data_from_course_file():
    with open("Courses_Scrapping.txt",mode="r") as f:
        text=f.read()
        return text
