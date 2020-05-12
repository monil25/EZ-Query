from flask import request
from flask import jsonify
from flask import Flask
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.model import Trainer
from rasa.nlu import config
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import re
from rasa.nlu.model import Metadata,Interpreter


trainer = Trainer(config.load("config.yml"))
model_directory = trainer.persist('./models/')
interpreter = Interpreter.load(model_dir='./models/nlu-6/nlu')



app = Flask(__name__)

@app.route("/predict", methods=["GET","POST"])
def predict():
    response = {}
    if request.method == "POST":
        imd = request.form
        params = imd.to_dict(flat=False)
        QUERY = params["QUERY"]

        response = interpreter.parse(QUERY[0])
        return jsonify(response)

    else:
        return jsonify({"Failed":"Not meant for this"})    

