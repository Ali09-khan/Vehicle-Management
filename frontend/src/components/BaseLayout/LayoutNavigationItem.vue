<script setup lang="ts">
import type { RouterLinkProps } from 'vue-router'

const props = defineProps<RouterLinkProps>()
</script>

<template>
  <RouterLink
    v-bind="props"
    class="flex items-center gap-2 p-4 hover:bg-blue-500/5"
    exact-active-class="border-r-4 border-blue-500 bg-blue-700/5 text-blue-500 [&>svg]:stroke-primary-500"
  >
    <slot />
  </RouterLink>
</template>
