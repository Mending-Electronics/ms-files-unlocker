// Modale.vue
(function () {
  window.Modale = {
    template: `
      <div v-if="visible" class="modal fade show" style="display: block; background-color: rgba(0,0,0,0.5);" @click="closeOnBackdrop">
        <div class="modal-dialog" @click.stop>
          <div class="modal-content">
            <div class="modal-header" v-if="title">
              <h5 class="modal-title">[[ title ]]</h5>
              <button type="button" class="btn-close" @click="close"></button>
            </div>
            <div class="modal-body">
              <slot></slot>
            </div>
            <div class="modal-footer" v-if="showFooter">
              <button type="button" class="btn btn-secondary" @click="close">[[ cancelText ]]</button>
              <button type="button" :class="confirmClass" @click="confirm">[[ confirmText ]]</button>
            </div>
          </div>
        </div>
      </div>`,
    props: {
      visible: { type: Boolean, default: false },
      title: { type: String, default: '' },
      confirmText: { type: String, default: 'Confirmer' },
      cancelText: { type: String, default: 'Annuler' },
      confirmClass: { type: String, default: 'btn-primary' },
      showFooter: { type: Boolean, default: true },
      closeOnBackdrop: { type: Boolean, default: true }
    },
    emits: ['close', 'confirm'],
    methods: {
      close: function() {
        this.$emit('close');
      },
      confirm: function() {
        this.$emit('confirm');
      },
      closeOnBackdrop: function(event) {
        if (this.closeOnBackdrop && event.target === event.currentTarget) {
          this.close();
        }
      }
    }
  };
})();
