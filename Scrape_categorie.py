import requests
from bs4 import BeautifulSoup
import csv
import Scrape_produit

# Récupération des liens
liens = []

for i in range(1, 4):
    url = 'http://books.toscrape.com/catalogue/category/books/fantasy_19/page-' + str(i) + '.html'
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.content, 'html.parser')
    base = 'http://books.toscrape.com/catalogue/'

    links = soup.findAll('h3')

    for link in links:
        a = link.find('a')
        lin = a['href']
        liens.append(base + lin[9:])

# Récupérations des infos pour chaque lien
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

    cate = Scrape_produit.scrape(books, 'cat')
    category.append(cate)

    revs = Scrape_produit.scrape(books, 'rev')
    review.append(revs)

    imgs = Scrape_produit.scrape(books, 'img')
    img_url.append(imgs)


# CSV
en_tetes = ['product_page_url', 'universal_ product_code', 'title', 'price_including_tax',
            'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating',
            'image_url']

with open('infos_categorie.csv', 'w', encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(en_tetes)

    for infos in zip(page_url, upc, titre, price_inclu_tax, price_exclu_tax, quantite, description, category,
                     review, img_url):
        writer.writerow(infos)

    print("le fichier infos_categorie.csv à été créé avec succès !")
