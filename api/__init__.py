from flask_restful import Api
from app import flaskAppInstance

from .ProjectAPI import ProjectAPI
from .NumPredict import NumPredict

restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(NumPredict,"/predict")
restServerInstance.add_resource(ProjectAPI,"/")
