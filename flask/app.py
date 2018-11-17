import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/NSFData.sqlite"
db = SQLAlchemy(app)

# create database model
class NSF(db.Model):
  __tablename__ = "NSF"

  Id = db.Column(db.Integer, primary_key = True)
  NSFName = db.Column(db.String)
  RDINST = db.Column(db.String)
  UnitId = db.Column(db.String)
  Year = db.Column(db.String)
  AcademicDiscipline = db.Column(db.String)
  FedFinancedSERD = db.Column(db.Integer)
  StateFinancedSERD = db.Column(db.Integer)
  BusinessFinancedSERD = db.Column(db.Integer)
  InstitutionFinancedSERD = db.Column(db.Integer)
  OtherFinancedSERD = db.Column(db.Integer)
  TotalSERDExpenditures = db.Column(db.Integer)
  ARRAFinancedRD = db.Column(db.Integer)
  StateFinancedRD = db.Column(db.Integer)
  BusinessFinancedRD = db.Column(db.Integer)
  NonProfitFinancedRD = db.Column(db.Integer)
  InstitutionFinancedRD = db.Column(db.Integer)
  OtherFinancedRD = db.Column(db.Integer)
  ForeignFinancedRD = db.Column(db.Integer)
  ContractFinancedRD = db.Column(db.Integer)
  GrantFinancedRD = db.Column(db.Integer)
  MedSchoolRDExpenditures = db.Column(db.Integer)
  ClinicalTrialRDExpenditures = db.Column(db.Integer)
  FedFinancedClinicalTrialRDExpenditures = db.Column(db.Integer)
  EquipmentRDExpenditures = db.Column(db.Integer)
  FedFinancedEquipmentRDExpenditures = db.Column(db.Integer)
  TotalRDExpenditures = db.Column(db.Integer)

  def __repr__(self):
    return '<Institution %r>' % (self.NSFName)

    # Create tables
@app.before_first_request
def setup():
  db.create_all()

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/NSFName")
def NSFName_data():
  """return NSFName and expenditures"""

    # Query for the top 10 emoji data
    results = db.session.query(NSF.NSFName, NSF.TotalRDExpenditures).\
      order_by(NSF.Year.desc()).\
      limit(10).all()

    # Create lists from the query results
    Name = [result[0] for result in results]
    Exp = [int(result[1]) for result in results]

    # Generate the plot trace
    trace = {
        "x": Name,
        "y": Exp,
        "type": "bar"
    }
    return jsonify(trace)


if __name__ == '__main__':
    app.run(debug=True)
