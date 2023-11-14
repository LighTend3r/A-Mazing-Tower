# <img src="doc/A-Mazing-Tower-Logo.jpg" alt="drawing" width="40"/> A-Mazing-Tower

## Description:
Bienvenue dans "A Mazing Tower" ! Un jeu de labyrinthe passionnant où vous devez explorer quatre salles labyrinthiques et collecter des pièces pour atteindre la victoire.

## 🎯 Contexte & Cahier des Charges

Développé dans le cadre d'une formation pour permettre une monté en compétence en Python, ce jeu vise à apprendre les bonnes pratique de programmation de manière ludique.

### Backlog:
|id|description|priorité|
|:-:|---|:-:|
|1|En tant qu'utilisateur, je peux voir la carte|1|
|2|En tant qu'utilisateur, je peux voir mes points|1|
|3|En tant qu'utilisateur, je peux me déplacer dans la salle où je suis|2|
|4|En tant qu'utilisateur, je peux ramasser des pièces|2|
|5|En tant qu'utilisateur, je peux me déplacer entre les salles avec un "téléporteur"|3|
|6|En tant qu'utilisateur, je peux ramasser des bonus/malus|4|

## 🎲 Règles du Jeu

- **Maquette :**

<img src="doc/Maquette.png" alt="drawing" width="500"/>

- **Déroulé d'une partie :**
    - Les joueurs apparaissent dans un des 4 labyrinthes.
    - Des pièces apparaissent (nombre défini par l'admin) à une position aléatoire dans les 4 labyrinthes.
    - Les joueurs peuvent se déplacer dans les labyrinthes.
    - Dès qu'il n'y a plus de pièce, les labyrinthes sont réinitialisés.

- **Conditions de Victoire :** Etre le joueur ayant ramassé le plus de pièce.

## 🎮 Use Cases

### Pour l'Administrateur

Un administrateur peut/doit :
- [Lister les actions que l'administrateur peut/doit effectuer pour lancer/administrer une arène de jeu avec des apprenants.]

### Pour le Joueur

Pour les informations sur le joueur, veuillez vous référer au [README](/src/api/README.md) de l'API. 

## 🖧 Architecture Matériel (Optionnel)

[Insérer un schéma overview présentant les machines et protocoles utilisés (serveurs, clients, broker) avec un texte expliquant le choix des technologies.]

## 📞 Diagramme de Séquence

[Expliquer le déroulé d'une partie à l'aide d'un diagramme de séquence. Décrire les principales étapes et comment les couches s'échangent des données.]
Expliquer les points suivants:
- [ ] les acteurs
- [ ] le déroulé d'une partie en partant des use case
- [ ] les données échangées entre chaque couche
- [ ] les algorithmes
- [ ] les machines
- [ ] les protocoles réseaux

## ✅ Pré-requis

### Pour l'Administrateur

- [Liste du matériel requis.]
- [Liste du logiciel requis.]

### Pour les Apprenants

Pour les prérequis des apprenants, veuillez vous référer au [README](/src/api/README.md) de l'API.

## ⚙️ Installation

Step by step : commandes à executer par l'administrateur, paquets à installer ...

## 🧪 Tests

### Définition du Plan de Test

[Expliquer ce qu'on attend quand on fait quoi.]

### Étapes pour Lancer les Tests


## 🛣️ Roadmap

[Insérer la roadmap du projet, décrivant les fonctionnalités futures, les améliorations, etc.]
Ce qui reste à faire priorisé dans le temps

## 🧑‍💻 Auteur

- Antoine CLERICE
- Thomas FEDORAWIEZ
- Léo HARNOIS
- Pierre TOITOT

## ⚖️ Licence

Ce projet est sous licence [Insérer le type de licence]. Consultez le fichier `LICENSE.md` pour plus d'informations.

S'appuyer sur https://choosealicense.com/ ou la doc de github
Attention à vérifier la compatibilité de votre licence avec celles des modules utilisés

