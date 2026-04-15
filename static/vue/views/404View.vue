// 404View.vue
(function () {
  window.NotFoundView = {
    template: `
      <div class="container">
        <Navbar></Navbar>
        <div class="py-5 text-center">
          <div class="display-1 text-muted">404</div>
          <h2 class="mb-4">Page non trouvée</h2>
          <p class="lead text-muted">La page que vous recherchez n'existe pas.</p>
          <div class="mt-4">
            <a class="btn btn-primary" href="/">Retour à l'accueil</a>
          </div>
        </div>
        <FooterComp></FooterComp>
      </div>`
  };
})();
