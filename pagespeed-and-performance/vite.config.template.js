// ==============================================================================
// HIGH-PERFORMANCE VITE BUNDLER & CODE-SPLITTING CONFIGURATION
// Target: 100/100 Google PageSpeed & Core Web Vitals (Zero TBT & CLS)
// ==============================================================================

import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [
    react()
  ],
  build: {
    // Target modern evergreen browsers for smaller bundle output
    target: 'es2022',
    // Split vendor dependencies into parallel, independently cacheable chunks
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes('node_modules')) {
            // Core UI runtime
            if (id.includes('react') || id.includes('react-dom')) {
              return 'vendor-react';
            }
            // Icon libraries (e.g. lucide-react, heroicons)
            if (id.includes('lucide-react') || id.includes('icons')) {
              return 'vendor-icons';
            }
            // Heavy utilities or standalone packages
            if (id.includes('qrcode')) {
              return 'vendor-qrcode';
            }
            // General third-party libraries
            return 'vendor-libs';
          }
        }
      }
    },
    // Warn only if an individual chunk exceeds 600 kB
    chunkSizeWarningLimit: 600
  }
});
