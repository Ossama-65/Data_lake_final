Data_Lake_Final
Ce projet est conçu pour gérer et exploiter un lac de données avec une API associée, des scripts d'administration, et une base de données SQLite. Le projet est structuré de manière à fournir une base solide pour les applications de gestion de données.

Structure du projet
bash
Copier le code
Data_Lake_Final/
│
├── data/                 # Contient les données brutes ou transformées
├── data_lake_api/        # Code source de l'API pour accéder au lac de données
├── admin.py              # Script d'administration
├── db.sqlite3            # Base de données SQLite
└── manage.py             # Script principal pour gérer les opérations
Fonctionnalités
Lac de données : Stocke des données structurées et non structurées.
API : Fournit un accès programmatique au lac de données.
Base de données SQLite : Gestion des métadonnées ou données associées.
Scripts d'administration : Simplifie les tâches administratives liées au lac de données.
Prérequis
Python 3.x
pip pour gérer les dépendances
SQLite pour la base de données
Installation
Clonez ce dépôt :

bash
Copier le code
git clone https://github.com/Ossama-65/Data_Lake_Final.git
cd Data_Lake_Final
Installez les dépendances :

bash
Copier le code
pip install -r requirements.txt
Lancez le serveur ou les scripts :

bash
Copier le code
python manage.py runserver
Utilisation
API :

Pour démarrer l'API, exécutez manage.py.
Accédez à l'API via http://localhost:8000/.
Administration :

Le fichier admin.py contient des fonctions pour la gestion des données.
Contribution
Les contributions sont les bienvenues ! Si vous souhaitez participer :

Fork le dépôt.
Créez une branche : git checkout -b feature-nom-de-votre-feature.
Faites vos modifications et committez : git commit -m "Ajout de nouvelle fonctionnalité".
Poussez vos modifications : git push origin feature-nom-de-votre-feature.
Créez une pull request.
Auteur
Manel Zerguit & Ossama Louridi
Licence
Ce projet est sous licence MIT.
