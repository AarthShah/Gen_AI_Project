def add_to_file(data):
    with open("Scrapping.txt",mode="a") as f:
        f.write(data)

def delete_all_data_from_file():
    with open("Scrapping.txt",mode="w") as fp:
        fp.write("")

def get_all_data_from_file():
    with open("Scrapping.txt",mode="r") as f:
        text=f.read()
        return text
