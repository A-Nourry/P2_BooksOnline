import requests
from bs4 import BeautifulSoup
import csv


def scrape(url, en_tete):
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, 'html.parser')

    tds = soup.findAll('td')
    if en_tete == 'link':
        result = url
        return result

    elif en_tete == 'upc':
        result = tds[0]
        return result.text

    elif en_tete == 'title':
        result = soup.find('h1')
        return result.text

    elif en_tete == 'ttc':
        result = tds[3]
        return result.text

    elif en_tete == 'ht':
        result = tds[2]
        return result.text

    elif en_tete == 'quantity':
        result = tds[5]
        return result.text

    elif en_tete == 'desc':
        des = soup.findAll('p', class_='')
        desc = []
        for d in des:
            desc.append(d.string)
        return desc

    elif en_tete == 'cat':
        a = soup.findAll('a')
        ahref = []
        for title in a:
            ahref.append(title.string)
        categorie = ahref[3]
        return categorie

    elif en_tete == 'rev':
        result = tds[6]
        return result.text

    elif en_tete == 'img':
        img = soup.find('img')
        lien = img['src']
        img_url = ['http://books.toscrape.com/' + lien[6:]]
        return img_url

    else:
        print('Argument invalide')


lien = 'http://books.toscrape.com/catalogue/dune-dune-1_151/index.html'

page_url = [scrape(lien, 'link')]
upc = [scrape(lien, 'upc')]
titre = [scrape(lien, 'title')]
price_inclu_tax = [scrape(lien, 'ttc')]
price_exclu_tax = [scrape(lien, 'ht')]
quantite = [scrape(lien, 'quantity')]
description = scrape(lien, 'desc')
category = [scrape(lien, 'cat')]
review = [scrape(lien, 'rev')]
img_url = scrape(lien, 'img')

# liste des informations
en_tetes = ['product_page_url', 'universal_ product_code', 'title', 'price_including_tax',
           'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']

# CSV
with open('infos_produit.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(en_tete)

    for infos in zip(page_url, upc, titre, price_inclu_tax, price_exclu_tax, quantite, description, category,
                     review, img_url):
        writer.writerow(infos)

if __name__ == '__main__':
    print("fichier infos_produit.csv créé avec succès !")
