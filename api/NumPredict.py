import os
import json
from flask_restful import Resource
from flask import request
import logging as logger
import keras
import numpy
import tensorflow
from keras import backend as K
from .LoadedModel import loaded_model,graph

class NumPredict(Resource):
    
    def post(self):
        pixelArr = json.loads(request.get_json()['number'])
        npArr = numpy.zeros((784,))

        for i in pixelArr:
            npArr[int(i)] = (float(pixelArr[i]) / 255)

        reshapedNpArr = npArr.reshape(1,28,28,1)
        with graph.as_default():
            prediction = loaded_model.predict(reshapedNpArr)
        response = {
            "prediction": str(prediction.argmax())
        }
        return response,200







