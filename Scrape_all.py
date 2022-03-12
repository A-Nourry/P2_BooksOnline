import requests
from bs4 import BeautifulSoup
import csv
import Scrape_produit
import Scrape_categorie
from collections import defaultdict

# Récupération des liens

liens = []

for i in range(1, 51):
    url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html'
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.content, 'html.parser')
    base = 'http://books.toscrape.com/catalogue/'

    print('lien de la page ' + str(i) + ' récupéré (' + url + ')')

    links = soup.findAll('h3')

    for link in links:
        a = link.find('a')
        lin = a['href']
        liens.append(base + lin)

# Tri des liens par catégories dans un dictionnaire {url1: catégorie1, url2: catégorie1,...}

links_by_categories = {}

for book in liens:
    Slinks = [Scrape_categorie.get_info(book)]

    for bookies in Slinks:
        links_by_categories[bookies] = Scrape_produit.scrape(book, 'cat')

        print('Page ' + book + ' scrapé avec succès !')

# Inversion du dictionnaire {catégorie1: [url1, url2,...], catégorie2: [url1, url2,...]}

links_by_categories_inv = defaultdict(list)

[links_by_categories_inv[v].append(k) for k, v in links_by_categories.items()]
dict_cat = dict(links_by_categories_inv)


'''lien = dict_cat[categories[i]]'''

# Récupération des catégories dans le dictionnaire

categories = []

for books in links_by_categories_inv.keys():
    cat = books
    categories.append(cat) if cat not in categories else categories

    print('catégorie ' + str(books) + ' récupérée')

    if len(categories) >= 50:
        break

# CSV

en_tetes = ['product_page_url', 'universal_ product_code', 'title', 'price_including_tax',
            'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating',
            'image_url']

for info in range(50):
    with open(categories[info] + '.csv', 'w', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(en_tetes)

        for infos in links_by_categories_inv[categories[info]]:
            writer.writerow(infos)

        print("le fichier infos_" + categories[info] + ".csv a été généré avec succès !")
