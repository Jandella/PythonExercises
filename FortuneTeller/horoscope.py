from bs4 import BeautifulSoup
from urllib import request
from datetime import datetime

segniZodiacali = ['ariete', 'toro', 'cemelli', 'cancro', 'leone', 'vergine', 'bilancia', 
'scorpione', 'sagittario', 'capricorno', 'acquario', 'pesci']
mesi = ['placeholder','gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto',
'settembre', 'ottobre', 'novembre', 'dicembre']

def paoloFox(segno:str):
    "Prende l'oroscopo di paolo fox"
    dataDaChiedere = datetime.today()
    indexOfSegno = segniZodiacali.index(segno.lower())
    indexOfSegno = indexOfSegno + 1 #base 1
    url = 'https://zon.it/oroscopo-paolo-fox-%s-%s-%s/%s' %(dataDaChiedere.day, mesi[dataDaChiedere.month], dataDaChiedere.year, indexOfSegno)
    html_doc = request.urlopen(url)
    soup = BeautifulSoup(html_doc.read(), features="html.parser")
    #the page is a bit messy---
    #first: get the first article tag with post class
    articoliPost = soup.find_all('article', class_="post")
    #grab the main content
    articolo = articoliPost[0].find_all('div', class_="td-post-content")[0]
    #take all the items
    items = articolo.find_all('div', class_="td-item")
    #the horoscope itself is into a span element, using class to be sure it's the rigth span
    spanDellOroscopo = items[0].find_all('span', class_="td-sml-description")[0]
    #there are a bunch of paragraph inside the span, grab all of them
    paragrafi = spanDellOroscopo.find_all('p')
    testo = ''
    i = 0
    #take the first paragraph that's not null or empty
    while (testo == '' or testo == None) and i < len(paragrafi):
        testo = paragrafi[i].get_text()
        i = i + 1
    return testo
    

def almanaccoBarbaNera(segno:str, domani:bool):
    "Prende l'oroscopo di Barbanera in base al segno"
    url = 'http://www.barbanera.it/segno.php?segno=%s&periodo=' %segno
    if domani == True:
        url += 'domani'
    html_doc = request.urlopen(url)
    soup = BeautifulSoup(html_doc.read(), features="html.parser")
    divOroscopo = soup.find_all('div', class_="oroscopo")
    testo = divOroscopo[0].get_text()
    return testo

def printBarbanera():
    print("=== OROSCOPO DI BARBANERA ===")
    print("Oggi")
    for segno in segniZodiacali:
        try:
            print(segno.upper())
            print(almanaccoBarbaNera(segno, False))
        except Exception as ex:
            print(ex)
    print("Domani")
    for segno in segniZodiacali:
        try:
            print(segno.upper())
            print(almanaccoBarbaNera(segno, True))
        except Exception as ex:
            print(ex)

def printPaoloFox():
    print("=== OROSCOPO DI PAOLO FOX ===")
    print("Oggi")
    for segno in segniZodiacali:
        try:
            print(segno.upper())
            print(paoloFox(segno))
        except Exception as ex:
            print(ex)

if __name__ == '__main__':
    #printBarbanera()
    #printPaoloFox()
    segno = input("Segno zodiacale? ")
    while not(segno in segniZodiacali):
        print("Non è un segno zodiacale")
        segno = input("Segno zodiacale? ")
    tipo = input("Preferisci Paolo Fox (P) o Barbanera (B)? ")
    if tipo.startswith('b') or tipo.startswith('B'):
        print("=== BARBANERA DICE: ===")
        print(segno.upper())
        print("Per oggi:")
        print(almanaccoBarbaNera(segno, False))
        print()
        print("Per domani:")
        print(almanaccoBarbaNera(segno, True))
    else:
        print("=== PAOLO FOX OGGI DICE: ===")
        print(segno.upper())
        print(paoloFox(segno))

