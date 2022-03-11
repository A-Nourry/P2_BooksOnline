import requests
from bs4 import BeautifulSoup
import csv
import Scrape_produit


# Récupérations des infos pour chaque lien
def get_info(lien):
    page_url = Scrape_produit.scrape(lien, 'link')
    upc = Scrape_produit.scrape(lien, 'upc')
    titre = Scrape_produit.scrape(lien, 'title')
    price_inclu_tax = Scrape_produit.scrape(lien, 'ttc')[1:]
    price_exclu_tax = Scrape_produit.scrape(lien, 'ht')[1:]
    quantite = Scrape_produit.scrape(lien, 'quantity')
    description = ', '.join(Scrape_produit.scrape(lien, 'desc'))
    category = Scrape_produit.scrape(lien, 'cat')
    review = Scrape_produit.scrape(lien, 'rev')
    img_url = Scrape_produit.scrape(lien, 'img')

    return page_url, upc, titre, price_inclu_tax, price_exclu_tax, quantite, description, category, review, img_url


if __name__ == '__main__':

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

    lien0 = []

    for books in liens:
        info_liens = get_info(books)
        lien0.append(info_liens)

    # CSV
    en_tetes = ['product_page_url', 'universal_ product_code', 'title', 'price_including_tax',
                'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating',
                'image_url']

    with open('Output/infos_categorie.csv', 'w', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(en_tetes)

        for infos in lien0:
            writer.writerow(infos)

        print("le fichier infos_categorie.csv a été généré avec succès !")
