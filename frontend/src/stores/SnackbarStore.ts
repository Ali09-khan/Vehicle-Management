import { defineStore } from 'pinia'
import { ref } from 'vue'

import type { BaseSnackbarProps } from '@/components/BaseSnackbar/BaseSnackbar.vue'

export const useSnackbarStore = defineStore('SnackbarStore', () => {
  const snackbars = ref<Map<number, any>>(new Map())

  function hide(id: number) {
    snackbars.value.delete(id)
  }

  function show(id: number, options: BaseSnackbarProps) {
    snackbars.value.set(id, options)

    setTimeout(() => {
      hide(id)
    }, 5_000)
  }

  return {
    snackbars,

    show,
    hide,
  }
})
