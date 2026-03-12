from django.shortcuts import render


def home(request):
    """Page d'accueil du portfolio."""
    context = {
        'page_title': 'Portfolio IA - Expert en Intelligence Artificielle',
        'meta_description': 'Portfolio d\'un expert en Intelligence Artificielle. Découvrez mes projets, compétences et réalisations en IA, Machine Learning et Deep Learning.',
    }
    return render(request, 'portfolio/home.html', context)


def about(request):
    """Page à propos."""
    context = {
        'page_title': 'À propos - Portfolio IA',
        'meta_description': 'En savoir plus sur mon parcours et mes compétences en Intelligence Artificielle.',
    }
    return render(request, 'portfolio/about.html', context)


def projects(request):
    """Page des projets."""
    context = {
        'page_title': 'Projets - Portfolio IA',
        'meta_description': 'Découvrez mes projets en Intelligence Artificielle, Machine Learning et Deep Learning.',
    }
    return render(request, 'portfolio/projects.html', context)


def contact(request):
    """Page de contact."""
    context = {
        'page_title': 'Contact - Portfolio IA',
        'meta_description': 'Contactez-moi pour discuter de vos projets en Intelligence Artificielle.',
    }
    return render(request, 'portfolio/contact.html', context)

