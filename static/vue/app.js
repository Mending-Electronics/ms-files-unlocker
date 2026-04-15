// app.js (ES5 style) - Application Vue générique
(function () {
  console.log('Initializing generic Vue app...');
  
  var app = Vue.createApp({
    template: `
      <div>
      <!-- <Navbar v-if="showNavbar"></Navbar> // inject globaly this component in all views -->
      <!-- <Navbar v-if="showNavbar"></Navbar> -->
        <div class="container-fluid">
          <router-view></router-view>
        </div>
        <!-- <FooterComp></FooterComp> // inject globaly this component in all views -->
        <!-- <FooterComp></FooterComp> -->
        <Toast v-for="toast in toasts" 
          :key="toast.id" 
          :title="toast.title" 
          :message="toast.message" 
          :type="toast.type" 
          :duration="toast.duration">
        </Toast>
        <Modale v-if="modale.visible" 
          :title="modale.title" 
          :visible="modale.visible" 
          @close="closeModale" 
          @confirm="confirmModale">
          <div v-html="modale.content"></div>
        </Modale>
        <OffCanvas v-if="offcanvas.visible" 
          :title="offcanvas.title" 
          :visible="offcanvas.visible" 
          @close="closeOffCanvas">
          <div v-html="offcanvas.content"></div>
        </OffCanvas>
      </div>`,
    data: function() {
      return {
        showNavbar: true,
        showFooter: true,
        toasts: [],
        modale: {
          visible: false,
          title: '',
          content: '',
          onConfirm: null
        },
        offcanvas: {
          visible: false,
          title: '',
          content: ''
        }
      };
    },
    mounted: function() {
      // Global toast method
      window.showToast = this.showToast.bind(this);
      
      // Global modal method
      window.showModal = this.showModal.bind(this);
      
      // Global offcanvas method
      window.showOffCanvas = this.showOffCanvas.bind(this);
      
      console.log('Generic app mounted with global methods');
      console.log('showToast method available:', typeof window.showToast);



    // initialise Bootstrap pour tous les toggles rendus par Vue
    var toggles = document.querySelectorAll('[data-bs-toggle="dropdown"]');
    toggles.forEach(function(el) {
      // crée/obtient l'instance Bootstrap
      bootstrap.Dropdown.getOrCreateInstance(el);

      // fallback local : garantit l'ouverture même si un listener global interfère
      el.addEventListener('click', function(ev) {
        ev.preventDefault();
        bootstrap.Dropdown.getOrCreateInstance(ev.currentTarget).toggle();
      }, false);
    });








    },
    methods: {
      showToast: function(message, type, title, duration) {
        console.log('showToast called with:', {message: message, type: type, title: title, duration: duration});
        
        var toast = {
          id: Date.now(),
          message: message || 'Notification',
          type: type || 'info',
          title: title || 'Notification',
          duration: duration || 3000
        };
        
        console.log('Adding toast to array:', toast);
        this.toasts.push(toast);
        console.log('Current toasts array:', this.toasts);
        
        // Auto remove toast après la durée (pour nettoyer le tableau)
        var self = this;
        if (toast.duration > 0) {
          setTimeout(function() {
            self.toasts = self.toasts.filter(function(t) { return t.id !== toast.id; });
            console.log('Toast removed from array, remaining:', self.toasts.length);
          }, toast.duration + 500); // +500ms pour laisser le temps au toast Bootstrap de se cacher
        }
      },
      showModal: function(title, content, onConfirm) {
        this.modale = {
          visible: true,
          title: title || 'Confirmation',
          content: content || '',
          onConfirm: onConfirm || null
        };
      },
      closeModale: function() {
        this.modale.visible = false;
      },
      confirmModale: function() {
        if (this.modale.onConfirm) {
          this.modale.onConfirm();
        }
        this.closeModale();
      },
      showOffCanvas: function(title, content) {
        this.offcanvas = {
          visible: true,
          title: title || 'Menu',
          content: content || ''
        };
      },
      closeOffCanvas: function() {
        this.offcanvas.visible = false;
      }
    }
  });

  // Set delimiters to [[ ]] to avoid PHP {{ }} conflicts
  if (app.config && app.config.compilerOptions) {
    app.config.compilerOptions.delimiters = ['[[', ']]'];
  }

  // Register global components if defined
  if (window.Navbar) {
    console.log('Registering Navbar component');
    app.component('Navbar', window.Navbar);
  }
  if (window.FooterComp) {
    console.log('Registering FooterComp component');
    app.component('FooterComp', window.FooterComp);
  }
  if (window.DashboardView) {
    console.log('Registering DashboardView component');
    app.component('DashboardView', window.DashboardView);
  }
  if (window.Toast) {
    console.log('Registering Toast component');
    app.component('Toast', window.Toast);
  }
  if (window.Modale) {
    console.log('Registering Modale component');
    app.component('Modale', window.Modale);
  }
  if (window.OffCanvas) {
    console.log('Registering OffCanvas component');
    app.component('OffCanvas', window.OffCanvas);
  }
  if (window.AlertComp) {
    console.log('Registering AlertComp component');
    app.component('AlertComp', window.AlertComp);
  }

  // Register app components
  if (window.ThreeJsApp) {
    console.log('Registering ThreeJsApp component');
    app.component('ThreeJsApp', window.ThreeJsApp);
  }
  if (window.QrCodeApp) {
    console.log('Registering QrCodeApp component');
    app.component('QrCodeApp', window.QrCodeApp);
  }
  if (window.SheetJsApp) {
    console.log('Registering SheetJsApp component');
    app.component('SheetJsApp', window.SheetJsApp);
  }
  if (window.ChartjsApp) {
    console.log('Registering ChartjsApp component');
    app.component('ChartjsApp', window.ChartjsApp);
  }

  // Use appropriate router based on current path
  var currentPath = window.location.pathname;
  var isDashboard = currentPath.includes('dashboard.php') || currentPath === '/dashboard' || currentPath.startsWith('/dashboard/');
  
  console.log('Current path:', currentPath, 'Is dashboard:', isDashboard);
  console.log('Available components:', {
    DashboardView: !!window.DashboardView,
    ThreeJsApp: !!window.ThreeJsApp,
    QrCodeApp: !!window.QrCodeApp,
    SheetJsApp: !!window.SheetJsApp,
    ChartjsApp: !!window.ChartjsApp
  });
  
  if (isDashboard && window.dashboardRouter) {
    console.log('Using dashboard router');
    app.use(window.dashboardRouter);
  } else if (!isDashboard && window.homeRouter) {
    console.log('Using home router');
    app.use(window.homeRouter);
  } else {
    console.log('No router available!');
  }
  
  console.log('Mounting generic app...');
  var mountedApp = app.mount('#app');
  console.log('Generic app mounted:', mountedApp);



})();
