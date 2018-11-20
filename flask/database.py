from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime

engine = create_engine('sqlite:///NSF_data.db')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class NSF(Base):
  __tablename__ = "NSF"
  
  index = Column(Integer, primary_key=True)
  Id = Column(String)
  NSFName = Column(String)
  RDINST = Column(String)
  UnitId = Column(String)
  Year = Column(String)
  AcademicDiscipline = Column(String)
  FedFinancedSERD = Column(Integer)
  StateFinancedSERD = Column(Integer)
  BusinessFinancedSERD = Column(Integer)
  InstitutionFinancedSERD = Column(Integer)
  OtherFinancedSERD = Column(Integer)
  TotalSERDExpenditures = Column(Integer)
  ARRAFinancedRD = Column(Integer)
  StateFinancedRD = Column(Integer)
  BusinessFinancedRD = Column(Integer)
  NonProfitFinancedRD = Column(Integer)
  InstitutionFinancedRD = Column(Integer)
  OtherFinancedRD = Column(Integer)
  ForeignFinancedRD = Column(Integer)
  ContractFinancedRD = Column(Integer)
  GrantFinancedRD = Column(Integer)
  MedSchoolRDExpenditures = Column(Integer)
  ClinicalTrialRDExpenditures = Column(Integer)
  FedFinancedClinicalTrialRDExpenditures = Column(Integer)
  EquipmentRDExpenditures = Column(Integer)
  FedFinancedEquipmentRDExpenditures = Column(Integer)
  TotalRDExpenditures = Column(String)



Base.metadata.create_all(bind=engine)