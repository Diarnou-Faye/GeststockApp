# Projet : Réalisation d'une Application de gestion de stock de produits

Dans le cadre des évaluations en Base de données de notre master en sciences de données etApplication, 
on nous a demander de réaliser une application de notre choix qui permet de faire l'interfacage entre Python 
et SQL.
Nous avons choisi d'utiliser le framework Django de Python pour gérer la parti backend du projet et Xamp avec
son serveur Apach pour gérer notre base de données SQL

Pour pouvoir éxecuter le projet il faut d'abord avoir Xamp et Django déja installé
une fois celà fait éxecuter d'abord les migrations avant de pouvoir lancer le projet

Commandes à éxecuter:
### python pip install Django
### pip install mysqlclient
### pip install pymysql  
### python manage.py CREATE DATABASE sondage
### python manage.py makemigrations
### python manage.py migrate

# 1. Présentation du projet :
## 1.1 Contexte :
Dans un contexte de digitalisation croissante des processus d'affaires, les entreprises se tournent de plus en plus vers des solutions numériques pour optimiser la gestion de leurs ressources. La gestion de stock, essentielle pour assurer une continuité dans la chaîne d'approvisionnement et la satisfaction de la demande, est souvent l'une des principales sources de coûts et de complexité dans les entreprises. Les méthodes traditionnelles de suivi des stocks, comme les registres papier ou les feuilles de calcul, montrent leurs limites en termes de précision, de temps, et de capacité d’analyse.
Face à ces défis, une application de gestion de stock devient un outil essentiel pour les entreprises de toutes tailles. Une telle application facilite le suivi en temps réel des quantités disponibles, des réapprovisionnements, des mouvements de stock et des niveaux de commande, tout en optimisant les coûts liés aux inventaires.

## 1.2 Problématique :
Les entreprises rencontrent des difficultés récurrentes pour gérer efficacement leurs stocks, ce qui peut conduire à plusieurs problématiques :

    • Des erreurs fréquentes dans la comptabilisation des produits en stock, menant à des ruptures ou à des surplus coûteux.
    • Un manque de visibilité en temps réel sur les niveaux de stock, rendant difficile l’ajustement rapide face à la demande.
    •Une absence d’outils de suivi des mouvements de stock (entrées et sorties), rendant complexe la traçabilité des produits.
    •Des délais dans les commandes ou réapprovisionnements, causés par un manque de données centralisées et facilement accessibles.
Ces problèmes peuvent entraîner des coûts supplémentaires, une insatisfaction des clients et une baisse de l'efficacité opérationnelle de l'entreprise. Dans ce contexte, le développement d'une application de gestion de stock vise à répondre à ces besoins en fournissant un outil précis, intuitif et facilement accessible.

## 1.3 Objectifs :
### 1.3.1 Objectif générale :
Développer une application de gestion de stock de produits qui permet aux entreprises d'optimiser leur gestion des inventaires, de suivre les mouvements de stock en temps réel et de minimiser les coûts liés à la logistique et au réapprovisionnement.
### 1.3.2 Objectifs spécifiques :
    • Suivi en Temps Réel
    • Gestion des Mouvements de Stock
    • Réapprovisionnement Automatique
    • Rapports et Analyse
    • Accès et Sécurité
