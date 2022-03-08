import requests
from bs4 import BeautifulSoup
import csv

# lien de la page
url = 'http://books.toscrape.com/catalogue/dune-dune-1_151/index.html'
reponse = requests.get(url)
soup = BeautifulSoup(reponse.text, 'html.parser')

# liste des informations
en_tete = ['product_page_url', 'universal_ product_code', 'title', 'price_including_tax',
           'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']

# récupération des informations
tds = soup.findAll('td')
page_url = [url]

# universal product code
upc = tds[0]

# récupération du titre
titre = soup.find('h1')

# récupération du prix TTC
price_inclu_tax = tds[3]

# récupération du prix Hors Tax
price_exclu_tax = tds[2]

# information sur la quantité restante
quantite = tds[5]

# récupération de la description du produit
des = soup.findAll('p', class_='')
description = []
for d in des:
    description.append(d.string)

# récupération de la categorie
a = soup.findAll('a')
ahref = []
for title in a:
    ahref.append(title.string)
category = [ahref[3]]


# review rating
review = tds[6]

# url de l'image
img = soup.find('img')
img_url = ['http://books.toscrape.com/' + img['src']]

# CSV
with open('infos_produit.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(en_tete)

    for infos in zip(page_url, upc, titre, price_inclu_tax, price_exclu_tax, quantite, description, category,
                     review, img_url):
        writer.writerow(infos)
