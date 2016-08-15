#!flask/bin/python
from app import app
# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return "This is home!"
# # start the server
# if __name__== "__main__":
app.run(debug=True, port=5000)



