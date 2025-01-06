from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base # changed to below
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

# create engine object to connect to the task_database
# username: 'cf-python', password: 'password', hostname: 'localhost', database name: 'task_datbase'
engine = create_engine("mysql+pymysql://cf-python:password@localhost/task_database")

