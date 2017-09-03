#update_db_file.py

from make_db_file import storeDbase, loadDbase

db = loadDbase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
storeDbase(db)