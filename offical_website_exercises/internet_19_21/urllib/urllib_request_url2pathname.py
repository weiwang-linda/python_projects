#Do some practice with url2pathname method of urllib.request module.

# para:    url : a file path url
# return:  The file path in your file system

# Convert the path component path from a percent-encoded URL to the local syntax for a path.  
# This does not accept a complete URL.
# This function uses unquote() to decode path. 


from urllib.request import url2pathname
from urllib.parse import unquote

url = "file:///home/weiwang/learn/python_projects/offical_website_exercises/internet_19_21/urllib/test%20for%20you/test.txt"

def read_file(filename):

	with open(filename) as f:

		for line in f:

			print(line)


if __name__ == '__main__':

	file_path = url2pathname(url)
	file_path = file_path.split('//')[-1]     #url2pathname(url) handles "%xx" except the "file://" string
	read_file(file_path)

	file_path2 = unquote(url)       #urllib.request.url2pathname(url) ==  urllib.parse.unquote(url)
	file_path2 = file_path2.split('//')[-1]  
	read_file(file_path2)