// Footer.js
(function () {

  const { ref, onMounted, onUnmounted } = Vue

  window.FooterComp = {
    template: `
      <footer
        class="position-absolute start-0 end-0 mt-5 py-4 navbar-dark bg-primary"
        :class="{ 'sticky-bottom': isSticky }"
      >
        <div class="container">
          <div class="row d-flex justify-content-between align-items-center">

            <div class="col-md-4 text-start">
              <div class="d-flex align-items-center">
                <span class="text-white me-2">JALLET Alexandre</span>
                <a href="https://github.com/mending-electronics" target="_blank" rel="noopener" class="text-white text-decoration-none">
                  <i class="bi bi-github"></i> Mending-Electronic
                </a>
              </div>
            </div>

            <div class="col-md-4 text-center">
              <small class="text-white">© ${new Date().getFullYear()} Demonstrateur PHP & Vue (Microservice/SPA) Sécurisée</small>
            </div>

            <div class="col-md-4 text-end">
              <div class="d-flex align-items-center justify-content-end">
                <span class="text-white me-2">Made with</span>
                <i class="bi bi-heart-fill text-success"></i>
                <span class="text-white ms-2">v1.0.0</span>
              </div>
            </div>

          </div>
        </div>
      </footer>
    `,

    setup() {
      const isSticky = ref(false)

      const updateSticky = () => {
        const windowHeight = window.innerHeight
        const pageHeight = document.body.scrollHeight
        isSticky.value = pageHeight <= windowHeight
      }

      onMounted(() => {
        updateSticky()
        window.addEventListener('resize', updateSticky)
      })

      onUnmounted(() => {
        window.removeEventListener('resize', updateSticky)
      })

      return { isSticky }
    }
  }

})();
