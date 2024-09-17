from flask import Flask, Blueprint, request, jsonify
# from waitress import serve
# from flask_cors import CORS

#Blueprints
from controller.service_provider_api import sevice_provider_api_bp
# from controllers.login import member_api_bp

app = Flask(__name__)
CORS(app)

#register Blueprints
app.register_blueprint(sevice_provider_api_bp)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5001, debug=True) #run on local port
    # serve(app, host='0.0.0.0',port=5001, debug=True)
