#make_db_pickle.py

from initdata import db
import pickle

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()