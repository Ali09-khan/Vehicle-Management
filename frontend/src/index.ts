import '@fontsource-variable/montserrat'
import { createApp } from 'vue'

import AppEntry from '@/AppEntry.vue'
import { router } from '@/router'
import { store } from '@/stores'
import '@/styles/main.scss'

const app = createApp(AppEntry)

app.use(store)
app.use(router)

app.mount('#app')

console.info('Build Date:', __BUILD_DATE)
