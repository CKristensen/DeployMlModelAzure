# DeployMlModelAzure
FastAPI container running on an Azure ACI that get predictions from a saved .pb TensorFlow Model in another Azure Storage Container.

We’re going to use an Azure Container Instance to host an API that serves our machine learning model for predictions. 
The model is stored as a Tensorflow SavedModel, and outputs the predicted sentiment (positive/negative) for an input sentence. 

/status: Should return a short message if the API is reachable and working.
/predict: Runs a sentiment prediction.
/refresh: Loads a newer model from Azure Storage. 

Note: If you want to run this please create you own model and upload it to your own Azure ACI. 
I only used the free tier in Azure to experiment with it.

Also edit the Dockerfile and set the correct path in the env variable.



