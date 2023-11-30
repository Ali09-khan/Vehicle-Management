<script setup lang="ts">
import { useSnackbarStore } from '@/stores'

import BaseSnackbar from '../BaseSnackbar/BaseSnackbar.vue'

const snackbarStore = useSnackbarStore()
</script>

<template>
  <Teleport to="#snackbars-container">
    <div class="fixed bottom-6 right-6 flex flex-col gap-2">
      <TransitionGroup name="list">
        <BaseSnackbar
          v-for="[id, snackbarProps] in snackbarStore.snackbars.entries()"
          v-bind="snackbarProps"
          :key="id"
        />
      </TransitionGroup>
    </div>
  </Teleport>
</template>

<style scoped>
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
</style>
