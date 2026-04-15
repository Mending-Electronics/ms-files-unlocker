// OffCanvas.vue
(function () {
  window.OffCanvas = {
    template: `
      <div v-if="visible" class="offcanvas offcanvas-start show" style="visibility: visible;" tabindex="-1">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title">[[ title ]]</h5>
          <button type="button" class="btn-close text-reset" @click="close"></button>
        </div>
        <div class="offcanvas-body">
          <slot></slot>
        </div>
      </div>
      <div v-if="visible" class="offcanvas-backdrop fade show" @click="close"></div>`,
    props: {
      visible: { type: Boolean, default: false },
      title: { type: String, default: 'Menu' }
    },
    emits: ['close'],
    methods: {
      close: function() {
        this.$emit('close');
      }
    }
  };
})();
