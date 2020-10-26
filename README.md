
# GCP_datacatalog script python version 0.0
Détection des types de colonne d'un fichiers csv provenant de Cloud storage dans le datacatalog de GCP

# Plusieurs hypothèses
On admet l'hypothèse que tout les fichiers csv d'un bucket de cloud storage aient le même schéma  
On admet que les seuls fichiers que nous trouveront dans un buckets sont des fichiers csv ou texte avec des séparateurs  



# Les fonctionalités 
Permet de détecter le premier ficher csv d'un bucket  
Permet de détecter les types de colonnes de plus de la moitié présent dans GCP datacatalog  
- Ceux qui sont intégrés ==> INTEGER - BOOLEAN - STRING - DATE - TIME - DATETIME - FLOAT  
- Ceux qu'il faillent intégrer ==> GEOGRPAPHY  
Début de Pattern Matching intégré (expression regex)  
Création et supression d'un groupe d'entré et d'une entrée dans GCP datacatalog  
Avec la création et supression, s'accompagne la détection des types de colonnes  

# Les bémols
Script peu automatisé  
- Insertion du : - nom du bucket  
                 - nom du groupe d'entrée/Description du groupe d'entrée/ id du groupe d'entrée  
                 - nom de l'entrée/ Description de l'entrée/Id de l'entrée  
Création et suppression des groupes d'entrée et des entrées supprime les tags de ces entrées  
Effectuer le script manuellement pour chaque groupes d'entrées/entrées  

# A modifier
Pouvoir détecter une multitude de types fichier  
Pouvoir donner l'option d'update les groupes d'entrées/ les entrées  
Pouvoir update tout les groupe d'entrée/entrée par mois ou de façon jouralier  

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2FSamj0ns0n%2FGCP_datacatalog)

