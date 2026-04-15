(function () {
    'use strict';

    if (typeof bootstrap === 'undefined') {
        console.error('Bootstrap is not loaded!');
        return;
    }

    function initBootstrapExtras() {

        // Tooltips
        const tooltips = [...document.querySelectorAll('[data-bs-toggle="tooltip"]')]
            .map(el => new bootstrap.Tooltip(el));

        // Popovers
        const popovers = [...document.querySelectorAll('[data-bs-toggle="popover"]')]
            .map(el => new bootstrap.Popover(el));

        // Comptage des composants Bootstrap dans la page
        const counts = {
            tooltips: tooltips.length,
            popovers: popovers.length,
            dropdowns: document.querySelectorAll('[data-bs-toggle="dropdown"]').length,
            collapses: document.querySelectorAll('[data-bs-toggle="collapse"]').length,
            modals: document.querySelectorAll('[data-bs-toggle="modal"]').length,
            offcanvas: document.querySelectorAll('[data-bs-toggle="offcanvas"]').length,
            carousels: document.querySelectorAll('[data-bs-ride="carousel"]').length,
            tabs: document.querySelectorAll('[data-bs-toggle="tab"]').length,
            buttons: document.querySelectorAll('[data-bs-toggle="button"]').length
        };

        console.log("Bootstrap components found:", counts);
    }

    // Initialisation au chargement du DOM
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initBootstrapExtras);
    } else {
        initBootstrapExtras();
    }

    // Pour Vue : réinitialiser après un rendu dynamique
    // window.initBootstrapExtras = initBootstrapExtras;

    
})();

// Patch fonctionnel dans la console pour faire fonctionner les dropdown et navbar-toggler


//     (getEventListeners(document).click || []).forEach(l => {
//         try { document.removeEventListener('click', l.listener, l.useCapture); console.log('removed', l.listener.name || l.listener.toString().slice(0,50)); }
//         catch(e){ console.warn('could not remove', e); }
//     });

// touve tous les handler Click
// if (typeof getEventListeners === 'function') {
//   (getEventListeners(document).click || []).forEach(function(l, i) {
//     console.groupCollapsed('document click listener #' + i);
//     console.log('useCapture:', !!l.useCapture);
//     try { console.log('name:', l.listener.name || '<anonymous>'); } catch(e){}
//     try { console.log('toString (first 400 chars):', l.listener.toString().slice(0,400)); } catch(e){}
//     console.log('listener object:', l.listener);
//     console.groupEnd();
//   });
// } else {
//   console.warn('getEventListeners not available in this context (use Chrome DevTools console).');
// }
