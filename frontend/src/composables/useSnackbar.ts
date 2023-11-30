import { ref } from 'vue'

import type { BaseSnackbarProps } from '@/components/BaseSnackbar/BaseSnackbar.vue'

import { useSnackbarStore } from '@/stores/SnackbarStore'

const id = ref(0)

export function useSnackbar() {
  const snackbarStore = useSnackbarStore()

  return {
    show(options: BaseSnackbarProps) {
      snackbarStore.show(id.value++, options)
    },
  }
}
