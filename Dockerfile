FROM python:3.9-slim

# making directory of app
WORKDIR /app

RUN apt-get update

# exposing default port for streamlit
EXPOSE 8501

# copy over requirements
COPY requirements.txt ./requirements.txt

# install pip then packages
RUN pip3 install -r requirements.txt

# copying all files over
#COPY . .
COPY app.py ./app.py
COPY llm.py ./llm.py
COPY .env ./.env 

# cmd to launch app when container is run
CMD streamlit run app.py
