# Portfolio IA - Site Web Django

Portfolio moderne et responsive pour un expert en Intelligence Artificielle, développé avec Django.

## 🚀 Fonctionnalités

- **Design moderne et responsive** : Optimisé pour tous les appareils (mobile, tablette, desktop)
- **SEO optimisé** : Meta tags, sitemap, robots.txt, structure sémantique
- **Accessibilité** : Conforme aux standards WCAG avec navigation au clavier et lecteurs d'écran
- **Performance** : Chargement optimisé, lazy loading, minification
- **Sécurité** : Protection CSRF, headers de sécurité, validation des formulaires

## 📋 Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

## 🔧 Installation

1. **Cloner le projet** (si applicable) ou naviguer dans le dossier du projet

2. **Créer un environnement virtuel** (recommandé) :
```bash
python -m venv venv
```

3. **Activer l'environnement virtuel** :
   - Sur Windows :
   ```bash
   venv\Scripts\activate
   ```
   - Sur macOS/Linux :
   ```bash
   source venv/bin/activate
   ```

4. **Installer les dépendances** :
```bash
pip install -r requirements.txt
```

5. **Appliquer les migrations** :
```bash
python manage.py migrate
```

6. **Créer un superutilisateur** (optionnel, pour accéder à l'admin Django) :
```bash
python manage.py createsuperuser
```

7. **Collecter les fichiers statiques** :
```bash
python manage.py collectstatic --noinput
```

## 🏃 Lancer le serveur de développement

```bash
python manage.py runserver
```

Le site sera accessible à l'adresse : http://127.0.0.1:8000/

## 📁 Structure du projet

```
portfolio/
├── manage.py
├── portfolio_project/          # Configuration du projet Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── portfolio/                  # Application principale
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── templates/
│       └── portfolio/
│           ├── base.html
│           ├── home.html
│           ├── about.html
│           ├── projects.html
│           └── contact.html
├── static/                     # Fichiers statiques
│   ├── css/
│   │   ├── reset.css
│   │   ├── main.css
│   │   └── responsive.css
│   ├── js/
│   │   └── main.js
│   └── images/
├── requirements.txt
└── README.md
```

## 🎨 Personnalisation

### Modifier les couleurs

Les couleurs sont définies dans `static/css/main.css` via les variables CSS :
```css
:root {
    --primary-color: #4F46E5;
    --secondary-color: #10B981;
    /* ... */
}
```

### Ajouter du contenu

- **Page d'accueil** : `portfolio/templates/portfolio/home.html`
- **Page À propos** : `portfolio/templates/portfolio/about.html`
- **Page Projets** : `portfolio/templates/portfolio/projects.html`
- **Page Contact** : `portfolio/templates/portfolio/contact.html`

### Modifier les métadonnées SEO

Les métadonnées sont définies dans chaque template HTML et peuvent être modifiées dans les vues Django (`portfolio/views.py`).

## 🔒 Sécurité

Pour la production, assurez-vous de :

1. **Changer la SECRET_KEY** dans `settings.py` :
```python
SECRET_KEY = os.environ.get('SECRET_KEY', 'votre-cle-secrete-ici')
```

2. **Désactiver DEBUG** :
```python
DEBUG = False
```

3. **Configurer ALLOWED_HOSTS** :
```python
ALLOWED_HOSTS = ['votre-domaine.com']
```

4. **Utiliser HTTPS** : Les paramètres de sécurité sont déjà configurés dans `settings.py` pour la production.

## 📱 Responsive Design

Le site est entièrement responsive avec des breakpoints pour :
- Mobile : jusqu'à 480px
- Tablette : jusqu'à 768px
- Desktop : 1200px et plus

## ♿ Accessibilité

Le site respecte les standards d'accessibilité :
- Navigation au clavier
- Attributs ARIA appropriés
- Contraste des couleurs
- Skip links
- Support des lecteurs d'écran

## 🚀 Déploiement

### Vercel
1. Installer Vercel CLI : `npm i -g vercel`
2. Déployer : `vercel`

### Heroku
1. Installer Heroku CLI
2. Créer un `Procfile` :
```
web: gunicorn portfolio_project.wsgi --log-file -
```
3. Déployer : `git push heroku main`

### Autres plateformes
Le projet Django standard peut être déployé sur n'importe quelle plateforme supportant Python/Django.

## 📝 Licence

Ce projet est sous licence MIT.

## 👤 Auteur

Portfolio IA - Expert en Intelligence Artificielle

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

