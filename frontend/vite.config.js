import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// // https://vite.dev/config/
// export default defineConfig({
//   plugins: [react()],
// })


export default defineConfig({
  plugins: [react()],
  server: {
    host: true, // 0.0.0.0 바인딩
    port: 5173, // 원하는 포트
    allowedHosts: ['spaceweb.dovis.dev','api-spaceweb.dovis.dev','dovis.dev'], // 허용할 도메인 추가
  },
})