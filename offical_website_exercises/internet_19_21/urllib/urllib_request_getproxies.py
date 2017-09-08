# Do practice with getproxies method of urllib.request module.

# return:  a dictionary of scheme to proxy server URL mappings
# example: {'http': 'http://squid.corp.redhat.com:3128', 'https': 'https://squid.corp.redhat.com:3128'}

# It scans the environment for variables named <scheme>_proxy, in a case insensitive approach.
# If both lowercase and uppercase environment variables exist (and disagree), lowercase is preferred.

from urllib.request import getproxies

d = getproxies()
print(d)