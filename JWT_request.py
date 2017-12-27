# coding:utf8
import urllib
import urllib2
import jwt
import json

# 2 获取密钥
response = urllib2.urlopen("http://39.106.51.249/my_secret")
html = response.read()
# 3 生成jwt
msg = jwt.encode({'name': u'陈春虎'}, html, algorithm='HS256')
# 4 获取测试数据
url = "http://39.106.51.249/my_data"
wd = {"token": msg}
wd = urllib.urlencode(wd)
fullurl = url + "?" + wd
request = urllib2.Request(fullurl)
response = urllib2.urlopen(request).read()
# 5 算出达成率，并将结果按从大到小排序，输出为csv文件
data = json.loads(response)
rate_dict = {}
for i in data['data']:
    rate = float(i[u"销量"]) / float(i[u"指标"])
    rate_dict[i[u"姓名"]] = '%.2f' % rate
rate_list = sorted(rate_dict.items(), key=lambda item: item[1], reverse=True)
with open('data.csv', 'wb') as f:
    for item in rate_list:
        line = ','.join(item) + '\n'
        f.write(line.encode('gbk'))
