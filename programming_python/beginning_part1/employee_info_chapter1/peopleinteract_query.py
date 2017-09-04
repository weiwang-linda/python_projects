#peopleinteract_query.py

import shelve
fieldnames = ('name','age','job','pay')
maxfield = max(len(f) for f in fieldnames)

db = shelve.open('class-shelve')

while True:
	key = input('\nkey? => ')
	if not key: break
	try:
		record = db[key]
	except :
		print("No such key %s!" %key)
	else:
		for field in fieldnames:
			print(field.rjust(maxfield), '=>', getattr(record,field))
			# print(field, '=>', record[field])  #TypeError: 'Person' object is not subscriptable

db.close()