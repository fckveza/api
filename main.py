import requests, json

BaseUrl = "https://api.fckveza.com"
Apikey = "Chat me https://line.me/ti/p/~veza1007"

def ytdl(url):
    params = {
      "apikey": Apikey, 
      "link": url
    }
    data = requests.get(BaseUrl+"/ytdl", params=params).json()
    return data
#example youtube download
print(ytdl("https://youtu.be/IYNRADB6GP0"))

def tiktokdl(url):
    params = {
      "apikey": Apikey, 
      "link": url
    }
    data = requests.get(BaseUrl+"/tiktokdl", params=params).json()
    return data
#example tiktok download
print(tiktokdl("https://vt.tiktok.com/yqyjPX/"))

def timelinedl(url):
    params = {
      "apikey": Apikey, 
      "link": url
    }
    data = requests.get(BaseUrl+"/timeline", params=params).json()
    return data
#example timeline download
print(tiktokdl("https:/timeline.line.me/post/_dcAJhbTlVNqvq27gmoe1M6crJ5Xl1a9fUKXRyvw/1157692114207018096"))
