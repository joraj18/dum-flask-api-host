from flask import Flask, Blueprint, request, jsonify
import json

from db.db import SmartInsuranceDatabase

# Create a Blueprint instance for the member API
sevice_provider_api_bp= Blueprint("serviceProviderAPI",__name__)


#Create member API route
@sevice_provider_api_bp.route('/', methods=['GET'])
def home():
    return "Hi"

@sevice_provider_api_bp.route('/getAllServiceProviders', methods=['GET'])
def service_provider_get():
    obj=SmartInsuranceDatabase()
    data=obj.get_all_serviceprovider()
    return jsonify(data)
