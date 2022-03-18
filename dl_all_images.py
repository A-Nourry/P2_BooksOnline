import os
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from tqdm import tqdm
import Scrape_produit


# Récupération des liens

liens = []

for i in range(1, 51):
    url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html'
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.content, 'html.parser')
    base = 'http://books.toscrape.com/catalogue/'

    print('liens de la page ' + str(i) + ' récupérés (' + url + ')')

    links = soup.findAll('h3')

    for link in links:
        a = link.find('a')
        lin = a['href']
        liens.append(base + lin)

# Tri des liens par catégories dans un dictionnaire {url1: catégorie1, url2: catégorie1,...}

links_by_categories = {}

for book in liens:
    Slinks = [Scrape_produit.scrape(book, 'img')]

    for books in Slinks:
        links_by_categories[books] = Scrape_produit.scrape(book, 'cat')

        print("L'URL et la catégorie du produit " + book + " ont bien été récupérés")


# Inversion des dictionnaires {catégorie1: [url1, url2,...], catégorie2: [url1, url2,...]}
links_by_categories_inv = defaultdict(list)

[links_by_categories_inv[v].append(k) for k, v in links_by_categories.items()]
dict_cat = dict(links_by_categories_inv)


# Récupération des catégories dans le dictionnaire

categories = []

for books in links_by_categories_inv.keys():
    cat = books
    categories.append(cat) if cat not in categories else categories

    print('catégorie ' + str(books) + ' récupérée')

    if len(categories) >= 50:
        break

print(categories)


def download(urls, pathname):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(urls, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # get the file name
    filename = os.path.join(pathname, urls.split("/")[-1])
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True,
                    unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))


for cats in categories:
    for images in links_by_categories_inv[cats]:
        download(images, 'produits_par_catégories/' + cats + '/images/')
