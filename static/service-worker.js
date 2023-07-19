const CACHE_NAME = 'my-app-cache-v1';
const urlsToCache = [
  '/',
  '/admin'
];

self.addEventListener('install', function(event) {
  // Realiza a instalação do Service Worker
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Cache aberto');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
  // Intercepta as solicitações de rede
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        // Se a solicitação existe no cache, retorna a resposta do cache
        if (response) {
          return response;
        }

        // Caso contrário, faz a solicitação de rede e armazena a resposta no cache
        return fetch(event.request)
          .then(function(response) {
            // Verifica se a resposta é válida
            if (!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }

            // Clona a resposta para poder usá-la e armazena no cache
            const responseToCache = response.clone();
            caches.open(CACHE_NAME)
              .then(function(cache) {
                cache.put(event.request, responseToCache);
              });

            return response;
          });
      })
  );
});

self.addEventListener('activate', function(event) {
  // Limpa caches antigos que não correspondem ao CACHE_NAME atual
  event.waitUntil(
    caches.keys()
      .then(function(cacheNames) {
        return Promise.all(
          cacheNames.map(function(cacheName) {
            if (cacheName !== CACHE_NAME) {
              return caches.delete(cacheName);
            }
          })
        );
      })
  );
});
