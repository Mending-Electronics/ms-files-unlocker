// home-router.js (ES5 style)
(function () {
  // Function to get component with fallback
  function getComponent(componentName) {
    return window[componentName] || { template: '<div>Loading ' + componentName + '...</div>' };
  }

  var routes = [
    { path: '/', component: getComponent('HomeView') },
    { path: '/login', component: getComponent('LoginView') },
    { path: '/signup', component: getComponent('SignupView') },
    { path: '/logout', component: getComponent('LogoutView') }
  ];

  console.log('Creating home router with routes:', routes);

  window.homeRouter = VueRouter.createRouter({
    history: VueRouter.createWebHistory(),
    routes: routes
  });

  console.log('Home router created:', window.homeRouter);

  // Navigation guard for authentication
  window.homeRouter.beforeEach(function (to, from, next) {
    console.log('Home navigation guard:', to.path);
    if (to.path === '/logout') {
      // Handle logout
      window.location.href = '/logout';
      return;
    }
    console.log('Home navigation allowed');
    next();
  });
})();
