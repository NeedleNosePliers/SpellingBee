/* Service worker : met tout en cache au premier chargement,
   puis sert depuis le cache → le jeu fonctionne sans Internet. */
const CACHE = "spelling-bee-fr-v1";
const FICHIERS = ["./", "./index.html", "./manifest.json", "./icone.svg"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(FICHIERS)));
  self.skipWaiting();
});

self.addEventListener("activate", e => {
  e.waitUntil(
    caches.keys().then(cles =>
      Promise.all(cles.filter(k => k !== CACHE).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", e => {
  e.respondWith(
    caches.match(e.request, { ignoreSearch: true })
      .then(rep => rep || fetch(e.request))
  );
});
