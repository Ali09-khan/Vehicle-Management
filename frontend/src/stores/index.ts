import { createPinia } from 'pinia'

const store = createPinia()

export * from './SnackbarStore'
export * from './AuthStore'
export * from './RoleStore'

export { store }
