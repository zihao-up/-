import requests
url = 'https://www.baidu.com'
res = requests.get(url)
res.encoding='utf-8'
print(res.text)
with open('tmp/2.1.html','w',encoding='utf-8')as f:
    f.write(res.text)


#===========2
import requests
url = 'https://www.baidu.com'
res = requests.post(url)
res.encoding='utf-8'
print(res.text)
with open('tmp/2.2.html','w',encoding='utf-8')as f:
    f.write(res.text)


#===========3
import requests
url = 'https://baike.baidu.com/item/%E5%8F%98%E5%BD%A2%E9%87%91%E5%88%9A/18396549?fr=aladdin'
res = requests.post(url)
res.encoding='utf-8'
print(res.text)
with open('tmp/2.3.html','w',encoding='utf-8')as f:
    f.write(res.text)



#===========4
import requests
url = 'https://baike.baidu.com/'
header={'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/'
        '537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
res = requests.get(url,header)
print(res.text)
with open('tmp/2.4.html','w',encoding='utf-8')as f:
    f.write(res.text)



# ===========5
import requests
url = 'http://news.china.com.cn/node_8028403.html'
txzzz={'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/'
                     '537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
res = requests.get(url,txzzz)
print(res.text)
with open('tmp/2.5.html','w',encoding='utf-8')as f:
    f.write(res.text)

# ===========6
import requests
txzzz={'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/'
                     '537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
url = 'http://news.china.com.cn/node_8028403.html'
res = requests.get(url,txzzz)
res.encoding='utf-8'
print(res.text)
with open('tmp/2.6.html','w',encoding='utf-8')as f:
    f.write(res.text)