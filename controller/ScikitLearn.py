from flask import Blueprint, request, jsonify
import service.ScikitLearn as service

aiApp = service.ScikitLearn()

class ScikitLearnAiClass(object):

    controller = Blueprint("scikit", __name__, url_prefix="/api/ai/sklearn")

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
    
    @controller.route("/accuracy")
    def accuracyAi():
        aiApp.accuracy()
        return '200 OK\n'

    @controller.route("/predict", methods=['POST'])
    def predict():
        data = request.get_json('param')
        print(dict(data).get('param'))
        prediction = aiApp.predict(dict(data).get('param'))
        return f'{{"prediction":"{prediction}"}}'
