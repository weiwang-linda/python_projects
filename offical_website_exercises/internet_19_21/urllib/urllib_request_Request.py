# Do some practice with Request class of urllib.request module.

# para:		url : a string of valid url
# 			data: an object with specificate data.(include bytes, file-like objects, and iterables)
# 			header: a dictionary
#			origin_req_host: the request-host of the origin transaction, it defaults to http.cookiejar.request_host(self)
#			unverifiable: defautl is False
#			method: string, indicates the HTTP request method that will be used.

# return:	Request object

# For an HTTP POST request method, data should be a buffer in the standard 
# application/x-www-form-urlencoded format. The urllib.parse.urlencode() function takes a 
# mapping or sequence of 2-tuples and returns an ASCII string in this format. It should be 
# encoded to bytes before being used as the data parameter.

# An appropriate Content-Type header should be included if the data argument is present. 
# If this header has not been provided and data is not None, 
# Content-Type: application/x-www-form-urlencoded will be added as a default.

# An unverifiable request is one whose URL the user did not have the option to approve.


from urllib.request import urlopen, Request, build_opener
import urllib
import pprint

url_cgi = "http://localhost/cgi-bin/cgi101.py"
params = urllib.parse.urlencode({'user': 'bob'})

def for_cgi(url):
	req = Request(url=url, data=b'some data')    #data should not be string
	html = urlopen(req)
	print(html.status, html.msg)
	html = html.read().decode(html.info().get_content_charset())
	pprint.pprint(html)

def add_header():
	opener = build_opener()               #build_opener usage
	opener.addheaders = [('User-agent', 'Mozilla/5.0'),]
	html = opener.open("http://www.baidu.com")

	req = Request("https://www.github.com")
	req.add_header('Refer','http://www.python.org')    #add_header for Request
	urlopen(req)

def para_get(para):
	f = urlopen("http://localhost/cgi-bin/cgi101.py?%s" % params)
	print(f.read().decode('utf-8'))

def para_post(url, para):
	req = Request(url=url)
	req.add_header("Content-Type",
	"application/x-www-form-urlencoded;charset=utf-8")    #POST method must make data to this type
	para = para.encode('utf-8')      #str.encode() make str to bytes
	f = urlopen(req, para)           #put data in urlopen function
	print(f.read().decode('utf-8'))

	req2 = Request(url=url, data=para)    #put data in Request class constractor
	ff = urlopen(req2)
	print(ff.read().decode('utf-8'))


if __name__ == '__main__':
	for_cgi(url_cgi)
	add_header()
	para_get(params)
	para_post(url_cgi, params)