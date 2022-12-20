from flask import Flask, render_template, url_for, request
import pandas as pd
import numpy as np
import source.connector as ct
import source.docreader as dr
from source.queries import parse_input, add_crime_ids, rem_attrs, dict_match_on_crime

app = Flask(__name__)

if __name__ == "__main__":
  app.run(debug=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form
        formfilters, queryfilters = parse_input(form)
        crime_db = ct.MongoConnector()
        mongo_db = crime_db.startup_db_client()
        crime_codes = dr.mongo_read()
        query = { '$and': [item for item in queryfilters] }
        # query = { '$and': [{"GEO_LAT": 39.7616457} , {"GEO_LON": -105.0241665}] }
        # query = { 'OFFENSE_CODE': 3501, 'OFFENSE_CODE_EXTENSION': 0}
        query_attributes = formfilters
        query_attributes = add_crime_ids(query_attributes)
        # query_attributes = None
        # query = { 'incident_id': 2017421909} 

        query_list = crime_codes.db_find(mongo_db, 'Crime', 'Denver_Crime', query, query_attributes)
        query_list = dict_match_on_crime(mongo_db,query_list,query_attributes)
        
        remove_attributes = ['OFFENSE_CODE', 'OFFENSE_CODE_EXTENSION', 'OFFENSE_TYPE_ID']
        query_list = rem_attrs(query_list, remove_attributes)

        if len(query_list) == 0:
            noquery = pd.DataFrame.from_dict([{'Welcome': 'queries.  Please enter a new query.'}])

            return render_template('index.html', tables = [noquery.to_html(classes="data")], titles=noquery.columns.values)
        # crime_codes.print_records(query_list)

        df = pd.DataFrame(query_list)
        df.fillna('', inplace=True)
        return render_template('index.html',  tables=[df.to_html(classes="data")], titles=df.columns.values)
    else:
        return render_template('index.html',  tables=[])


##Testing
# @app.route("/")
# def print_data():
#     crime_db = ct.MongoConnector()
#     mongo_db = crime_db.startup_db_client()
#     crime_codes = dr.mongo_read()
#     query = { '$and': [{"GEO_LAT": 39.7616457} , {"GEO_LON": -105.0241665}] }
#     # query = { 'OFFENSE_CODE': 3501, 'OFFENSE_CODE_EXTENSION': 0}
#     query_attributes = ['OFFENSE_TYPE_ID', 'FIRST_OCCURRENCE_DATE', 'INCIDENT_ADDRESS', 'NEIGHBORHOOD_ID']
#     # query_attributes = None
#     # query = { 'incident_id': 2017421909} 

#     query_list = crime_codes.db_find(mongo_db, 'Crime', 'Denver_Crime', query, query_attributes)

#     # crime_codes.print_records(query_list)

#     df = pd.DataFrame(query_list)
#     return render_template('index.html',  tables=[df.to_html(classes="data")], titles=df.columns.values)
