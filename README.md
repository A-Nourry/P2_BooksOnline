# Programme d'extraction des prix
Les scripts suivants ont pour but d'extraire les données
du site web http://books.toscrape.com/ et de les enregistrer dans un fichier au format **.csv** :

- **Scrape_produit.py** : Extrait les informations du livre **Dune** et génère un fichier nommé **infos_produit.csv**.
  

- **Scrape_categorie.py** : Extrait les informations des livres de la catégorie **Fantasy** et génère un fichier nommé **infos_categorie.csv**.


- **Scrape_all.py** : Extrait les informations de tous les livres du site web et génère plusieurs fichiers **.csv** par catégories.

## Comment exécuter les scripts

- __Pré-requis : Python doit être installé sur votre système__


Tout d'abord, téléchargez et décompressez le dossier du code avant de passer aux étapes suivantes.

### 1 . Environnement virtuel

Avant de pouvoir exécuter correctement les scripts, il faut créer un environnement virtuel.

Pour commencer, ouvrez le terminal,
allez dans le dossier que vous avez téléchargé
(ce n'est pas obligatoire, mais préférable pour vous y retrouver) et tapez la commande suivante :

`python -m venv env`


Exemple :
```
C:\BooksOnline>python -m venv env
```


Cette commande permet de créer l'environnement virtuel **env** et également un dossier **env** dans le répertoire dans lequel vous vous trouvez.

Maintenant que l'environnement virtuel est créé, il faut l'activer. Pour cela tapez la commande suivante :

Mac/Linux: `source env/bin/activate`

Si vous êtes sur Windows il faut exécuter le fichier **activate.bat** qui se trouve dans **env/Scripts/** en tapant directement `env\Scripts\activate.bat`

### 2 . Installation des paquets du fichier _requirements.txt_

Pour que les scripts python puissent correctement s'exécuter vous aurez besoin d'installer les paquets se trouvant dans le fichier **requirements.txt**


Une fois que l'environnement virtuel est bien activé, assurez-vous d'être dans le dossier que vous avez téléchargé,
là où se trouve le fichier **requirements.txt** et tapez la commande :

`pip install -r requirements.txt`

Vous pouvez vérifier que les paquets sont bien installé avec la commande :

`pip freeze`

### Maintenant, vous pouvez exécuter les scripts avec succès !

Exemple pour exécuter un script via le terminal : `python3 infos_produit.py`
