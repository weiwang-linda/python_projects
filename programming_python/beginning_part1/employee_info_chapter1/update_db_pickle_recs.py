#update_db_pickle_recs.py

import pickle
subfile = open('sue.pkl','rb')
sue = pickle.load(subfile)
subfile.close()
sue['pay'] *= 1.10
subfile = open('sue.pkl', 'wb')
pickle.dump(sue, subfile)
subfile.close()