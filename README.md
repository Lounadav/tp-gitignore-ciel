# Projet — Analyse simple de logs réseau
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Repo Size](https://img.shields.io/github/repo-size/Lounadav/tp-gitignore-ciel)
![Issues](https://img.shields.io/github/issues/Lounadav/tp-gitignore-ciel)
![CyberSecurity](https://img.shields.io/badge/Focus-Cybersecurity-red.svg)

Nom du dépôt GitHub : **`tp-gitignore-ciel`**

## Contexte

> Vous êtes technicien réseau / cybersécurité.
> Vous devez analyser rapidement des journaux (logs) pour détecter :
>
> * des tentatives de connexion suspectes
> * des adresses IP répétées
> * des erreurs fréquentes

Ce type de script est **courant en supervision, SOC, ou administration système**.

## Fonctionnalités du projet

Le script Python :

* lit un fichier de logs réseau
* extrait les adresses IP
* compte les tentatives par IP
* met en évidence les IP suspectes

## Librairies utilisées

* `colorama` → affichage coloré (alertes)
* `tabulate` → affichage en tableau
* `python-dateutil` → gestion des dates (optionnel)

## Structure du dépôt

```text
tp-gitignore-ciel/
├── .venv/                  ← NE DEVRAIT PAS ÊTRE VERSIONNÉ
├── __pycache__/            ← NE DEVRAIT PAS ÊTRE VERSIONNÉ
├── logs/
│   └── auth.log
├── main.py
├── requirements.txt
└── README.md
```
1er commit :

[ ] `.venv` commité

[ ] `__pycache__` présent

[x] Pas de `.gitignore`

2ème commit: 

[X] `.venv` supprimé de Github

[X] `__pycache__` supprimé de Github

[x] Présence `.gitignore`

3ème commit : 

[X] `Read.me` modifié

[X] Ajout de `Reponse.md`