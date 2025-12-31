import chromadb 
db1=chromadb.PersistentClient(path="./Uploaded_file")
content_file=db1.get_or_create_collection("File_Uploaded")

db=chromadb.PersistentClient(path="./Sunbeam_data")
content_scraping=db.get_or_create_collection("Sunbeam_web_data")

def add_file(ids,vectordb,metadata):
    try:
        content_file.add(ids=ids,embeddings=vectordb,metadatas=metadata)
        return "file added"
    except Exception:
        return "failed to Add Data"
    
def add_sunbeam_data(ids,vectordb,metadata):
    content_scraping.add(ids=ids,embeddings=vectordb,metadatas=metadata)
    return "Scrapping Done"

def delete_data(id,options="file"):
    if options=="file":
        try :
            content_file.delete(ids=[id])
            return "deleted successfully"
        except Exception :
            return "failed to Detete"
    else:
        try :
            content_scraping.delete(ids=[id])
            return "deleted successfully"
        except Exception :
            return "failed to Detete"

def update_data(id,vectordb,metadata,option="file"):
    if option=="file":
        try:
            delete_data(id,option)
            content_file.add(ids=id,embeddings=vectordb,metadatas=metadata)
            return "Updated Sucessfully.."
        except Exception :
            return "Failed to Update.."
    else:
        try:
            delete_data(id,option)
            content_scraping.add(ids=id,embeddings=vectordb,metadatas=metadata)
            return "Updated Sucessfully.."
        except Exception :
            return "Failed to Update.."


def get_data_for_Embed_query(Equery,option="file"):
    if option=="file":
        result=content_file.query(query_embeddings=Equery,n_results=3,)
    else:
        result=content_scraping.query(query_embeddings=Equery,n_results=3,)
    return result