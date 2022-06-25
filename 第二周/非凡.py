import requests
url = 'http://150.158.140.127/index/index.php'
res = requests.get(url)
res.encoding='utf-8'
print(res.text)
with open('tmp/3.0.html','w',encoding='utf-8')as f:
    f.write(res.text)