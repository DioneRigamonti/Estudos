import pyshorteners

url = "sua URL / Your URL"

link = pyshorteners.Shortener()

short_url = link.tinyurl.short(url)

print(short_url)
