FROM python:3.9-slim

WORKDIR /tmp/work

COPY requirements.txt ${PWD} 

RUN pip install -r requirements.txt \
    && apt-get update && apt-get install -y git 
