from flask_restful import Resource
import logging as logger

class ProjectAPI(Resource):

    def get(self):

        projectDetails = {
                "version" : "1",
                "owner" : "hkovesdi",
                "projectName" : "Handwritten digit recognizer API"
        }


        return projectDetails,200







