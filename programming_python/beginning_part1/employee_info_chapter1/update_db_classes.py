#update_db_classes.py

import shelve
db = shelve.open('class-shelve')
sue = db['sue']
sue.giveRaise(0.25)
db['sue'] = sue

tom = db['tom']
tom.giveRaise(.20)
db['tom'] = tom
db.close()