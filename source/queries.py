import source.connector as ct

def parse_input(form):
        headers = { 'fid': "_id",
                    'fii': "incident_id",
                    'foi': "offense_id",
                    'foc': "OFFENSE_CODE",
                    'foce': "OFFENSE_CODE_EXTENSION",
                    'foti': "OFFENSE_TYPE_ID",
                    'foci': "OFFENSE_CATEGORY_ID",
                    'ffod': "FIRST_OCCURRENCE_DATE",
                    'flod': "LAST_OCCURRENCE_DATE",
                    'frd': "REPORTED_DATE",
                    'fia': "INCIDENT_ADDRESS",
                    'fgx': "GEO_X",
                    'fgy': "GEO_Y",
                    'fglong': "GEO_LON",
                    'fglat': "GEO_LAT",
                    'fdi': "DISTRICT_ID",
                    'fpi': "PRECINCT_ID",
                    'fni': "NEIGHBORHOOD_ID",
                    'fic': "IS_CRIME",
                    'fit': "IS_TRAFFIC",
                    'fvc': "VICTIM_COUNT" }
        queryterms = { 'id': "_id",
                    'ii': "incident_id",
                    'oi': "offense_id",
                    'oc': "OFFENSE_CODE",
                    'oce': "OFFENSE_CODE_EXTENSION",
                    'oti': "OFFENSE_TYPE_ID",
                    'oci': "OFFENSE_CATEGORY_ID",
                    'fod': "FIRST_OCCURRENCE_DATE",
                    'lod': "LAST_OCCURRENCE_DATE",
                    'rd': "REPORTED_DATE",
                    'ia': "INCIDENT_ADDRESS",
                    'gx': "GEO_X",
                    'gy': "GEO_Y",
                    'glong': "GEO_LON",
                    'glat': "GEO_LAT",
                    'di': "DISTRICT_ID",
                    'pi': "PRECINCT_ID",
                    'ni': "NEIGHBORHOOD_ID",
                    'ic': "IS_CRIME",
                    'it': "IS_TRAFFIC",
                    'vc': "VICTIM_COUNT" }
        queryfilters, formfilters = [], []
        for item in form:
            if form[item] == 'y' and item in headers:
                formfilters.append(headers[item])
            elif item in queryterms:
                if item in ['vc','ii','oc','oce','gx','gy','glong','glat','di','pi','ic','it']:
                    queryfilters.append({queryterms[item]: int(form[item])})
                else:
                    queryfilters.append({queryterms[item]: form[item]})
        return formfilters,queryfilters