import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from zipfile import ZipFile

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# List the blobs in the container
blob_client = blob_service_client.get_blob_client(container="model", blob="compressed_model.zip")
stream = blob_client.download_blob()


with open('compressed_model.zip', 'ab') as fp:
    # Using `get_blob_to_bytes`
    b = stream.content_as_bytes()
    fp.write(b)
    # Or using `get_blob_to_stream`
    # service.get_blob_to_stream(container_name, blob.name, fp)
