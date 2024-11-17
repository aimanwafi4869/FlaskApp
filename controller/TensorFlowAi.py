from flask import Blueprint, request, jsonify
import service.TensorFlow as service

aiApp = service.TensorFlow()

class TensorFlowAiClass(object):

    controller = Blueprint("ai", __name__, url_prefix="/api/ai")

    @controller.route("/initialize")
    def initializeAi():
        aiApp.a = 'initialize'
        return 'initialize'

    @controller.route("/change/<value>")
    def changeAi(value):
        aiApp.a = value
        return aiApp.a
    
    @controller.route("/testBody", methods=['POST'])
    def bodyAi():
        data = request.json
        aiApp.a = data
        return aiApp.a
    
    @controller.route("/print")
    def valueAi():
        return aiApp.a
    
    @controller.route("/train")
    def trainAi():
        return aiApp.train()