from bs4 import BeautifulSoup
import requests
import csv

my_url = "https://www.billboard.com/charts/hot-100"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
   }
r = requests.get(my_url)
page_soup = BeautifulSoup(r.content, 'html.parser')


Chart = page_soup.find_all('li', {'class': 'chart-list__element display--flex'})

file = open('Test.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Ranking', 'Song', 'Artist'])

for item in Chart:
   Rank = item.find('span', class_='chart-element__rank__number').text.strip()
   Song = item.find('span', class_='chart-element__information__song text--truncate color--primary').text.strip()
   Artist = item.find('span', class_='chart-element__information__artist text--truncate color--secondary').text.strip()


   print(Rank, '. ', Song, '- ', Artist)
   writer.writerow([Rank.encode(), Song.encode(), Artist.encode()])

file.close()