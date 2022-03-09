# Programme d'extraction des prix
Les scripts suivants ont pour but d'extraire les données
du site http://books.toscrape.com/ et de les enregistrer dans un fichier au format .csv:

- **Scrape_produit.py** : Extrait les informations du livre "Dune" et les enregistre dans un fichier nommé **infos_produit.csv**
- **Scrape_categorie.py** : Extrait les informations de toute une catégorie et les enregistre dans un fichier nommé **infos_categorie.csv**
- _d'autres scripts à venir..._

## Comment exécuter les scripts

- __Pré-requis : Python doit être installé sur votre système__


Tout d'abord, téléchargez et décompressez le dossier complet avant de passer aux étapes suivantes.

### Environnement virtuel

Avant de pouvoir exécuter correctement les scripts, il va falloir créer un environnement virtuel.

Pour commencer, ouvrez le terminal,
allez dans le dossier que vous avez téléchargé
(ce n'est pas obligatoire, mais préférable pour vous y retrouver) et tapez la commande suivante :

`python -m venv env`


Exemple :
```
C:\BooksOnline>python -m venv env
```


Cette commande permet de créer l'environnement virtuel **env** et également un dossier **env** dans le répertoire dans lequel vous vous trouvez.

Maintenant que l'environnement virtuel est créé, il faut l'activer. Pour cela taper la commande suivante :

Mac/Linux: `source env/bin/activate`

Si vous êtes sur Windows il faut exécuter le fichier **activate.bat** qui se trouve dans **env/Scripts/** en tapant directement `env\Scripts\activate.bat`

### Installation des paquets du fichier _requirements.txt_

Pour que les scripts python puissent correctement s'exécuter vous aurez besoin d'installer les paquets se trouvant dans le fichier **requirements.txt**


Une fois que l'environnement virtuel est bien activé, assurez-vous d'être dans le dossier que vous avez téléchargé,
là où se trouve le fichier **requirements.txt** et tapez la commande :

`pip install -r requirements.txt`

Vous pouvez vérifier que les paquets sont bien installé avec la commande :

`pip freeze`

### Maintenant, vous pouvez exécuter les scripts avec succès !

Exemple pour exécuter un script via le terminal : `python3 Page_produit.py`










