import requests
from urllib import request
import re


n=811
for i in range(30):
    num = 144940 + i
    url = 'https://www.rouding.com/roudingtuku/shishangzhaopian/%s.html' %num
    # url = 'https://www.rouding.com/roudingtuku/shishangzhaopian/144935.html'
    r = requests.get(url)
    html=r.text
    jpglist=re.findall('//cdn.rouding.com/.+?\.jpg',html)

    print(num)
    for each in jpglist:
        try:
            request.urlretrieve("https:"+each,'img\\%s.jpg' %n)
        except Exception as e:
            print(e)
        finally:
            print('图片%s下载操作完成' %n)
        n+=1