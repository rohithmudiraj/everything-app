import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
   server: {
    host: '0.0.0.0', // Makes Vite listen on all network interfaces
    allowedHosts: ['frontend', 'localhost', '0.0.0.0'] // Add your allowed hosts here
  }
})
