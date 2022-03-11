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
        soupdes = []
        for d in des:
            soupdes.append(d.string)
        return soupdes

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
        i_lien = img['src']
        i_url = 'http://books.toscrape.com/' + i_lien[6:]
        return i_url

    else:
        print('Argument invalide')


def mkcsv(file_name, en1, en2, en3, en4, en5, en6, en7, en8, en9, en10):
    en_tetes = ['product_page_url', 'universal_ product_code', 'title', 'price_including_tax',
                'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating',
                'image_url']

    with open('Output/' + file_name, 'w', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(en_tetes)

        for infos in zip(en1, en2, en3, en4, en5, en6, en7, en8, en9, en10):
            writer.writerow(infos)

    print("le fichier " + file_name + " a été créé avec succès !")


if __name__ == '__main__':
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
    img_url = [scrape(lien, 'img')]

    mkcsv('infos_produit.csv', page_url, upc, titre, price_inclu_tax, price_exclu_tax, quantite, description, category,
          review, img_url)
