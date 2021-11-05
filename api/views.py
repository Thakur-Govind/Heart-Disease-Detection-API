from django.shortcuts import render
from django.http import JsonResponse
import os.path
from .models import MlModel
# model imports
import pickle
import numpy as np

#def train_model():
def try_get_model(request):
    model = MlModel.objects.all()[0].model
    print(pickle.load(model.open()))
    return JsonResponse({"success":"model reached"})

def transform_data(data):
    return np.array(data).reshape(1,-1)
def api_hit(request,age,sex,trestbps,restecg,thalach):
    #filepath = os.path.abspath('finalized_RFC.sav')
    # f = open(filepath)
    model = MlModel.objects.all()[0].model
    rfc = pickle.load(model.open())
    print("Model Loaded Successfully")
    feed = [age,sex,trestbps,restecg,thalach]
    for i in feed:
        if i is None:
            return JsonResponse({"run":"failed","error":"One or more data values are NULL. Please check data and try again"})
        # if not isinstance(i,int):
        #     return JsonResponse({"run":"failed","error":"Invalid Data type in some value. Check data sent"})
    try:
        data = transform_data(feed)
        prediction = rfc.predict(data)
        health = ["normal","abnormal"]
        return JsonResponse({"run":"success","prediction":str(prediction[0]),"health":health[prediction[0]]})
    except:
        return JsonResponse({"run":"failed","error":"Unexpected Error. Please check model log"})


