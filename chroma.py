import chromadb 
content=None
content_scraping=None
def add_file(ids,vectordb,metadata):
    try:
        db=chromadb.PersistentClient(path="./Uploaded_file")
        content=db.get_or_create_collection("File_Uploaded")
        content.add(ids=ids,embeddings=vectordb,metadatas=metadata)
        return "file added"
    except Exception:
        return "failed to Add Data"
    
def add_sunbeam_data(ids,vectordb,metadata):
    db=chromadb.PersistentClient(path="./Sunbeam_data")
    content_scraping=db.get_or_create_collection("Sunbeam_web_data")
    content_scraping.add(ids=ids,embeddings=vectordb,metadatas=metadata)
    return "Scrapping Done"

def delete_data(id,options=add_file):
    try :
        options.delete(ids=[id])
        return "deleted successfully"
    except Exception :
        return "failed to Detete"

def update_data(id,vectordb,metadata,option=add_file):
    try:
        delete_data(id,option)
        option.add(ids=id,embeddings=vectordb,metadatas=metadata)
        return "Updated Sucessfully.."
    except Exception :
        return "Failed to Update.."


def get_data_for_Embed_query(Equery,option=add_file):
    result=option.query(query_embeddings=Equery,n_results=3,)
    return result