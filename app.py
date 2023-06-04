import streamlit as st
import os
import pinecone

# Pinecone configuration
pinecone_index_name = "influential-americans"

# Set Pinecone API key
# os.environ["PINECONE_API_KEY"] = "YOUR_PINECONE_API_KEY"  # Update with your Pinecone API key

# Connect to the Pinecone index
pinecone.init(api_key='3b6e97c7-6444-48de-a432-fec85c1f80c5')
pinecone_index = pinecone.Index(index_name=pinecone_index_name)

def main():
    st.title("Influential African Americans Search")
    
    query = st.text_input("Enter a query")
    
    if query:
        response = search_influential_americans(query)
        format_output(response)

def search_influential_americans(query):
    try:
        response = pinecone_index.query(queries=[query], top_k=5)
        return response
    except pinecone.ApiException as e:
        st.error(f"An error occurred during the query: {e}")
        return None

def format_output(response):
    if not response or not response.ids:
        st.error("I am sorry, but your query is outside the boundaries of what I was trained on.")
    else:
        st.subheader("Response:")
        st.write(response)
        # Add any other desired formatting of the response

if __name__ == "__main__":
    main()
