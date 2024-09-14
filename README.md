
# Analyse exploratoire des arbres de Paris

Ce projet fait partie d'un concours Smart City dans le cadre du programme **"Végétalisons la ville"**. 
L'objectif est de réaliser une analyse exploratoire des données des arbres de Paris pour mieux comprendre 
leur répartition et leur état.

## Objectifs du projet
- Analyser les données des arbres à Paris pour identifier des caractéristiques clés.
- Visualiser la distribution des circonférences et des hauteurs des arbres.
- Nettoyer et prétraiter les données pour des analyses plus poussées.

## Environnement de développement
Les outils suivants ont été utilisés pour le projet :
- **Google Colaboratory** pour l'analyse des données en ligne.
- **Anaconda** et **Jupyter** pour le développement local.
- **PyCharm** pour le développement avancé.

## Jeu de données
Les données utilisées pour cette analyse proviennent du site OpenData de la Ville de Paris.

### Aperçu des données
Le jeu de données comprend environ **200 000 arbres**, avec les colonnes principales suivantes :
- `circonference_cm` : Circonférence de l'arbre en cm
- `hauteur_m` : Hauteur de l'arbre en mètres
- `stade_developpement` : Stade de développement de l'arbre (J = Jeune, A = Adulte, etc.)

## Résultats
### Distribution des circonférences des arbres
![Distribution de la circonférence des arbres](distribution_circonference.png)

### Distribution des hauteurs des arbres
![Distribution de la hauteur des arbres](distribution_hauteur.png)

### Analyse des variables quantitatives hauteur et circonférence par régression linéaire
![Analyse de la hauteur et la circonférence par régression linéaire](Analyse_régression_linéaire.png)

## Comment exécuter le projet
1. Clonez le dépôt GitHub :
   ```bash
   git clone https://github.com/votre-compte/votre-projet.git
   ```
2. Installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```
3. Exécutez le notebook `P2_01_notebook.ipynb` pour voir l'analyse complète.

## Licence
Ce projet est distribué sous la licence MIT.
