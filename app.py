# Import the dependencies.
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from flask import Flask,jsonify
import datetime as dt
app = Flask(_name_)

#################################################
# Database Setup
#################################################

engine = create_engine('sqlite:///Resources/hawaii.sqlite', connect_args={'check_same_thread': False}, echo=True)

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
measurement=Base.classess.measurement
station=Base.classes.station

# Create our session (link) from Python to the DB
Session=sessionmker(bind=engine)
session=Session()

#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
