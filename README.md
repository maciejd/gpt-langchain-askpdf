# gpt-langchain-askpdf
Simple GPT apllication allowing you to query your own PDF file. Uses streamlit for UI, ChromaDB to store embeddings and langchain.

## How to run it?
1. Create `.env` file in root directory of the project with the following contents. Replace OpenAI key with your own.
```
OPENAI_API_KEY="YOUR_API_KEY"
```
2. Run docker compose in detached mode `docker-compose up -d` 
3. Open [http://localhost:8000](http://localhost:8000)


## How does it work?
1. Loads file using streamlit
2. Splits pdf into chunks using langchain splitter
3. Generates embeddings using `text-embedding-ada-002`
4. Stores embeddings in an in-memory instance of ChromaDB vector database
5. Runs a RAG chain that will rertieve relevant splits and adds them to the context of a final prompt

## More info
The app leverages Retrieval-augmented generation (RAG). More info can be found [here](https://python.langchain.com/docs/use_cases/question_answering/)
