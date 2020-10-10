FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN pip install update
RUN export AZURE_STORAGE_CONNECTION_STRING="YOU NEED TO ENTER YOUR AZURE CONNECTION STRING HERE"

COPY ./app /app