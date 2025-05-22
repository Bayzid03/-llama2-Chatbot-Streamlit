from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

# Configuring LangChain
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Initializing the Streamlit page
st.title('Langchain Demo With LLAMA2 API')

# Creating the chain
try:
    llm = Ollama(model="llama2")
    chain = (
        ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant. Please response to the user queries"),
            ("user", "Question:{question}")
        ])
        | llm
        | StrOutputParser()
    )
except Exception as e:
    st.error(f"Error initializing LLM: {str(e)}")
    st.stop()

# User input
input_text = st.text_input("Search the topic you want")

# Processing input and displaying response
if input_text:
    try:
        with st.spinner('Generating response...'):
            response = chain.invoke({"question": input_text})
            st.write(response)
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")