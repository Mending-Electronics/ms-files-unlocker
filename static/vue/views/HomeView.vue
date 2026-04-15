// HomeView.vue
(function () {
  window.HomeView = {
    template: `
      <div class="container">
        <Navbar></Navbar>
        <section class="py-5 my-5">

          <div class="d-flex justify-content-center align-items-center" style="min-height: calc(100vh - 120px);">
            <div class="py-5 text-center">
              <!-- Hero Section -->
              <div class="hero-section mb-5">
                <h1 class="display-4 fw-bold text-body mb-3">
                  <i class="bi bi-shield-check me-2"></i>
                  App Vue + PHP Sécurisée
                </h1>
                <p class="lead fs-4 text-muted mb-4">
                  Application web moderne avec architecture Vue.js SPA et backend PHP sécurisé
                </p>
                <div class="d-flex justify-content-center gap-3 flex-wrap">
                  <a class="btn btn-success btn-lg px-4" href="/signup">
                    <i class="bi bi-person-plus me-2"></i>Créer un compte
                  </a>
                  <a class="btn btn-primary btn-lg px-4" href="/login">
                    <i class="bi bi-box-arrow-in-right me-2"></i>Se connecter
                  </a>
                </div>
              </div>

              <!-- Features Grid -->
              <div class="features-section mb-5">
                <h2 class="h3 mb-4 text-secondary">
                  <i class="bi bi-stars me-2"></i>Fonctionnalités Principales
                </h2>
                <div class="row g-4 justify-content-center">
                  <div class="col-md-6 col-lg-4">
                    <div class="card h-100 shadow-sm border-0">
                      <div class="card-body text-center p-4">
                        <div class="feature-icon mb-3">
                          <i class="bi bi-shield-lock fs-1 text-success"></i>
                        </div>
                        <h5 class="card-title">Sécurité Renforcée</h5>
                        <p class="card-text text-muted">
                          Protection CSRF, validation des entrées, hashage des mots de passe et politiques de sécurité modernes
                        </p>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6 col-lg-4">
                    <div class="card h-100 shadow-sm border-0">
                      <div class="card-body text-center p-4">
                        <div class="feature-icon mb-3">
                          <i class="bi bi-lightning-charge fs-1 text-warning"></i>
                        </div>
                        <h5 class="card-title">Performance</h5>
                        <p class="card-text text-muted">
                          Architecture SPA avec Vue.js 3, chargement rapide et expérience utilisateur fluide
                        </p>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6 col-lg-4">
                    <div class="card h-100 shadow-sm border-0">
                      <div class="card-body text-center p-4">
                        <div class="feature-icon mb-3">
                          <i class="bi bi-gear fs-1 text-info"></i>
                        </div>
                        <h5 class="card-title">Architecture Microservice</h5>
                        <p class="card-text text-muted">
                          Structure type microservice minimaliste sans runtime/bundler JavaScript, déploiement simplifié et autonomie des services
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Apps Showcase -->
              <div class="apps-showcase mb-5">
                <h2 class="h3 mb-4 text-secondary">
                  <i class="bi bi-grid-3x3-gap me-2"></i>Applications Web Intégrées
                </h2>
                <div class="row g-4 justify-content-center">
                  <div class="col-md-6 col-lg-3">
                    <div class="card h-100 shadow-sm border-0">
                      <div class="card-body text-center p-3">
                        <i class="bi bi-box fs-2 text-primary mb-2"></i>
                        <h6 class="card-title">ThreeJS</h6>
                        <p class="card-text small text-muted">Visualisations 3D interactives</p>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6 col-lg-3">
                    <div class="card h-100 shadow-sm border-0">
                      <div class="card-body text-center p-3">
                        <i class="bi bi-bar-chart fs-2 text-success mb-2"></i>
                        <h6 class="card-title">ChartJS</h6>
                        <p class="card-text small text-muted">Graphiques et statistiques</p>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6 col-lg-3">
                    <div class="card h-100 shadow-sm border-0">
                      <div class="card-body text-center p-3">
                        <i class="bi bi-qr-code fs-2 text-warning mb-2"></i>
                        <h6 class="card-title">QR Code</h6>
                        <p class="card-text small text-muted">Générateur de QR codes</p>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6 col-lg-3">
                    <div class="card h-100 shadow-sm border-0">
                      <div class="card-body text-center p-3">
                        <i class="bi bi-file-earmark-spreadsheet fs-2 text-info mb-2"></i>
                        <h6 class="card-title">SheetJS</h6>
                        <p class="card-text small text-muted">Tableurs et données Excel</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Tech Stack -->
              <div class="tech-stack mb-5">
                <h2 class="h3 mb-4 text-secondary">
                  <i class="bi bi-stack me-2"></i>Stack Technologique
                </h2>
                <div class="d-flex justify-content-center flex-wrap gap-3">
                  <span class="badge bg-success fs-6 p-2">
                    <i class="bi bi-lightning-charge me-1"></i>Vue.js 3
                  </span>
                  <span class="badge bg-primary fs-6 p-2">
                    <i class="bi bi-server me-1"></i>PHP 8
                  </span>
                  <span class="badge bg-info fs-6 p-2">
                    <i class="bi bi-database me-1"></i>SQLite
                  </span>
                  <span class="badge bg-warning text-white fs-6 p-2">
                    <i class="bi bi-layout-wtf me-1"></i>Bootstrap 5
                  </span>
                  <span class="badge bg-danger fs-6 p-2">
                    <i class="bi bi-shield-check me-1"></i>CSRF Protection
                  </span>
                </div>
              </div>

              <!-- CTA Section -->
              <div v-if="!userLoggedIn" class="cta-section">
                <div class="card border-0 bg-gradient">
                  <div class="card-body p-4">
                    <h3 class="card-title h4 mb-3">Prêt à commencer ?</h3>
                    <p class="card-text text-muted mb-4">
                      Rejoignez-nous et découvrez une application web moderne et sécurisée
                    </p>
                    <div class="d-flex justify-content-center gap-3">
                      <a class="btn btn-success btn-lg" href="/signup">
                        <i class="bi bi-rocket-takeoff me-2"></i>Commencer maintenant
                      </a>
                    </div>
                  </div>
                </div>
              </div>

              <div v-else class="user-dashboard-link">
                <div class="card border-0 bg-success bg-opacity-10">
                  <div class="card-body p-4">
                    <h3 class="card-title h4 mb-3">
                      <i class="bi bi-person-check me-2"></i>Bienvenue de retour !
                    </h3>
                    <p class="card-text mb-4">
                      Accédez à votre tableau de bord pour utiliser toutes les fonctionnalités
                    </p>
                    <a class="btn btn-success btn-lg" href="/dashboard">
                      <i class="bi bi-speedometer2 me-2"></i>Tableau de bord
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <FooterComp></FooterComp>
      </div>`,
    data: function () {
      return {
        userLoggedIn: window.__USER_LOGGED__ || false
      };
    }
  };
})();
