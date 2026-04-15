// Alert.vue
(function () {
  window.AlertComp = {
    template: `
      <div v-if="show" :class="alertClasses" role="alert">
        <div class="d-flex align-items-center">
          <i :class="iconClasses" class="me-2"></i>
          <span>[[ message ]]</span>
          <button v-if="dismissible" type="button" class="btn-close ms-auto" @click="dismiss"></button>
        </div>
      </div>
    `,
    
    props: {
      message: {
        type: String,
        required: true
      },
      type: {
        type: String,
        default: 'info',
        validator: function(value) {
          return ['info', 'success', 'warning', 'danger'].includes(value);
        }
      },
      dismissible: {
        type: Boolean,
        default: false
      },
      autoDismiss: {
        type: Boolean,
        default: false
      },
      dismissAfter: {
        type: Number,
        default: 5000
      }
    },
    
    data: function() {
      return {
        show: true,
        timeoutId: null
      };
    },
    
    computed: {
      alertClasses: function() {
        return 'alert alert-' + this.type;
      },
      
      iconClasses: function() {
        const iconMap = {
          'info': 'bi bi-info-circle-fill',
          'success': 'bi bi-check-circle-fill',
          'warning': 'bi bi-exclamation-triangle-fill',
          'danger': 'bi bi-x-circle-fill'
        };
        return iconMap[this.type] || iconMap['info'];
      }
    },
    
    mounted: function() {
      if (this.autoDismiss) {
        this.timeoutId = setTimeout(() => {
          this.dismiss();
        }, this.dismissAfter);
      }
    },
    
    beforeUnmount: function() {
      if (this.timeoutId) {
        clearTimeout(this.timeoutId);
      }
    },
    
    methods: {
      dismiss: function() {
        this.show = false;
        this.$emit('dismissed');
      }
    }
  };
})();
