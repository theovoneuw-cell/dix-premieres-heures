# Guitare — deux volets

Vingt séances d'une heure pour enseigner la guitare en cours particulier, à des ados
et des adultes. Écrit du point de vue du prof : déroulé minuté, problèmes accrochés
à la minute où ils surviennent, et une feuille détachable à donner à l'élève en fin
de cours. Tout est en tablature, il n'y a pas une portée dans le site.

| | | |
|---|---|---|
| **Volet 1 — Débutant** | `index.html` | De la première prise en main à un morceau joué en entier. |
| **Volet 2 — Intermédiaire** | `intermediaire.html` | Notes du manche, positions de gamme reliées, blues en sixtes, mi 7 ♯9, improvisation. |

Publié avec GitHub Pages. C'est une PWA : installable sur l'écran d'accueil d'un
iPhone, elle fonctionne ensuite **sans réseau**.

## L'installer sur un iPhone

1. Ouvrir l'adresse du site **dans Safari** (seul Safari sait installer une PWA sur iOS).
2. Bouton Partager → **Sur l'écran d'accueil**.
3. L'app s'ouvre en plein écran, sans barre d'adresse, et reste disponible en mode avion.

Pour recevoir une mise à jour : ouvrir l'app avec du réseau, la fermer complètement
depuis le sélecteur d'apps, la rouvrir.

## Exporter une feuille élève

Chaque feuille détachable a un bouton **Exporter cette feuille en PDF**. Le JavaScript
masque tout le reste de la page et appelle l'impression du navigateur : pas de
bibliothèque, texte vectoriel, et ça marche hors ligne. Sur iPhone, l'aperçu
d'impression permet d'envoyer le PDF directement par Messages ou Mail.

## Structure

| Fichier | Rôle |
|---|---|
| `index.html`, `intermediaire.html` | Les deux volets. Générés — voir plus bas. |
| `assets.css` | Polices (Instrument Serif, Libre Franklin, IBM Plex Mono) embarquées en base64, puis l'identité. Aucun appel réseau. |
| `app.js` | Diagrammes d'accords en SVG, rythmiques, compteur de minutes, export PDF, enregistrement du service worker. |
| `sw.js` | Service worker. C'est lui qui rend l'app utilisable hors ligne. |
| `icons/`, `icon.swift` | Manche de guitare vu de face. Le script Swift régénère les cinq tailles. |
| `build/` | Le générateur et les sources. |

## Modifier le contenu

Le volet intermédiaire est décrit **en données** dans `build/build.py` : chaque séance
est une liste d'étapes `(type, minute, durée, titre, texte, [(problème, correction)])`.
Le volet débutant est conservé tel quel dans `build/debutant-*.html`.

```
cd build && python3 build.py
```

Le script vérifie que chaque séance fait bien 60 minutes et affiche le nombre de
minutes où l'élève a l'instrument en main — la règle du site est de ne jamais
descendre sous 35.

## Prévisualiser avant de publier

```
python3 build/serve.py 8000
```

Puis http://localhost:8000/. Le serveur envoie `no-store` et déclare les bons types
MIME — le serveur Python de base sert `.webmanifest` en binaire, ce qui casse
l'installation de la PWA.

Le service worker ne s'enregistre pas sur `localhost` et s'y désinscrit s'il traîne
d'une session précédente : sans ça il servirait son cache et masquerait les
modifications en cours.

**Après toute modification de contenu, incrémenter `CACHE` dans `sw.js`**
(`guitare-v3` → `v4`). Sinon les appareils où la PWA est déjà installée continuent
de servir l'ancienne version depuis leur cache, et le déploiement reste invisible
pour eux.

## Sources du volet intermédiaire

Construit à partir de feuilles de cours manuscrites (théorie ton/demi-ton, positions
de pentatonique, grille de « Hey Joe », exercice de mouvement perpétuel) et de deux
partitions de travail (un arrangement de blues en accords de sixte, une transcription
de « Purple Haze »).

Les tablatures de ces deux partitions ne sont pas reproduites : elles sont protégées.
Le site en enseigne les techniques avec ses propres exercices, et donne les grilles
d'accords, qui ne le sont pas.
