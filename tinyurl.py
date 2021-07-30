import pyshorteners 
print("hello! this is my project for URL SHORTENER ")
print("enter your long url and rest")
url=input()
s = pyshorteners.Shortener()
print('The short url is ', s.tinyurl.short(url))
