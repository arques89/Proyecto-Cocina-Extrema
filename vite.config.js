import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    // ... otras opciones de compilación
    rollupOptions: {
      external: ['mock-aws-s3', 'aws-sdk', 'nock'], // Lista los módulos externos
    },
  },
});