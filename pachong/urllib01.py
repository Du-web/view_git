from urllib import request, parse

# resp = request.urlopen('https://www.sogou.com/')
# print(resp.read())
# request.urlretrieve('https://www.sogou.com/', 'sougou.html')
# request.urlretrieve('https://bkimg.cdn.bcebos.com/pic/c83d70cf3bc79f3d95569ce8bda1cd11738b29b6?x-bce-process=image/resize,m_lfit,w_268,limit_1/format,f_jpg', 'zhanggenshuo.jpg')
# data = {'name': '杜杜', 'age': 18, 'greet': 'hello world'}
# qs = parse.urlencode(data)
# print(qs)

# url = 'https://edu.csdn.net/course/play/24756/280658;user?id=s#comment'
# result = parse.urlparse(url)
# print(result)
# result1 = parse.urlsplit(url)
# print(result1)
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
# }
# rq = request.Request('https://www.baidu.com/',headers=header)
# print(rq)
# resp = request.urlopen(rq)
# print(resp.read())
# url = 'http://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid=17394943ea27a-026a8cedb6c377-4353761-144000-17394943ea3c8&riskLevel=71&optimusCode=10'
# header = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
# }
# rq = request.Request(url, headers=header)
# resp = request.urlopen(rq)
# resp = request.urlopen(url)
# print(resp.read().decode())

# url = 'https://www.biedoul.com/'
# rest = request.urlopen(url)
# print(rest.read())

res = request.urlopen()




