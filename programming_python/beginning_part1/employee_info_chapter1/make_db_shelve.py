#make_db_shelve.py

from initdata import bob, sue
import shelve
db = shelve.open('people-shelve')
print(db)
db['bob'] = bob
db['sue'] = sue
db.close()