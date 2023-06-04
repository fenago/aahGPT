import streamlit as st
from llama_index import GPTVectorStoreIndex
from llama_index.vector_stores import PineconeVectorStore

# Pinecone configuration
pinecone_index_name = "influential-americans"
pinecone_index_environment = "asia-southeast1-gcp"  # Update with your Pinecone environment

# Set Pinecone API key
os.environ["PINECONE_API_KEY"] = "YOUR_PINECONE_API_KEY"  # Update with your Pinecone API key

# Connect to the existing Pinecone index
vector_store = PineconeVectorStore(
    index_name=pinecone_index_name,
    environment=pinecone_index_environment
)

# Create GPTVectorStoreIndex
city_index = GPTVectorStoreIndex(vector_store=vector_store)

def main():
    st.title("Influential African Americans Search")
    
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
