# Projet — Analyse simple de logs réseau

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

[ ] `.venv` commité
[ ] `__pycache__` présent
[x] Pas de `.gitignore`