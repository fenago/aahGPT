import streamlit as st
from llama_index import GPTVectorStoreIndex

# Load your Pinecone index
index_name = "influential-americans"
city_index = GPTVectorStoreIndex()

def main():
    st.title("Influential African Americans GPT")
    
    query = st.text_input("Enter a query")
    
    if query:
        response = city_index.query(query)
        format_output(response)

def format_output(response):
    if not response or not response.get_formatted_sources():
        st.error("I am sorry, but your query is outside the boundaries of what I was trained on.")
    else:
        st.subheader("Response:")
        st.write(response)
        st.subheader("Formatted Sources:")
        st.write(response.get_formatted_sources())

if __name__ == "__main__":
    main()
