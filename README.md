# GitOps-ML: Détection de Fraude Cartes Bancaires

Un projet MLOps complet pour la détection de fraude sur les transactions par carte bancaire, conçu pour être reproductible, maintenable et prêt pour la production.

## 📋 Vue d'ensemble

Pipeline de machine learning complet avec:
- **Data Processing**: Nettoyage et validation
- **Feature Engineering**: Création intelligente de features
- **Model Training**: Entraînement avec LightGBM ou Random Forest
- **Evaluation**: Calcul de métriques de performance détaillées
- **DVC**: Gestion des pipelines de données et des artefacts
- **MLflow**: Suivi des expérimentations (optionnel)

## 🚀 Démarrage Rapide

### 1. Installation

```bash
# Cloner le projet
git clone <URL-DU-REPO>
cd GitOps-ML

# Créer un environnement virtuel et l'activer
python -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

## 📁 Structure

```
src/
├── config.py               # Configuration
├── data_processing.py      # Nettoyage
├── features.py             # Features
├── model.py                # Modèle
├── train.py                # Entraînement
└── evaluate.py             # Évaluation
```

## 🚀 Usage

```bash
# Entraîner
python src/train.py

# Évaluer
python src/evaluate.py --model-path models/model.pkl

# Pipeline DVC
dvc repro
```

## 📊 Métriques

- AUC-ROC
- Average Precision
- F1-Score
- Precision & Recall

---

**Décembre 2025**