# Guide de démarrage rapide

## Installation en 5 minutes

### 1. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 2. Appliquer les migrations
```bash
python manage.py migrate
```

### 3. Lancer le serveur
```bash
python manage.py runserver
```

### 4. Accéder au site
Ouvrez votre navigateur à l'adresse : **http://127.0.0.1:8000/**

## Personnalisation rapide

### Modifier le contenu
- **Page d'accueil** : `portfolio/templates/portfolio/home.html`
- **À propos** : `portfolio/templates/portfolio/about.html`
- **Projets** : `portfolio/templates/portfolio/projects.html`
- **Contact** : `portfolio/templates/portfolio/contact.html`

### Modifier les couleurs
Éditez les variables CSS dans `static/css/main.css` :
```css
:root {
    --primary-color: #4F46E5;  /* Changez cette couleur */
    --secondary-color: #10B981; /* Et celle-ci */
}
```

### Ajouter vos projets
Modifiez `portfolio/templates/portfolio/projects.html` pour ajouter vos propres projets.

## Prochaines étapes

1. **Ajouter vos images** : Placez-les dans `static/images/`
2. **Personnaliser le contenu** : Modifiez les templates HTML
3. **Configurer le formulaire de contact** : Ajoutez la logique backend dans `portfolio/views.py`
4. **Déployer** : Suivez les instructions dans `README.md`

## Support

Pour plus d'informations, consultez le `README.md` complet.

