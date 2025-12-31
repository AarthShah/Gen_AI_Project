import streamlit as st
from Agent  import chat_model



def show_chat_history():
     st.title("Risey AI ..")
     for i in st.session_state.conversation:
          print(i)
          
          if i["role"]=="user":
                st.chat_message("user").write(i["content"])
          elif i["role"]=="assistant":
                st.chat_message("assistant").write(i["content"])

def chat_screen():
    show_chat_history()
    input=st.chat_input("You: ", key="input_message")
    # uploaded_pdf = st.file_uploader(
    #     "Upload PDF",
    #     type=["pdf"],
    #     key="pdf_file"
    # )
    if input:
        st.chat_message("user").write(input)
        response=chat_model(input)
        st.chat_message("ai").write(response)



# def first_chat_message(message):
#         st.chat_message("user").write(message)
#         print(message)
#         response=chat_model(message)
#         print(response)
#         st.chat_message("ai").write(response)


# if __name__=="__main__":
#      first_chat_message("hi")