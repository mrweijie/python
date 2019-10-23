#!/usr/bin/python
# import sys
from time import ctime
import base64
import _md5
# print (sys.path)
# print('[%s] %s' % (ctime(), "1"))
str = "123'12'456";

print(base64.b64encode(bytes(str, 'utf-8')).decode())
print(str)