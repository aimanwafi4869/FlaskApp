from flask import Blueprint, request, jsonify
import service.ScikitLearn as service

dataset = 'dataset/fish_landings.csv'
modelType = 'linearRegression'
aiApp = service.ScikitLearn(modelType,dataset)

class ScikitLearnAiClass(object):

    controller = Blueprint("scikit", __name__, url_prefix="/api/ai/sklearn")

    @controller.route("/change/<value>")
    def changeAi(value):
        aiApp.a = value
        return aiApp.a
    
    @controller.route("/testBody", methods=['POST'])
    def bodyAi():
        data = request.json
        aiApp.a = data
        return aiApp.a
    
    @controller.route("/train")
    def trainAi():
        return aiApp.train()
    
    @controller.route("/accuracy")
    def accuracyAi():
        return aiApp.accuracy()

    @controller.route("/predict", methods=['POST'])
    def predict():
        data = request.get_json('date')
        print(dict(data).get('date'))
        prediction = aiApp.predict(dict(data).get('date'))
        return f'{{"prediction":"{prediction}"}}\n'
