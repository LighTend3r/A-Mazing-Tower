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
    - Des pièces apparaissent aléatoirements dans les 4 labyrinthes.
    - Les joueurs peuvent se déplacer dans les labyrinthes en utilisant des téléporteurs.
    - Dès qu'il n'y a plus de pièces, les labyrinthes sont réinitialisés.

- **Conditions de Victoire :** Être le joueur ayant ramassé le plus de pièces. 

## 🎮 Use Cases

### Pour l'Administrateur

Un administrateur peut/doit :
- [Lister les actions que l'administrateur peut/doit effectuer pour lancer/administrer une arène de jeu avec des apprenants.]

### Pour le Joueur

Pour les informations sur le joueur, veuillez vous référer au [README](/src/api/README.md) de l'API. 

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

- Python 3.12 ou plus 🐍
- une arène dans Pytactx


### Pour les Apprenants

Pour les prérequis des apprenants, veuillez vous référer au [README](/src/api/README.md) de l'API.

## ⚙️ Installation

- `pip install paho-mqtt pillow requests`
- `git clone https://github.com/LighTend3r/A-Mazing-Tower.git`
- `cd scr/server`
- `python mapMaker.py`

Et voila 👍

## 🧪 Tests

### Définition du Plan de Test

[Expliquer ce qu'on attend quand on fait quoi.]

### Étapes pour Lancer les Tests

[ALED]

## 🛣️ Roadmap

[Insérer la roadmap du projet, décrivant les fonctionnalités futures, les améliorations, etc.]
Ce qui reste à faire priorisé dans le temps

## 🧑‍💻 AuteurS

- Antoine CLERICE
- Thomas FEDORAWIEZ
- Léo HARNOIS
- Pierre TOITOT

- L'équipe ***Jusdeliens*** 🔥🔥🔥


## ⚖️ Licence

Ce projet est sous licence [MIT License](https://opensource.org/license/mit/). Consultez le fichier [`LICENSE.md`](LICENSE.md) pour plus d'informations.