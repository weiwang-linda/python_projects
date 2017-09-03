#make_db_pickle_recs.py

from initdata import db, sue, tom
import pickle
for key in db:
	dbfile = open(key+'.pkl', 'wb')
	pickle.dump(db[key], dbfile)
	dbfile.close()