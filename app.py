import streamlit as st
import tiktoken
import dotenv
import llm


def run_app():
    #load API keys as global variables
    dotenv.load_dotenv()

    #define variables
    pages = []
    vectorstore = None
    
    st.title("My AI app")

    input = st.radio(
    "What would you like to query?",
    ["PDF file", "Website"])
    
    if input == 'PDF file':
        upload_pdf_flow()
    else:
        upload_url_flow()

    if st.button("Embed and store"):   
        #embeds splits in vectorstore
        vectorstore = llm.embed_and_store_splits(pages)
   
    #field to type question    
    placeholder = "Type here..."
    question = st.text_input(
        "Enter your question", placeholder
    )

    #query LLM only when question is submitted
    if question and question != placeholder:
        
        result = llm.queryPDF(vectorstore, question)
        st.write(result)

#retrurn number of tokens from string
def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

#return number of tokens from list
def num_tokens_from_list(pages):
    num_tokens = 0
    for i, page in enumerate(pages):
        num_tokens += num_tokens_from_string(page.page_content, "cl100k_base")
    st.write(f"Number of tokens in document: {num_tokens}")
    st.write(f"Cost to embed: ${num_tokens /1000 * 0.0001}")


def upload_pdf_flow():
    st.write("Ask a question to your PDF document")
    uploaded_file = st.file_uploader("Choose a file")

    #uploads file, saves to the disk and splits into list of pages
    if uploaded_file:
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        pages = llm.load_pdf_and_split(uploaded_file.name)
        num_tokens_from_list(pages)
        st.write(uploaded_file.name)
        st.write(pages)

def upload_url_flow():
    url = st.text_input("Enter URL")
    if url:
        pages = llm.load_url_and_split(url)
        num_tokens_from_list(pages)

if __name__ == "__main__":
    run_app()
