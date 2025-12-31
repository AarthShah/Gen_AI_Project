from scrapping.Add_data_to_file import get_all_data_from_file
from chroma import add_sunbeam_data,add_file
from embedding import create_embedding
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_sunbeam_data():
    data=get_all_data_from_file()
    data = data.replace("ï¿½", "•")
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200,
                                                 separators=[
            "==================================================", # Primary break
            "\n# ",   # Course Title break
            "\n\n",   # Paragraph break
        ]
        # keep_separator=True 
        )
    
    docs=text_splitter.create_documents([data])
    return docs
print("Chunking Done...")

docs = chunk_sunbeam_data()
print("len of docs :",len(docs))
for doc in docs:
    # print("****"*30)
    print("\nChunk--> : ",doc)

                                                 