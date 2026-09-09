// Deux volets + une feuille de style qui contient les polices en base64.
// Stratégie : cache d'abord, réseau ensuite. L'app fonctionne en avion.
// ⚠ Incrémenter CACHE à chaque modification de contenu, sinon les appareils
//   où la PWA est déjà installée continuent de servir l'ancienne version.
const CACHE = 'guitare-v5';
const ASSETS = [
  './', './index.html', './intermediaire.html',
  './assets.css', './app.js', './manifest.webmanifest',
  './icons/apple-touch-icon.png', './icons/icon-192.png',
  './icons/icon-512.png', './icons/favicon-32.png'
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') return;
  e.respondWith(
    caches.match(e.request).then((hit) =>
      hit || fetch(e.request).then((res) => {
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put(e.request, copy));
        return res;
      }).catch(() => caches.match('./index.html'))
    )
  );
});
