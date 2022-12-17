import pandas as pd
import connector as ct
from pprint import pprint

class read_doc():
    def __init__(self) -> None:
        # self.doc = pd.read_csv('data/crime.csv', encoding= 'ISO-8859-1').to_dict()
        pass
    def db_insert(self):
        pass


class mongo_read(read_doc):
    def __init__(self) -> None:
        super().__init__()

    def csv_to_json(self, filename):
        data = pd.read_csv(filename)
        datadict = data.to_dict()
        return data.to_dict()

    def print_records(self, query_results):
        for i, record in enumerate(query_list):
            print(f'Record number: {i}')
            pprint(record)
            print('\n')
        df = pd.DataFrame.from_dict(query_results)
        print(df)

    def db_insert_csv(self, filepath, dbname, colname, mongo_db):
        datadict = pd.read_csv(filepath, encoding= 'ISO-8859-1').to_dict()
        header = [header for header in datadict]
        db = mongo_db[dbname]
        col = db[colname]
        for i in datadict[header[0]]:
            row = {}
            for j in header:
                row[j] = datadict[j][i] ##{'Incident_number': 2134556}
            col.insert_one(row)

    def db_find(self, mongo_connect, dbname, colname, query, returnfields = None):
        if returnfields is not None:
            return_dict = {}
            return_dict['_id'] = False
            for item in returnfields:
                return_dict[item] = True
        else:
            return_dict = None
        
        db = mongo_connect[dbname]
        col = db[colname]
        query_results = col.find(query, return_dict)
        query_list = []
        for record in query_results:
            query_list.append(record)
        return query_list


crime_db = ct.MongoConnector()
mongo_db = crime_db.startup_db_client()
crime_codes = mongo_read()
query = { '$and': [{"GEO_LAT": 39.7616457} , {"GEO_LON": -105.0241665}] }
# query = { 'OFFENSE_CODE': 3501, 'OFFENSE_CODE_EXTENSION': 0}
query_attributes = ['OFFENSE_TYPE_ID', 'FIRST_OCCURRENCE_DATE', 'INCIDENT_ADDRESS', 'NEIGHBORHOOD_ID']
# query_attributes = None
# query = { 'incident_id': 2017421909}

query_list = crime_codes.db_find(mongo_db, 'Crime', 'Denver_Crime', query, query_attributes)

crime_codes.print_records(query_list)

## figure out how to sort by attribute




