// HomeView.vue - MS Files Unlocker
(function () {
  window.HomeView = {
    template: `
      <div class="container mt-4">
        <div class="text-center my-4">
          <h1 class="fs-2">MS Excel Tool <span class="bi bi-wrench-adjustable-circle text-secondary"></span></h1>
          <img class="mb-3" src="/static/assets/webp/unlock.webp" height="150px" alt="" />
          <p class="text-center">
            This platform simplifies Excel security management by supporting 2007 to 2016 files. 
            It lets you reset or remove passwords and protections, decode common VBA obfuscations, 
            and analyze for potential malware threats in VBA scripts.
          </p>
        </div>

        <div class="card">
          <div class="card-body">
            <!-- Feature Selection -->
            <h5 class="mb-3">Select a Process:</h5>
            <div class="row mb-4">
              <div class="col-md-6 mb-3">
                <div 
                  class="card feature-card" 
                  :class="{ selected: selectedFeature === 'xl-reset' }"
                  @click="selectFeature('xl-reset')"
                >
                  <div class="card-body">
                    <h6 class="card-title"><b>Reset Workbook and Worksheets Passwords</b></h6>
                    <p class="card-text small text-muted">
                      Used to keep protection parameters if you need to change lost password
                    </p>
                  </div>
                </div>
              </div>
              <div class="col-md-6 mb-3">
                <div 
                  class="card feature-card" 
                  :class="{ selected: selectedFeature === 'xl-remove' }"
                  @click="selectFeature('xl-remove')"
                >
                  <div class="card-body">
                    <h6 class="card-title"><b>Remove Workbook and Worksheets Protections</b></h6>
                    <p class="card-text small text-muted">
                      If you only need to remove all protections
                    </p>
                  </div>
                </div>
              </div>
              <div class="col-md-6 mb-3">
                <div 
                  class="card feature-card" 
                  :class="{ selected: selectedFeature === 'vba-remove' }"
                  @click="selectFeature('vba-remove')"
                >
                  <div class="card-body">
                    <h6 class="card-title"><b>Remove VBA Project Password</b></h6>
                    <p class="card-text small text-muted">
                      Refer to the ReadMe file to fix the VBA project after the process
                    </p>
                  </div>
                </div>
              </div>
              <div class="col-md-6 mb-3">
                <div 
                  class="card feature-card" 
                  :class="{ selected: selectedFeature === 'vba-decode' }"
                  @click="selectFeature('vba-decode')"
                >
                  <div class="card-body">
                    <h6 class="card-title"><b>Decode VBA Project Obfuscation</b></h6>
                    <p class="card-text small text-muted">
                      Hex encoding, StrReverse, Base64, VBA expressions
                    </p>
                  </div>
                </div>
              </div>
              <div class="col-md-6 mb-3">
                <div 
                  class="card feature-card" 
                  :class="{ selected: selectedFeature === 'vba-analysis' }"
                  @click="selectFeature('vba-analysis')"
                >
                  <div class="card-body">
                    <h6 class="card-title"><b>Cybersecurity Analysis</b></h6>
                    <p class="card-text small text-muted">
                      Find suspicious Malware in the VBA script like Dridex
                    </p>
                  </div>
                </div>
              </div>
            </div>

            <!-- File Upload -->
            <div 
              class="upload-zone mb-3" 
              :class="{ dragover: isDragging, 'bg-success text-white': selectedFile }"
              style="cursor: pointer;"
              @dragover.prevent="isDragging = true"
              @dragleave.prevent="isDragging = false"
              @drop.prevent="handleDrop"
              @click="$refs.fileInput.click()"
            >
              <input 
                type="file" 
                ref="fileInput" 
                @change="handleFileSelect" 
                accept=".xlsx,.xlsm"
                style="display: none"
              >
              <i class="bi bi-cloud-upload display-4"></i>
              <p class="mt-2 mb-0 text-center">Click to select or drag and drop your Excel file</p>
              <p class="" v-if="selectedFile">Selected: [[ selectedFile.name ]]</p>
            </div>

            <!-- Process Button -->
            <div class="text-center" v-if="selectedFeature && selectedFile">
              <button 
                class="btn btn-primary btn-lg" 
                @click="processFile"
                :disabled="isProcessing"
              >
                <span v-if="isProcessing">
                  <span class="spinner-border spinner-border-sm me-2"></span>
                  Processing...
                </span>
                <span v-else>Start Processing</span>
              </button>
            </div>

            <!-- Progress Bar -->
            <div class="mt-3" v-if="isProcessing">
              <div class="progress">
                <div class="progress-bar progress-bar-striped progress-bar-animated" style="width: 100%"></div>
              </div>
            </div>

            <!-- Result -->
            <div class="mt-4" v-if="result">
              <div class="alert" :class="'alert-' + result.type" role="alert">
                <h5 class="alert-heading">[[ result.title ]]</h5>
                <p>[[ result.message ]]</p>
                <hr>
                <div v-if="result.downloadUrl">
                  <a :href="result.downloadUrl" class="btn btn-success" download>
                    <i class="bi bi-download me-2"></i>Download File
                  </a>
                </div>
                <div v-if="result.note" class="small text-muted mt-2">
                  <i class="bi bi-info-circle me-1"></i>[[ result.note ]]
                </div>
              </div>
            </div>

            <!-- Output for VBA Decode/Analysis -->
            <div class="mt-4" v-if="outputData">
              <h6>Output:</h6>
              <div class="output-area">
                <pre v-if="outputData.deobfuscation"><strong>Deobfuscation:</strong>\\n[[ outputData.deobfuscation ]]</pre>
                <pre v-if="outputData.decode"><strong>Decode:</strong>\\n[[ outputData.decode ]]</pre>
                <pre v-if="outputData.reveal"><strong>Reveal:</strong>\\n[[ outputData.reveal ]]</pre>
                <pre v-if="outputData.analysis"><strong>Analysis:</strong>\\n[[ outputData.analysis ]]</pre>
              </div>
            </div>

            <!-- Reset Button -->
            <div class="text-center mt-4" v-if="result || outputData">
              <button class="btn btn-secondary" @click="resetForm">
                Process Another File
              </button>
            </div>
          </div>
        </div>
      </div>`,
    data: function () {
      return {
        selectedFeature: null,
        selectedFile: null,
        isDragging: false,
        isProcessing: false,
        result: null,
        outputData: null
      };
    },
    methods: {
      selectFeature: function (feature) {
        this.selectedFeature = feature;
        this.result = null;
        this.outputData = null;
      },
      handleFileSelect: function (event) {
        var file = event.target.files[0];
        if (file) {
          this.selectedFile = file;
        }
      },
      handleDrop: function (event) {
        this.isDragging = false;
        var file = event.dataTransfer.files[0];
        if (file && (file.name.endsWith('.xlsx') || file.name.endsWith('.xlsm'))) {
          this.selectedFile = file;
        } else {
          alert('Please select a valid Excel file (.xlsx or .xlsm)');
        }
      },
      processFile: async function () {
        var self = this;
        if (!this.selectedFeature || !this.selectedFile) {
          alert('Please select a feature and a file');
          return;
        }

        this.isProcessing = true;
        this.result = null;
        this.outputData = null;

        var formData = new FormData();
        formData.append('file', this.selectedFile);

        var endpoints = {
          'xl-reset': '/api/xl-reset',
          'xl-remove': '/api/xl-remove',
          'vba-remove': '/api/vba-remove',
          'vba-decode': '/api/vba-decode',
          'vba-analysis': '/api/vba-analysis'
        };

        try {
          var response = await fetch(endpoints[this.selectedFeature], {
            method: 'POST',
            body: formData
          });

          var data = await response.json();

          if (response.ok && data.success) {
            if (data.filename) {
              this.result = {
                type: 'success',
                title: 'Success!',
                message: data.message,
                downloadUrl: '/download/' + data.filename,
                note: data.note || null
              };
            } else if (data.data) {
              this.outputData = data.data;
              this.result = {
                type: 'info',
                title: 'Processing Complete',
                message: data.message
              };
            }
          } else {
            this.result = {
              type: 'danger',
              title: 'Error',
              message: data.error || 'Processing failed'
            };
          }
        } catch (error) {
          this.result = {
            type: 'danger',
            title: 'Error',
            message: 'An error occurred: ' + error.message
          };
        } finally {
          this.isProcessing = false;
        }
      },
      resetForm: function () {
        this.selectedFeature = null;
        this.selectedFile = null;
        this.result = null;
        this.outputData = null;
        if (this.$refs.fileInput) {
          this.$refs.fileInput.value = '';
        }
      }
    }
  };
})();
