import wrapper.Flask as wrapper
from flask import Flask 
from controller import Api
from controller.TensorFlowAi import TensorFlowAiClass
from controller.Ultralytics import UltralyticsAiClass
from controller.ScikitLearn import ScikitLearnAiClass

flaskApp = Flask(__name__)

app = wrapper.FlaskWrapper(flaskApp)

# app.addEnpoint('/api', 'api', Api, methods=['GET'])

app.registerBlueprint(Api.controller, url_prefix='/api/rest')
app.registerBlueprint(TensorFlowAiClass.controller, url_prefix='/api/ai')
app.registerBlueprint(UltralyticsAiClass.controller, url_prefix='/api/ai/ultra')
app.registerBlueprint(ScikitLearnAiClass.controller, url_prefix='/api/ai/sklearn')

if __name__ == '__main__':
    app.run(debug=True)