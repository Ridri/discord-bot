# Projet : créer un bot discord

## Fonctionnalités :

* ### Gestion des évènements :

* on_ready
    * Une fois que le bot est connecté au client et a terminé sa configuration, le client renvoie l'évènement on_ready.

* on_member_join
    * Quand un utilisateur rejoint le serveur discord sur lequel se trouve le bot, le client renvoie l'évènement on_member_join.

* on_member_remove
    * Quand un utilisateur quitte le serveur discord sur lequel se trouve le bot, le client renvoie l'évènement on_member_join.

* ### Gestion du bot :

* ping
    * Quand la commande `$ping` est utilisée sur le serveur, le bot renvoie sa latence (son temps de réponse).

* status
    * Quand la commande `$status` est utilisée sur le serveur, le statut et l'activité du bot sont actualisées selon les paramètres entrés.

* ### Gestion des membres :

* delete
    * La commande `$del` permet de supprimer un nombre de messages donnés.
      
* kick
    * La commande `$kick` permet d'expulser (kick) un membre du serveur.
      
* ban

* ### Gestion du serveur

* *vide*
