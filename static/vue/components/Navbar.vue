// Navbar.vue
(function () {
  window.Navbar = {
    template: `  
      <div class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top" data-bs-theme="dark">
      <div class="container">
        <a href="../" class="navbar-brand">
        <b>Demonstrateur  PHP/Vue</b>
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarResponsive">
          
        
        <!-- Liens a gauche dans la Navbar -->
        <ul class="navbar-nav">
           

            <template v-if="!userLoggedIn">
              <li class="nav-item"><router-link class="nav-link hover-border" to="/">Home</router-link></li>
            </template>  

            <template v-if="userLoggedIn">
              <li class="nav-item"><router-link class="nav-link hover-border" to="/dashboard">Dashboard</router-link></li>
              <li class="nav-item"><router-link class="nav-link hover-border" to="/dashboard/threejs">Three.js 3D</router-link></li>
              <li class="nav-item"><router-link class="nav-link hover-border" to="/dashboard/qrcode">QR Code</router-link></li>
              <li class="nav-item"><router-link class="nav-link hover-border" to="/dashboard/sheetjs">SheetJS Excel</router-link></li>
              <li class="nav-item"><router-link class="nav-link hover-border" to="/dashboard/chartjs">ChartJS Graphiques</router-link></li>
            </template>
       
          </ul>


          <!-- Liens a droite dans la Navbar -->
          <ul class="navbar-nav ms-md-auto">

            <template v-if="!userLoggedIn">
              <li class="nav-item"><router-link class="nav-link hover-border" to="/signup">Sign up</router-link></li>
              <li class="nav-item"><router-link class="nav-link hover-border" to="/login">Login</router-link></li>
            </template>  

            <template v-if="userLoggedIn">
              <li class="nav-item"><router-link class="nav-link text-danger" to="/logout"><i class="bi bi-door-open me-1"></i> Logout</router-link></li>
            </template>


            <li class="nav-item py-2 py-lg-1 col-12 col-lg-auto">
              <div class="vr d-none d-lg-flex h-100 mx-lg-2 text-white"></div>
              <hr class="d-lg-none my-2 text-white-50">
            </li>


            <li class="nav-item">
              <a target="_blank" rel="noopener" class="nav-link" href="https://github.com/mending-electronics"><i class="bi bi-github"></i><span class="d-lg-none ms-2">GitHub</span></a>
            </li>

            <li class="nav-item py-2 py-lg-1 col-12 col-lg-auto">
              <div class="vr d-none d-lg-flex h-100 mx-lg-2 text-white"></div>
              <hr class="d-lg-none my-2 text-white-50">
            </li>

            <li class="nav-item dropdown" data-bs-theme="light">
              <a class="nav-link dropdown-toggle d-flex align-items-center" href="#" id="theme-menu" aria-expanded="false" data-bs-toggle="dropdown" data-bs-display="static" aria-label="Toggle theme">
                <i class="bi bi-circle-half"></i>
                <span class="d-lg-none ms-2">Toggle theme</span>
              </a>
              <ul class="dropdown-menu dropdown-menu-end">
                <li>
                  <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="light" aria-pressed="false">
                    <i class="bi bi-sun-fill"></i><span class="ms-2">Light</span>
                  </button>
                </li>
                <li>
                  <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="dark" aria-pressed="true">
                    <i class="bi bi-moon-stars-fill"></i><span class="ms-2">Dark</span>
                  </button>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
      
      
      
      
      
      `,
    data: function () {
      return {
        userLoggedIn: window.__USER_LOGGED__ || false,
      };
    },
  };
})();
