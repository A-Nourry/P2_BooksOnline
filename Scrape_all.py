import requests
from bs4 import BeautifulSoup
import csv
import Scrape_produit
from collections import defaultdict


def get_key(val, my_dict):
    result = []
    for key, value in my_dict.items():
        if value == val:
            result.append(key)
            continue
        return result


# Récupération des liens
liens = []

for i in range(1, 2):
    url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html'
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.content, 'html.parser')
    base = 'http://books.toscrape.com/catalogue/'

    links = soup.findAll('h3')

    for link in links:
        a = link.find('a')
        lin = a['href']
        liens.append(base + lin)

# Récupération des catégories
categories = []

for books in liens:
    cat = Scrape_produit.scrape(books, 'cat')
    categories.append(cat) if cat not in categories else categories

# Tri des liens par catégories
links_by_categories = {}

for book in liens:
    links_by_categories[book] = Scrape_produit.scrape(book, 'cat')

links_by_categories_inv = defaultdict(list)
[links_by_categories_inv[v].append(k) for k, v in links_by_categories.items()]
dict_cat = dict(links_by_categories_inv)

lien0 = ', ' .join(dict_cat[categories[0]])


'''# Récupérations des infos pour chaque lien
page_url = []
upc = []
titre = []
price_inclu_tax = []
price_exclu_tax = []
quantite = []
description = []
category = []
review = []
img_url = []

for books in liens:
    s_url = Scrape_produit.scrape(books, 'link')
    page_url.append(s_url)

    s_upc = Scrape_produit.scrape(books, 'upc')
    upc.append(s_upc)

    s_titre = Scrape_produit.scrape(books, 'title')
    titre.append(s_titre)

    pit = Scrape_produit.scrape(books, 'ttc')
    price_inclu_tax.append(pit[1:])

    pet = Scrape_produit.scrape(books, 'ht')
    price_exclu_tax.append(pet[1:])

    qts = Scrape_produit.scrape(books, 'quantity')
    quantite.append(qts)

    s_des = Scrape_produit.scrape(books, 'desc')
    description.append(s_des)

    revs = Scrape_produit.scrape(books, 'rev')
    review.append(revs)

    imgs = Scrape_produit.scrape(books, 'img')
    img_url.append(imgs)

    cate = Scrape_produit.scrape(books, 'cat')

    category.append(cate)

Scrape_produit.mkcsv('infos_cat.csv', page_url, upc, titre, price_inclu_tax, price_exclu_tax, quantite, description,
                     category,
                     review, img_url)'''
