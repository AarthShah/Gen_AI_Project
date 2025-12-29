from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv()

llm=init_chat_model(
    model="moonshotai/kimi-k2-instruct-0905",
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("Groq_Api")
    )

agent = create_agent(model=llm)

def chat_model(messages):
    st.session_state.conversation.append({"role": "user", "content": messages})
    result=agent.invoke({"messages": st.session_state.conversation})
    print("Agent: ", result['messages'][-1].content)
    return result['messages'][-1].content

if __name__ == "__main__":
    Conversation=[]
    while True:
        Conversation.append({"role": "user", "content": input("User: ")})
        result=agent.invoke({"messages": Conversation})
        print("Agent: ", result['messages'][-1].content)