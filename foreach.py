url = 'http://www.gz.gov.cn/gzgov/s2342/common_list'
urlReal='';
for index in range(10):
	if index == 0:
		urlReal = url+'.shtml'
	else :
		urlReal= url+'_'+str(index)+'.shtml'
	print (urlReal)