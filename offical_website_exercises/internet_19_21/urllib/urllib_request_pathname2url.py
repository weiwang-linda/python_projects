#Do some practice with pathname2url method of urllib.request module.

# para:    path : a path string for file system
# return:  the path component of a URL

# This does not produce a complete URL. 
# The return value will already be quoted using the quote() function.
# Usually use with urllib.parse and os modules

# extension: For pdf file operations, reference https://pypi.python.org/pypi/python-poppler-qt5/

import os
from urllib import parse, request, error

def _get_file_url(filename):

	file_url = parse.urljoin('file:', 
		request.pathname2url(os.path.abspath(filename)))   #pathname2url return part of url

	return file_url

def open_file(filename):
	file_url = _get_file_url(filename)

	try:

		# print(file_url)
		# file:///home/weiwang/learn/python_projects/offical_website_exercises/internet_19_21/urllib/urllib_request_urlopen.py
		ret = request.urlopen(file_url).read().decode('utf-8')

	except error.URLError as ue:
		print(ue)

	return ret

if __name__ == '__main__':

	text = open_file('urllib_request_urlopen.py')
	import pprint
	pprint.pprint(text)
