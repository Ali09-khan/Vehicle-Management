import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import svgLoader from 'vite-svg-loader'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    strictPort: true,
    port: 1010,
    host: true,
  },
  define: {
    __BUILD_DATE: JSON.stringify(new Date().toLocaleString('ru-RU', { timeZone: 'Asia/Almaty' })),
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  plugins: [vue(), svgLoader({ svgo: false })],
})
