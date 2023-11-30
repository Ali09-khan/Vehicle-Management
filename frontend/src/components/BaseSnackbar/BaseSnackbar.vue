<script lang="ts">
export type BaseSnackbarProps = {
  message: string
  kind?: 'error' | 'success'
}
</script>

<script setup lang="ts">
import { defineAsyncComponent } from 'vue'
import type { Component } from 'vue'

const props = withDefaults(defineProps<BaseSnackbarProps>(), {
  kind: 'success',
})

const CheckCircleIcon = defineAsyncComponent(() => import('@/assets/icons/check-circle.svg'))
const XCircleIcon = defineAsyncComponent(() => import('@/assets/icons/x-circle.svg'))

const icons: Record<Exclude<BaseSnackbarProps['kind'], undefined>, Component> = {
  error: XCircleIcon,
  success: CheckCircleIcon,
}
</script>

<template>
  <div class="relative flex items-center gap-2 rounded-lg bg-white px-4 py-2 shadow-xl">
    <Component :is="icons[props.kind]" />

    {{ props.message }}
  </div>
</template>
