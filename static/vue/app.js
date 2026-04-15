// app.js (ES5 style) - MS Files Unlocker Vue App
(function () {
  console.log('Initializing MS Files Unlocker Vue app...');
  
  var app = Vue.createApp({
    delimiters: ['[[', ']]']
  });

  // Register HomeView component
  if (window.HomeView) {
    console.log('Registering HomeView component');
    app.component('home-view', window.HomeView);
  } else {
    console.error('HomeView component not found!');
  }
  
  console.log('Mounting app...');
  var mountedApp = app.mount('#app');
  console.log('App mounted:', mountedApp);
})();;
