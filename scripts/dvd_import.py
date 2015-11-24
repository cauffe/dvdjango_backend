#!/usr/bin/env python

import csv
import sys
import os
from unidecode import unidecode

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Movie, MovieCas, Genre, Studio

#cassandra imports
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "dvd_csv.txt"

dvd_csv = os.path.join(dir_name, file_name)

csv_file = open(dvd_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:




    movie = MovieCas(title=unidecode(row['DVD_Title']), sql_id=int(new_movie.id))

    movie.save()
    cluster.shutdown()



    try:
        new_movie.save()
    except Exception, e:
        print "lol, no.."



