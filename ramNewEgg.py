from bs4 import BeautifulSoup
import requests


def extraction(page):
    headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"          #my user agent on google
    url = f"https://www.newegg.com/p/pl?d=ddr4+ram+2x32+3600&page={page}"                                                                #using f to take in page number
    current = requests.get(url)
    if current.status_code != 200:
        return 0
    soup = BeautifulSoup(current.content, "html.parser")
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'item-cell')                                                                                    #find item division for a field
    for prod in divs:                                                                                                                    #loop divs
        info = prod.find('div', class_ = 'item-branding')                                                                                #one more find to access item branding that holds title
        for item in info:
            title = prod.find('a', class_ = 'item-title').text.strip()                                                                           #finally extract text from field

        infoPrice = prod.find('div', class_ = 'item-action')
        for price in infoPrice:
            tempPrice = prod.find('li', class_ = 'price-current').text.strip()
        #ram = {'title' : title, 'price' : tempPrice[:7]}
        #listRam.append(ram)
        print(title, tempPrice[:7])
            
listRam = []
flag = True
pageNum = 0

while flag:
    if pageNum == 5:
        flag = False
    pageNum += 1
    a = extraction(pageNum)
    transform(a)
    print(transform(a) + "I am here")
    #print(listRam)
    continue

print("")
