from django.db import models

class Entreprise(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    secteur_activite = models.CharField(max_length=100)
    taille = models.IntegerField()
    date_creation = models.DateField()
    siege_social = models.CharField(max_length=100)
    site_web = models.URLField(max_length=200)
    numero_telephone = models.CharField(max_length=20)
    adresse_email = models.EmailField(max_length=100)
    profil_reseaux_sociaux = models.URLField(max_length=200)
    id_entreprise = models.IntegerField()

class Offre(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    type_offre = models.CharField(max_length=50, choices=[('emploi', 'Emploi'), ('stage', 'Stage')])
    domaine = models.CharField(max_length=100)
    description = models.TextField()
    competences = models.TextField()
    experience = models.CharField(max_length=100)
    diplomes = models.CharField(max_length=100)
    lieu_travail = models.CharField(max_length=100)
    type_contrat = models.CharField(max_length=50, choices=[('CDI', 'CDI'), ('CDD', 'CDD'), ('stage', 'Stage')])
    duree_contrat = models.CharField(max_length=100, blank=True, null=True)
    salaire = models.CharField(max_length=100)
    date_debut = models.DateField()
    avantages = models.TextField()
    nombre_postes = models.IntegerField()
    langues = models.CharField(max_length=100)
    date_cloture = models.DateField()