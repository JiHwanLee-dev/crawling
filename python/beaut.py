from bs4 import BeautifulSoup
import requests


webpage = requests.get('https://www.megabox.co.kr/booking')
soup = BeautifulSoup(webpage.content, 'html.parser')
#brchList > ul > li:nth-child(1)
#print(soup)

test = soup.select_one("#brchList > ul")
test22 = soup.find_all('div')
test33 = soup.find('div', {'class':'all-list'})
print(test22)

