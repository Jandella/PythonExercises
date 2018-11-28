from bs4 import BeautifulSoup
from urllib import request

segniZodiacali = ['Ariete', 'Toro', 'Gemelli', 'Cancro', 'Leone', 'Vergine', 'Bilancia', 
'Scorpione', 'Sagittario', 'Capricorno', 'Acquario', 'Pesci']

def paoloFox():
    "Prende l'oroscopo di paolo fox"
    print("Da implementare")

def almanaccoBarbaNera(segno:str, domani:bool):
    "Prende l'oroscopo di Barbanera in base al segno"
    url = 'http://www.barbanera.it/segno.php?segno=%s&periodo=' %segno
    if domani == True:
        url += 'domani'
    html_doc = request.urlopen(url)
    soup = BeautifulSoup(html_doc.read(), features="html.parser")
    divOroscopo = soup.find_all('div', class_="oroscopo")
    testo = divOroscopo[0].get_text()
    print(segno.upper())
    print(testo)

if __name__ == '__main__':
    print("=== OROSCOPO DI BARBANERA ===")
    print("Oggi")
    for segno in segniZodiacali:
        try:
            print(almanaccoBarbaNera(segno, False))
        except Exception as ex:
            print(ex)
    print("Domani")
    for segno in segniZodiacali:
        try:
            print(almanaccoBarbaNera(segno, True))
        except Exception as ex:
            print(ex)
