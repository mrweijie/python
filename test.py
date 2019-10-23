from urllib import request
import re

url = 'https://www.csdn.net/'
url_request = request.Request(url)
url_response = request.urlopen(url_request)
data=url_response .read().decode('utf-8')
jpglist=re.findall('https://csdnimg.cn.+?.jpg',data)

n=1
for each in jpglist:
	print(each)
	try:
		request.urlretrieve(each,'pic2\\%s.jpg' %n)
	except Exception as e:
		print(e)
	finally:
		print('图片%s下载操作完成' %n)
	n+=1