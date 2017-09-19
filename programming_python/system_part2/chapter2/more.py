"""
分割字符串或文本文件并交互地进行分页显示.
只针对文本文件，pdf文件需要用其他模块读取。

"""

__author__ = "weiwang"
__date__ = 2017/9/15

def more(text, numlines=15):
	lines = text.splitlines()

	while lines:
		chunk = lines[:numlines]
		lines = lines[numlines:]
		for line in chunk:
			print(line)
		if lines and input('more?') not in ['Y','y']:
			break


if __name__ == '__main__':
	import sys
	more(open(sys.argv[1]).read(), 10)