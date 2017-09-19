# sys_module.py sys解释器相关函数
# 该模块含有解释器的一些变量，与解释器交互的函数。

__author__ = "weiwang"
__date__ = 2017/9/15

import sys

def sys_attr_func():
	# Display platform and version
	platform = sys.platform
	max_int = sys.maxsize
	python_ver = sys.version

	print(platform, max_int, python_ver)

	# modules search path
	path0 = sys.path
	print("Module search path: ", path0)
	sys.path.append('/home/weiwang/learn')
	path1 = sys.path
	print("The changed path: ", path1)

	# hooks
	modules_map = sys.modules
	modules_name = list(sys.modules.keys())
	s = 'a'
	t = s
	n = t
	refcount = sys.getrefcount('a')
	builtin_module = sys.builtin_module_names
	print(modules_map)
	print(modules_name)
	print(refcount)
	print(builtin_module)

	# exception info
	try:
		raise IndexError
	except:
		print(sys.exc_info())

if __name__ == '__main__':
	sys_attr_func()