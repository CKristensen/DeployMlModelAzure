# DeployMlModelAzure
FastAPI container running on an Azure ACI that get predictions from a Model in another Azure Storage Container.

We’re going to use an Azure Container Instance to host an API that serves our machine learning model for predictions. 
The model is stored as a Tensorflow SavedModel, and outputs the predicted sentiment (positive/negative) for an input sentence. 

/status: Should return a short message if the API is reachable and working.
/predict: Runs a sentiment prediction.
/refresh: Loads a newer model from Azure Storage. 


