import os, streamlit as st
import pinecone
from langchain.llms.openai import OpenAI
from llama_index import LLMPredictor, ServiceContext

# Streamlit Secrets
pinecone_api_key = st.secrets["pinecone"]["api_key"]
pinecone_environment = st.secrets["pinecone"]["environment"]
openai_api_key = st.secrets["openai"]["api_key"]

# Pinecone index name
index_name = "influential-americans"

# Define a simple Streamlit app
st.title("Ask Llama about African American History")
query = st.text_input("What would you like to ask?", "")

# If the 'Submit' button is clicked
if st.button("Submit"):
    if not query.strip():
        st.error(f"Please provide the search query.")
    else:
        # Initialize Pinecone
        pinecone.init(api_key=pinecone_api_key, environment=pinecone_environment)

        # Check if the index exists
        if index_name not in pinecone.list_indexes():
            st.error(f"The index '{index_name}' does not exist.")
        else:
            try:
                # This example uses gpt-4 by default; feel free to change if desired
                llm_predictor = LLMPredictor(llm=OpenAI(api_key=openai_api_key, temperature=0, model_name="gpt-4"))

                # Connect to the existing Pinecone index
                index = pinecone.Index(index_name)

                # Query and retrieve the response
                query_result = index.query(queries=[query], top_k=10)
                st.success(query_result)
            except Exception as e:
                st.error(f"An error occurred: {e}")
