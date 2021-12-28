from flask import Flask
import csv

app = Flask(__name__)

@app.route('/pacientes', methods=[GET])
def pacientes():
    pass

def pacientesCsv():
    pass