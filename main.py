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
