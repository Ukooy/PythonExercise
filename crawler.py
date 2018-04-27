import urllib.parse
import urllib.request

def getHtml(url,values):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
    headers = {'User-Agent':user_agent}
    data = urllib.parse.urlencode(values)
    response_result = urllib.request.urlopen(url+'?'+data).read()
    html = response_result.decode('utf-8')
    return html

#获取数据
def requestLocalAPI():
    print('请求数据')
    url = 'http://localhost:8888/api/test/cut'
    value ={
        'content'    :'北京市北京风景67号院'
    }
    result = getHtml(url,value)
    return result

