#dump_db_pickle_recs.py

import pickle, glob
for file in glob.glob('*.pkl'):
	# print(file)
	recfile = open(file, 'rb')
	record = pickle.load(recfile)
	print(file.split('.')[0], '=>\n', record)
	recfile.close()


suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])
suefile.close()