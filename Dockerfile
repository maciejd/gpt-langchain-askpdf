FROM python:3.9-slim

# create directory for app
WORKDIR /app

RUN apt-get update

# expose default port for streamlit
EXPOSE 8501

# copy requirements
COPY requirements.txt ./requirements.txt

# install pip and required packages
RUN pip3 install -r requirements.txt

# copy project files
COPY app.py ./app.py
COPY llm.py ./llm.py
COPY .env ./.env 

# launch app
CMD streamlit run app.py
