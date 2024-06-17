# Library_project
# Gestionnaire de Bibliothèque

## Description

Cette application permet de gérer une bibliothèque avec les fonctionnalités suivantes :
- Ajouter des livres
- Rechercher des livres
- Prêter des livres
- Retourner des livres

## Structure du projet

Project_Library/
├── main.py
├── library_manager/
│   ├── __init__.py
│   ├── book.py
│   ├── library.py
│   └── book_database.py
└── tests/
    ├── __init__.py
    ├── test_book.py
    ├── test_integration.py
    └── test_library.py
# J'ai fait les tests unittaires avec pytest et les tests d'intégrations