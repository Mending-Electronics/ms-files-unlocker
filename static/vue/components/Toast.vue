// Toast.vue
(function () {
  window.Toast = {
    template: `
      <div ref="toastElement" class="toast position-fixed top-0 end-0 m-3" style="z-index: 99999;" role="alert">
        <div class="toast-header" :class="{
             'bg-success text-white': type === 'success',
             'bg-warning text-white': type === 'warning', 
             'bg-danger text-white': type === 'danger',
             'bg-info text-white': type === 'info'
           }">
          <i class="me-2" :class="{
            'bi bi-check-circle-fill': type === 'success',
            'bi bi-exclamation-triangle-fill': type === 'warning',
            'bi bi-x-circle-fill': type === 'danger',
            'bi bi-info-circle-fill': type === 'info'
          }"></i>
          <strong class="me-auto">[[ title ]]</strong>
          <button type="button" class="btn-close" @click="hideToast"></button>
        </div>
        <div class="toast-body bg-body text-body">
          [[ message ]]
        </div>
      </div>`,
    props: {
      title: { type: String, default: 'Notification' },
      message: { type: String, required: true },
      type: { type: String, default: 'info' }, // success, warning, info, danger
      duration: { type: Number, default: 3000 }
    },
    data: function() {
      return {
        bsToast: null
      };
    },
    computed: {
    },
    mounted: function() {
      var self = this;
      console.log('Toast component mounted, initializing Bootstrap toast');
      
      // Initialiser le toast Bootstrap
      if (typeof bootstrap !== 'undefined' && this.$refs.toastElement) {
        this.bsToast = new bootstrap.Toast(this.$refs.toastElement, {
          delay: this.duration,
          autohide: this.duration > 0
        });
        
        // Afficher le toast
        setTimeout(function() {
          if (self.bsToast) {
            self.bsToast.show();
            console.log('Bootstrap toast shown');
          }
        }, 100);
      } else {
        console.error('Bootstrap not available or toast element not found');
      }
    },
    beforeUnmount: function() {
      if (this.bsToast) {
        this.bsToast.dispose();
      }
    },
    methods: {
      hideToast: function() {
        if (this.bsToast) {
          this.bsToast.hide();
        }
      }
    }
  };
})();
