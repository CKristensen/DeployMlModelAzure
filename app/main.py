from fastapi import FastAPI
import tensorflow as tf
import os, uuid
from zipfile import ZipFile
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import logging

AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=goolit2;AccountKey=iOHs5Z9m+/S4doMBH5G/JQzbO/6vx+V6UiRw9FQw3gHypjLoZqu0tMvh9WOezkMWEBSyz+ZMaFcvjZyiMHft9Q==;EndpointSuffix=core.windows.net"


logging.basicConfig(filename="log.log", level=logging.INFO)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/sentence/{sentence}")
def get_prediction(sentence: str):
    logging.info('get prediction')
    connect_str = AZURE_STORAGE_CONNECTION_STRING
    
    logging.info('done1')
    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    logging.info('done2')
    # List the blobs in the container
    blob_client = blob_service_client.get_blob_client(container="model", blob="compressed_model.zip")
    
    logging.info('done3')
    stream = blob_client.download_blob()
    logging.info('done4')

    logging.info('Started get zip') 
    with open('cm.zip', 'ab') as fp:
        b = stream.content_as_bytes()
        fp.write(b)

    logging.info('Started open zip')
    with ZipFile('cm.zip') as myzip:
        myzip.extractall()
        model = tf.keras.models.load_model('.')
    

    logging.info('Starting prediction')
    return {'Sentence': str(sentence), 'Sentence score': str(float(model.predict([[sentence]])))}