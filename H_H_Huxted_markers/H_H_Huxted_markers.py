import sys
import psycopg2, psycopg2.extras
import pymssql
from collections import namedtuple
from datetime import datetime
from shapely import wkt
import time
import datetime
import timeit
from configparser import ConfigParser, ConfigParser
from osgeo import ogr
import  csv

########################################################
def read_csv_file(csv_file, dest_db_name):

    parser = ConfigParser()
    parser.read('defaults.cfg')

    dest_db = parser.get(dest_db_name.upper(), 'db')
    dest_host = parser.get(dest_db_name.upper(), 'host')    
    dest_user = parser.get(dest_db_name.upper(), 'user')
    dest_passwd = parser.get(dest_db_name.upper(), 'passwd')

    with open(csv_file) as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in csvreader:
            print ("%s %s %s " % (row[4], row[15], row[16]))
            name=row[4]
            lat=float(row[15])
            lon=float(row[16])

            point = ogr.Geometry(ogr.wkbPoint)
            point.AddPoint(lat, lon)
            pointWKT=point.ExportToWkt()

            print(pointWKT)

            # parse fields | 
            
            # open connection to dest_db_name
            with pymssql.connect(host=dest_host, database=dest_db, user=dest_user, password=dest_passwd) as ins_con:
                with ins_con.cursor() as ins_cur:
                    last_marker_id = str(ins_con.execute("SELECT @@Identity").fetchone()[0])

            # insert into markersn cust_1282?

            # insert into markers_attribute

            # insert into markers_geofence

#######################################################
def main():
    start_time = datetime.datetime.now()
    print("Start Time %s " % (start_time))
    if len(sys.argv) != 3:
        print ('Usage: wrong number of arguements')
        exit(1)

    csv_file=sys.argv[1]
    dest_db_name=sys.argv[2]

    read_csv_file(csv_file, dest_db_name)
    print ("DONE")

############################################
#
#  Main
############################################
if __name__ == '__main__':
    
    main()