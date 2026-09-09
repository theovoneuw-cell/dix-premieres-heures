# Les dix premières heures

Dix séances d'une heure pour démarrer un guitariste débutant, à destination du prof :
déroulé minuté, problèmes accrochés à la minute où ils surviennent, et une feuille
détachable à donner à l'élève en fin de cours. Tout est en tablature.

Publié avec GitHub Pages. C'est une PWA : installable sur l'écran d'accueil d'un iPhone,
elle fonctionne ensuite **sans réseau**.

## L'installer sur un iPhone

1. Ouvrir l'adresse du site **dans Safari** (pas Chrome : seul Safari sait installer une
   PWA sur iOS).
2. Bouton Partager → **Sur l'écran d'accueil**.
3. L'icône apparaît sur l'écran d'accueil. L'app s'ouvre en plein écran, sans barre
   d'adresse, et le contenu reste disponible en mode avion.

Pour recevoir une mise à jour : ouvrir l'app une fois avec du réseau, la fermer
complètement (glisser vers le haut depuis le sélecteur d'apps), la rouvrir.

## Structure

| Fichier | Rôle |
|---|---|
| `index.html` | Toute la page, autonome. Les trois polices (Zilla Slab, Spectral, IBM Plex Mono) sont embarquées en base64 : aucun appel réseau. |
| `sw.js` | Service worker. Cache d'abord, réseau ensuite. C'est lui qui rend l'app utilisable hors ligne. |
| `manifest.webmanifest` | Nom, icônes, couleurs, mode plein écran. |
| `icons/` | Manche de guitare vu de face, généré par `icon.swift`. |

## Modifier le contenu

Tout est dans `index.html`, y compris le CSS et le JavaScript qui dessinent les
diagrammes d'accords et les rythmiques. Après modification, **incrémenter le numéro de
version dans `sw.js`** (`dix-heures-v1` → `v2`), sinon les appareils qui ont déjà
installé l'app continueront de servir l'ancienne version depuis leur cache.

## Impression

La feuille d'impression est prévue : une séance par page, la feuille élève jamais coupée
en deux, fond blanc. Cmd+P depuis un navigateur de bureau.
