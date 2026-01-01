from About import About_us
from intership import get_internship_data
from Courses import get_courses_link
from pre_cat import get_pre_cat_data
from  Add_data_to_file import delete_all_data_from_file



def reload_scrapping():
    delete_all_data_from_file()
    try:
        About_us()
        get_internship_data()
        get_pre_cat_data()
        get_courses_link()
        rag=Rag_process()
        if rag == "Rag Process Done":
            return "Scrapping Completed" 
        else:
            return "Scrapping Failed in Rag Process"
    except Exception as e:
        return f"An error occurred: {e}"
    

def Rag_process():
    from Rag import chunk_sunbeam_data
    result=chunk_sunbeam_data()
    if result:
        return "Rag Process Done"
    return "Rag Process Failed"

if __name__ == "__main__":
    result = reload_scrapping()
    print(result)