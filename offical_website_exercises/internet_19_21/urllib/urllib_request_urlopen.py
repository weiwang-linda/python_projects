#Do some practice with urlopen method of urllib.request module.

# para:    "url" : a string or Request object
# para:    others : have default value

# HTTP/1.1 and includes Connection:close header in its HTTP requests.

# Always returns a "http.client.HTTPResponse" object which can work as a context manager and has methods such as:
# >>> dir(html)
#['begin', 'chunk_left', 'chunked', 'close', 'closed', 'code', 'debuglevel', 'fileno', 'flush', 
#'fp', 'getcode', 'getheader', 'getheaders', 'geturl', 'headers', 'info', 'isatty', 'isclosed', 
#'length', 'msg', 'read', 'readable', 'readall', 'readinto', 'readline', 'readlines', 'reason', 
#'seek', 'seekable', 'status', 'tell', 'truncate', 'url', 'version', 'will_close', 'writable', 
#'writelines']

# Raises URLError on protocol errors.

from urllib.request import urlopen
import pprint

URLS = ('https://github.com',)

def displayHeaders(url):
	http_response = urlopen(url)
	if not http_response:
		print("No handler handle this request!")
	else:
		print(http_response.geturl())
		pprint.pprint(dict(http_response.getheaders()))

def urlrequest_success(url):
	http_response = urlopen(url)
	print(http_response.__class__.__name__)
	if http_response.msg == 'OK' and http_response.getcode() == 200:
	#if http_response.reason == 'OK' and http_response.status == 200:
		print("The url is requested successfully!")
	else:
		print("The url is requested fail!")

def get_htmltype(url):
	try:
		http_response = urlopen(url)
		content_type = http_response.getheader('Content-Type').split(';')
		print(content_type)
	except URLError as e:
		print(e)

def search_sourcecode(url):
	try:
		http_response = urlopen(url)   # return a iteral object,context manager
	except URLError as e:
		print(e)
	with http_response as response:
		for line in response:
			line = line.decode('utf-8')
			if 'Sign up for GitHub' in line:
				print(line)

def download_webpage(url):
	try:
		http_response = urlopen(url)
	except URLError as e:
		print(e)
	content = http_response.read()     #return a bytestream
	print(content.decode(http_response.info().get_content_charset()))   # decode to string

if __name__ == '__main__':
	for url in URLS:
		displayHeaders(url)
		urlrequest_success(url)
		get_htmltype(url)
		search_sourcecode(url)
		download_webpage(url)