# La Réunion DataCup Challenge 2024 - ESI'Flipside

La [Réunion DataCup Challenge](https://data.regionreunion.com/p/page-reunion-datacup-challenge) est un événement unique où toutes les compétences en manipulation de données sont mises à l’honneur : extraction, traitement, modélisation… Porté par la Région Réunion, *La Réunion DataCup Challenge* s'inscrit dans un cadre de coopération avec les producteurs de données du territoire souhaitant ouvrir, mutualiser et valoriser leurs données. Les thématiques des partenaires sont variées : de la préservation des ressources à l’économie, ou encore des préoccupations des collectivités territoriales et de leurs habitants.

L’objectif de cette seconde édition est de continuer à fédérer une communauté autour des données ouvertes du territoire ainsi qu'initier des projets pérennisables et utiles au plus grand nombre.


## ESI'Flipside

Notre équipe a choisi de répondre au défi **La bonne adresse** porté par **EDF et Réunion THD**

Ce défi s'inscrit dans un contexte où de nombreux organismes publics et privés disposent de listes d’adresses qui, collectées au fil du temps, ne sont que rarement contrôlées ou mises à jour. En conséquence, la qualité de ces informations se dégrade progressivement, rendant difficile leur exploitation efficace. Le défi consiste à comparer les données adresses sources à des référentiels existants, d’identifier les données incorrectes et de proposer des pistes de solutions pour les corriger.

Il a pour objectif de concevoir un prototype d’outil d’aide à la correction d’un fichier d’adresses. Cet outil, basé sur une comparaison avec les données de la BAN (Base Adresse Nationale) et de l’ARCEP, permettra non seulement de détecter les écarts entre les sources et les référentiels, mais également de proposer des corrections pertinentes. Par ailleurs, une analyse statistique de la qualité des données sources et une visualisation cartographique des adresses seront également incluses dans le prototype.



## **Documentation**

Notre solution répond au problème de la qualité et de la mise à jour des bases d'adresses, souvent collectées au fil du temps sans contrôle régulier. Elle consiste à croiser les bases d'adresses avec celles fournies par les communes et à proposer des mises à jour des données en fonction d'un éventail de conditions. Cette solution s'adresse à tous les organismes ou collectivités qui souhaiteraient valoriser leur base d'adresses de manière accessible.

### **Installation**

[Guide d'installation (en Anglais)](/INSTALL.md)

### **Utilisation**


Notre solution est visée à ce que ça soit open-source, accessible à tout le monde, y compris les entreprises nécessitant de créer une base de données d'adresse. Tout d'abord, une fois que l'application est déployée, les utilisateurs pourront avoir accès à un site permettant de prendre en entrée un fichier CSV contenant au moins une colonne pour chaque spécificité d'une adresse (numéro, nom, coordonnées, longitudes & latitudes) et la ville concernée. Le site va donc pouvoir analyser ce fichier en le comparant avec le fichier CSV de la Base d'Adresses Nationale (BAN) qu'il pourra récupérer grâce à l'API lié au site contenant les adresses de France (https://adresse.data.gouv.fr).\
\
Le résultat de cette comparaison sera le même fichier CSV avec les corrections appliquées par le backend autonome du site, qui permettra aux utilisateurs de gagner du temps.


### **Contributions**

Si vous souhaitez contribuer à ce projet, merci de suivre les [recommendations](/CONTRIBUTING.md).

### **Licence**

Le code est publié sous licence [MIT](/licence.MIT).

Les données référencés dans ce README et dans le guide d'installation sont publiés sous [Etalab Licence Ouverte 2.0](/licence.etalab-2.0).
