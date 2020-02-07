from flask import jsonify
from google.cloud import storage
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

bucket_name = '<your bucket name>'

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    
    storage_client = storage.Client()

    bucket=storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs(prefix='iris_model/iris_classifer.sav')
    for blob in blobs:
        model_str_downloaded = blob.download_as_string()
        pickled = pickle.loads(model_str_downloaded)



    
    
    request_json = request.get_json()
    
    
    X = [request_json['predict']]
    
    if request_json and 'predict' in request_json:
        return jsonify({"result": int(pickled.predict(X)[0])})
    else:
        return jsonify({"reponse": "error"})
