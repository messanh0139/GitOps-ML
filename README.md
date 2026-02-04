# Projet d'apprentissage automatique avec DVC (contrôle de version des données)
Ce projet utilise l'ensemble de données bancaires (card_transdata.csv) pour illustrer un pipeline ML de base avec DVC pour le versionnage des données et des modèles.


## Requirements
1. DVC : Pour suivre les étapes de données, de modélisation et de pipeline
2. Git : pour le contrôle de version
3. Scikit-learn : pour entraîner un modèle
4. Pandas et Joblib

## Configurer l'environnement

### Créer et activer un environnement virtuel
```sh
python3 -m venv venv
source venv/bin/activate
```

### Installer les dépendances
```sh
pip install -r requirements.txt
```

### Initialiser Git et DVC
```sh
git init
```
```sh
dvc init
```

### Télécharger et ajouter l'ensemble de données au répertoire de données

```sh
mkdir data
```

```sh
wget -O data/card_transdata.csv https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/card_transdata.csv
```

### Ajouter l'ensemble de données transdata avec suivi DVC
```sh
dvc add data/card_transdata.csv
```

### Suivez les modifications avec Git
```sh
git add data/card_transdata.csv.dvc 
```

```sh
git commit -m "Add card_transdata dataset with DVC tracking"
```


## Créer un pipeline DVC

### Étape de préparation des données
```sh
dvc stage add -n data_processing \
  -d src/data_processing.py -d data/card_transdata.csv \
  -o data/X_train.csv -o data/X_test.csv -o data/y_train.csv -o data/y_test.csv \
  python src/data_processing.py
```

### Étape de formation du modèle
```sh
dvc stage add -n train \
  -d src/train.py -d data/X_train.csv -d data/y_train.csv \
  -o model/model.joblib \
  python src/train.py
```

### Évaluer le modèle entraîné
```sh
dvc stage add -n evaluate \
  -d src/evaluate.py -d model/model.joblib -d data/X_test.csv -d data/y_test.csv \
  -M metrics.json \
  python src/evaluate.py
```

### Valider les modifications
```sh
git add dvc.yaml 
```
```sh
git commit -m "Add DVC pipeline stages for data_processing, train, evaluate"
```


### Exécuter l'ensemble du pipeline
```sh
dvc repro
```

Si le pipeline réussit, exécutez la commande :
```sh
git add dvc.lock
```

### Visualiser les indicateurs
```sh
dvc metrics show
```

Optionnel:
```sh
dvc metrics diff --targets metrics.json
```


## Utilisez Makefile pour automatiser l'ensemble du pipeline DVC.

### Installer make
```sh
sudo apt install make -y
```

```sh
cd <directory with Makefile>
```

### Exécutez n'importe quelle tâche du pipeline DVC
```sh
make install     # installs dependencies
make run         # runs the DVC pipeline
make metrics     # shows metrics from metrics.json
```



## Déployez le modèle entraîné avec Gradio + Joblib
```sh
pip install gradio
```
Déjà installé dans les requirements.txt

```sh
python app/gradio_app.py
```

Dans votre navigateur, accédez à l'URL suivante :
```sh
http://localhost:7860
```

## Maintenant, simulons une modification des données

### Sauvegardez et modifiez l'ensemble de données d'origine
```sh
cp data/card_transdata.csv data/card_transdata.csv.bak
```

Ajouter une fausse ligne (synthétique)
```sh
echo "4.4,5.6,2.9,1.8,1.3,1.0,1.5,5.1" >> data/card_transdata.csv
echo "4.0,5.0,2.0,1.0,0.0,0.0,0.0,4.3" >> data/card_transdata.csv
```
Consultez le fichier card_transdata.csv pour voir les modifications.

### Suivez l'évolution des données avec DVC
```sh
dvc add data/card_transdata.csv
```

### Commit changes (Valider les modifications)
```sh
git add data/card_transdata.csv.dvc
git commit -m "Modified bank transactions dataset with fraude or not"
```

### Relancer le pipeline
```sh
dvc repro
```

### Suivre les modifications avec Git
```sh
git add model/model.joblib dvc.lock metrics.json
git commit -m "Retrained model with updated data"
```

### Exécutez des expériences sans les valider.
```sh
dvc exp run
```

### Liste des expériences
```sh
dvc exp show
```
q to Exit


### Garde la meilleure et engage-la.
```sh
dvc exp apply <exp_id>
```
```sh
git add .
git commit -m "Applied best model experiment"
```

## Simuler le retour en arrière
### Expérimentez de nouvelles expériences et appliquez les meilleures pratiques.
```sh
dvc exp run
```
```sh
dvc exp show
```
```sh
dvc exp apply <exp_id>
git add .
git commit -m "Applied better model from experiment"
```

### Récupérer les journaux Git et extraire l'ancien commit
```sh
git log --oneline
```

### Copiez le hachage du commit vers lequel vous souhaitez revenir :
```sh
git checkout <old_commit_hash>
```

### Rétablir l'état de tous les fichiers suivis par DVC (données/modèle/métriques)
```sh
dvc checkout
```