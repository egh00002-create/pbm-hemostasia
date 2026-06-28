/// <reference types="vitest/config" />
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';
import { VitePWA } from 'vite-plugin-pwa';

// Base relativa para servir igual en GitHub Pages (subruta) y en Netlify (raíz).
export default defineConfig({
  base: './',
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.svg', 'icons/icon-192.png', 'icons/icon-512.png'],
      manifest: {
        name: 'PBM — Hemostasia y Medicina Transfusional Perioperatoria',
        short_name: 'PBM',
        description:
          'Lector de la serie, calculadoras clínicas y evaluación (200 preguntas). Apoyo docente, no dispositivo médico.',
        lang: 'es',
        dir: 'ltr',
        theme_color: '#8E2433',
        background_color: '#FAF6F7',
        display: 'standalone',
        orientation: 'portrait',
        start_url: './',
        scope: './',
        icons: [
          { src: 'icons/icon-192.png', sizes: '192x192', type: 'image/png' },
          { src: 'icons/icon-512.png', sizes: '512x512', type: 'image/png' },
          {
            src: 'icons/icon-512.png',
            sizes: '512x512',
            type: 'image/png',
            purpose: 'maskable',
          },
        ],
      },
      workbox: {
        // App shell + datos: todo precacheado para funcionar 100% offline.
        globPatterns: ['**/*.{js,css,html,svg,png,ico,woff2}', 'app-data/*.{json,md}'],
        maximumFileSizeToCacheInBytes: 6 * 1024 * 1024,
        navigateFallback: 'index.html',
        runtimeCaching: [
          {
            urlPattern: ({ url }) => url.pathname.includes('/app-data/'),
            handler: 'StaleWhileRevalidate',
            options: { cacheName: 'pbm-data' },
          },
        ],
      },
      devOptions: { enabled: false },
    }),
  ],
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: ['./src/test/setup.ts'],
    css: false,
  },
});
