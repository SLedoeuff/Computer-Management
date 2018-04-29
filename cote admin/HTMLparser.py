import os
import re
from bs4 import BeautifulSoup,Tag
from urllib2 import urlopen


# def GetDocument():
# 	os.system('wget http://www.cert.ssi.gouv.fr/')

html=urlopen("http://www.cert.ssi.gouv.fr/site/cert-fr_alerte.rss").read()
soup=BeautifulSoup(html,"html5lib")
tab=soup.find_all('item')
print tab