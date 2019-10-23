from urllib import request
import re

url = 'http://www.gz.gov.cn/gzgov/s2342/common_list';
urlReal='';
urlList=[];
for index in range(1):
	if index == 0:
		urlReal = url+'.shtml';
	else :
		urlReal= url+'_'+str(index)+'.shtml';
	url_request = request.Request(urlReal);
	url_response = request.urlopen(url_request);
	data=url_response .read().decode('utf-8');
	urlList.extend(list(filter(lambda x: x != 'href="../../gzgov/s2342/common_list.shtml', re.findall('href="../../gzgov/s2342/.+?.shtml',data)))) ;
titles=[];
contents=[];
a=2;
for each in urlList:
	url_request = request.Request(each.replace('href="../..','http://www.gz.gov.cn'));
	url_response = request.urlopen(url_request);
	data=url_response .read().decode('utf-8').replace("\t","").replace("\r\n","").replace(" ","");
	if a < 3:
		#print(data);
		a+=1;
	titles.extend(re.findall('<h1class="content_title">.*?</h1>',data));
	contents.extend(re.findall('<divclass="content_article"id="zoomcon">.*?</div>',data));
	
for each in titles:
	print(each.replace('<h1class="content_title">','').replace('</h1>',''));

for each in contents:
	print(each);