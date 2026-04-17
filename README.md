# SIA : Satellite Imaging Analysis
## Description
Environnement d'apprentissage des outils de traitements d'images satellites et de familiarisation avec les outils git.

## Pour les non-utilisateurs/rices de Jupyter Lab 
Vous devrez installer les différentes librairies utilisées (si pas déjà fait) à l'aide de pip ou mamba:
'pip install <your library>'

## Ressources
<p align="center">
	<img width="211" height="71" alt="image" src="https://github.com/user-attachments/assets/154d3eeb-9452-4c87-80b9-a640e91cb702" />
</p>


### Python

Vous trouverez ci-après différents liens vers les librairies utilisées :

Lien vers la documentation Rasterio : [Rasterio Documentation](https://rasterio.readthedocs.io/en/stable/#)
Lien vers la documentation de Collections [Collections Documentation](https://docs.python.org/3/library/collections.html)
<p align="center">
	<img width="211" height="91" alt="image" src="https://github.com/user-attachments/assets/d7192930-b54b-41ff-8e76-5c836515c236" />
</p>
### Données satellites
Vous trouverez ci-après différents liens vers les données des satellites Sentinel qui sont en libre accès (sous réserve de créer un compte sur l'observatoire Copernicus).

Liens vers le moteur de recherche Copernicus : [copernicus Browser](https://browser.dataspace.copernicus.eu/)

Worklow pour l'export de données :
- Déilimiter sa zone géographique d'intérêt
- Choisir le satellites souhaités (Sentinel 1/2/3/5P/6, SAR, etc...)
- Choisir les dates de prises de vues souhaitées (Attention au pourcentage de la couverture nuageuse qui peut obstruer les images)
- Télécharger l'image
	- Choisir le format/resolution/
	- Choisir les bandes souhaitées (Rouge, Vert, Bleu, infrarouge, autres...)
	- Choisir le système de coordonnées pour le géoréférencement que l'on calculera ultérieurement
