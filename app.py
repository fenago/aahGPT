import streamlit as st
import pinecone

# Get Pinecone API key and environment from Streamlit secrets
pinecone_api_key = st.secrets["pinecone"]["api_key"]
pinecone_environment = st.secrets["pinecone"]["environment"]

# Authenticate with Pinecone
pinecone.init(api_key=pinecone_api_key, environment=pinecone_environment)

# Pinecone index name
index_name = "influential-americans"

# Check if the index exists
if index_name in pinecone.list_indexes():
    st.write(f"The index '{index_name}' exists.")
else:
    st.write(f"The index '{index_name}' does not exist.")

# Create an interface to query the index
query_input = st.text_input("Enter your query:")

if query_input:
    # Create a pinecone query
    query_result = pinecone.deployment(index_name).query(queries=[query_input], top_k=10)
    
    # Show the result
    for item in query_result.results:
        st.write(item.id, item.score)
else:
    st.write("Please enter a query.")
