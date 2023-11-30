<script setup lang="ts">
import { onBeforeMount, ref } from 'vue'

import SnackbarContainer from '@/components/containers/SnackbarContainer.vue'

import { useRoleStore } from '@/stores'

const initialized = ref(false)

const roleStore = useRoleStore()

onBeforeMount(async () => {
  await roleStore.initialize()

  initialized.value = true
})
</script>

<template>
  <template v-if="initialized">
    <RouterView />
    <SnackbarContainer />
  </template>
</template>
