import requests, json

BaseUrl = "https://api.vhtear.com"
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

def smuledl(url):
    params = {
      "apikey": Apikey, 
      "link": url
    }
    data = requests.get(BaseUrl+"/getsmule", params=params).json()
    return data
#example smule download
print(smuledl("https://www.smule.com/p/767512225_3062360163"))

def shortener(url):
    params = {
      "apikey": Apikey, 
      "link": url
    }
    data = requests.get(BaseUrl+"/shortener", params=params).json()
    return data
#example shortener
print(shortener("https://www.google.com"))

def googleimg(query):
    params = {
      "apikey": Apikey, 
      "query": query
    }
    data = requests.get(BaseUrl+"/googleimg", params=params).json()
    return data
#example google image
print(googleimg("kopi susu"))

def walpaperhd(query):
    params = {
      "apikey": Apikey, 
      "query": query
    }
    data = requests.get(BaseUrl+"/walpaper", params=params).json()
    return data
#example walpaper
print(walpaperhd("sakura"))

def youtube(query):
    params = {
      "apikey": Apikey, 
      "query": query
    }
    data = requests.get(BaseUrl+"/youtube", params=params).json()
    return data
#example youtube serach
print(youtube("night core"))

def jooxdl(query):
    params = {
      "apikey": Apikey, 
      "query": query
    }
    data = requests.get(BaseUrl+"/musicdl", params=params).json()
    return data
#example joox download
print(jooxdl("sayang"))

def spotifydl(query):
    params = {
      "apikey": Apikey, 
      "query": query
    }
    data = requests.get(BaseUrl+"/spotify", params=params).json()
    return data
#example spotify download
print(spotifydl("sayang"))

def genprim(authkey):
    params = {
      "apikey": Apikey, 
      "auth": authkey
    }
    data = requests.get(BaseUrl+"/genprim", params=params).json()
    return data
#example generate primery token
print(genprim("uac4fdee83ecfb6f0317c97151df9446a:InVUu83UqxmTpuqJwWHS"))

def zodiak(query):
    params = {
      "apikey": Apikey, 
      "query": query
    }
    data = requests.get(BaseUrl+"/zodiak", params=params).json()
    return data
#example zodiak
print(zodiak("scorpio"))

def wikipedia(query):
    params = {
      "apikey": Apikey, 
      "query": query
    }
    data = requests.get(BaseUrl+"/wikipedia", params=params).json()
    return data
#example wikipedia
print(zodiak("jokowi"))

def corona():
    params = {
      "apikey": Apikey
    }
    data = requests.get(BaseUrl+"/corona", params=params).json()
    return data
#example corona
print(corona())

def infogempa():
    params = {
      "apikey": Apikey
    }
    data = requests.get(BaseUrl+"/infogempa", params=params).json()
    return data
#example infogempa
print(infogempa())

def tebakgambar():
    params = {
      "apikey": Apikey
    }
    data = requests.get(BaseUrl+"/tebakgambar", params=params).json()
    return data
#example tebakgambar
print(tebakgambar())

def funkuis():
    params = {
      "apikey": Apikey
    }
    data = requests.get(BaseUrl+"/funkuis", params=params).json()
    return data
#example funkuis
print(funkuis())

def togel():
    params = {
      "apikey": Apikey
    }
    data = requests.get(BaseUrl+"/togel", params=params).json()
    return data
#example togel
print(togel())

def kurs():
    params = {
      "apikey": Apikey
    }
    data = requests.get(BaseUrl+"/kurs", params=params).json()
    return data
#example kurs
print(kurs())

def valentine(text1,text2,link1,link2):
    params = {
      "apikey": Apikey,
      "t1": text1,
      "t2": text2,
      "l1": link1,
      "l2": link2
    }
    data = requests.get(BaseUrl+"/valentine", params=params).json()
    return data
#example valentine
print(valentine("Veza","Hani","https:/obs-sg.line-apps.com/os/p/u3ef45bfb65e4c101f9126ea9b5d3b1e5","https:/obs-sg.line-apps.com/os/p/ue69deccc9ec05714297bc08184f75a15"))

def resepmasakan(query):
    params = {
      "apikey": Apikey, 
      "query": query
    }
    data = requests.get(BaseUrl+"/resepmasakan", params=params).json()
    return data
#example resep masakan
print(resepmasakan("soto lamongan"))

def shopee(query,count):
    params = {
      "apikey": Apikey, 
      "query": query,
      "count": count
    }
    data = requests.get(BaseUrl+"/shopee", params=params).json()
    return data
#example shopee serach product
print(shopee("samsung a51","30"))

def xxxvideo(query):
    params = {
      "apikey": Apikey, 
      "query": query
    }
    data = requests.get(BaseUrl+"/xxxvideo", params=params).json()
    return data
#example xxxvideo
print(xxxvideo("japan"))

def gsmarena(query):
    params = {
      "apikey": Apikey, 
      "query": query
    }
    data = requests.get(BaseUrl+"/gsmarena", params=params).json()
    return data
#example gsmarena
print(gsmarena("samsung a51"))

