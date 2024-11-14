import FlaskWrapper as wrapper
from flask import Flask 
from controller import Api
from controller import AI

flaskApp = Flask(__name__)

app = wrapper.FlaskWrapper(flaskApp)


# app.addEnpoint('/api', 'api', Api, methods=['GET'])

app.registerBlueprint(Api.controller, url_prefix='/api/rest')
app.registerBlueprint(AI.controller, url_prefix='/api/ai')

if __name__ == '__main__':
    app.run(debug=True)