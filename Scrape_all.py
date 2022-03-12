import requests
from bs4 import BeautifulSoup
import csv
import Scrape_produit
import Scrape_categorie
from collections import defaultdict


# Récupération des liens

liens = []

for i in range(1, 2):
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
    links_by_categories[book] = Scrape_produit.scrape(book, 'cat')

    print('catégorie du livre ' + book + ' récupérée')

# Inversion du dictionnaire {catégorie1: [url1, url2,...], catégorie2: [url1, url2,...]}

links_by_categories_inv = defaultdict(list)

[links_by_categories_inv[v].append(k) for k, v in links_by_categories.items()]
dict_cat = dict(links_by_categories_inv)

'''lien = dict_cat[categories[i]]'''

# Récupération des catégories dans le dictionnaire

categories = []

for books in links_by_categories.keys():
    cat = Scrape_produit.scrape(books, 'cat')
    categories.append(cat) if cat not in categories else categories

    print('catégorie ' + links_by_categories[str(books)] + ' récupérée')

    if len(categories) >= 50:
        break

print(categories)

# scraping des liens du dictionnaire

all_infos = {}

for i in range(2):
    for keys in links_by_categories_inv[categories[i]]:
        all_infos["cat{0}".format(i)] = dict_cat[categories[i]]

infos_scrape = {}

for i in range(2):
    for links in all_infos['cat' + str(i)]:
        test = [Scrape_categorie.get_info(links)]
        infos_scrape["lien{0}".format(i)] = test

        print('page' + links + ' scrapé avec succès')

# CSV

en_tetes = ['product_page_url', 'universal_ product_code', 'title', 'price_including_tax',
            'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating',
            'image_url']

for info in range(2):
    with open('Output/Categories/' + categories[info] + '.csv', 'w', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(en_tetes)

        for infos in infos_scrape["lien" + str(info)]:
            writer.writerow(infos)

        print("le fichier infos_" + categories[info] + ".csv a été généré avec succès !")
