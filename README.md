<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SIA : Satellite Imaging Analysis</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        h1 {
            font-size: 2.5em;
            border-bottom: 1px solid #eee;
            padding-bottom: 0.3em;
        }
        h2, h3 {
            margin-top: 1.5em;
        }
        img {
            max-width: 100%;
            height: auto;
        }
        .logo-container {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }
        .logo-container img {
            width: 80px;
            height: 80px;
            margin-right: 15px;
        }
        ul, ol {
            padding-left: 20px;
        }
        li {
            margin-bottom: 5px;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: monospace;
        }
        a {
            color: #0366d6;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <h1>SIA : Satellite Imaging Analysis</h1>

    <h2>Description</h2>
    <p>Environnement d'apprentissage des outils de traitements d'images satellites et de familiarisation avec les outils git.</p>

    <h2>Pour les non-utilisateurs/rices de Jupyter Lab</h2>
    <p>Vous devrez installer les différentes librairies utilisées (si pas déjà fait) à l'aide de pip ou mamba:</p>
    <p><code>pip install &lt;your library&gt;</code></p>

    <h2>Ressources</h2>

    <div class="logo-container">
        <img src="https://logos-world.net/wp-content/uploads/2021/10/Python-Emblem.png" alt="Python Logo">
    </div>

    <h3>Python</h3>
    <p>Vous trouverez ci-après différents liens vers les librairies utilisées :</p>
    <ul>
        <li>Lien vers la documentation Rasterio : <a href="https://rasterio.readthedocs.io/en/stable/#" target="_blank">Rasterio Documentation</a></li>
        <li>Lien vers la documentation de Collections : <a href="https://docs.python.org/3/library/collections.html" target="_blank">Collections Documentation</a></li>
    </ul>

    <h3>Données satellites</h3>
    <p>Vous trouverez ci-après différents liens vers les données des satellites Sentinel qui sont en libre accès (sous réserve de créer un compte sur l'observatoire Copernicus).</p>
    <p>Liens vers le moteur de recherche Copernicus : <a href="https://browser.dataspace.copernicus.eu/" target="_blank">Copernicus Browser</a></p>

    <h3>Worklow pour l'export de données</h3>
    <ul>
        <li>Déilimiter sa zone géographique d'intérêt</li>
        <li>Choisir le satellites souhaités <em>(Sentinel 1/2/3/5P/6, SAR, etc...)</em></li>
        <li>Choisir les dates de prises de vues souhaitées (Attention au pourcentage de la couverture nuageuse qui peut obstruer les images)</li>
        <li>Télécharger l'image
            <ul>
                <li>Choisir le format/resolution/</li>
                <li>Choisir les bandes souhaitées (Rouge, Vert, Bleu, infrarouge, autres...)</li>
                <li>Choisir le système de coordonnées pour le géoréférencement que l'on calculera ultérieurement</li>
            </ul>
        </li>
    </ul>

</body>
</html>
