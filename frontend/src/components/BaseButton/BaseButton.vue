<script setup lang="ts">
import { cva } from 'class-variance-authority'

type BaseButtonProps = {
  intent?: 'primary' | 'secondary' | 'tertiary' | 'danger'
  size?: 's' | 'm' | 'l' | 'xl'
  type?: HTMLButtonElement['type']
  disabled?: boolean
}

const props = withDefaults(defineProps<BaseButtonProps>(), {
  intent: 'primary',
  size: 'm',
  type: 'button',
})

const styles = cva([], {
  variants: {
    intent: {
      primary: 'bg-blue-500 ',
      secondary: 'bg-orange-600',
      tertiary: 'border border-gray-300 bg-white',
      danger: 'bg-red-500',
    },
    size: {
      s: 'py-1',
      m: 'py-2',
      l: 'py-3',
      xl: 'py-4',
    },
  },
  compoundVariants: [
    {
      intent: ['primary', 'secondary', 'danger'],
      class: 'text-white disabled:bg-gray-200',
    },
    {
      intent: ['tertiary'],
      class: 'disabled:border-gray-200 disabled:bg-gray-200 disabled:text-white',
    },
  ],
})
</script>

<template>
  <button
    :class="['flex items-center justify-center gap-2 rounded px-3 disabled:cursor-not-allowed', styles(props)]"
    :disabled="disabled"
    :type="type"
  >
    <slot name="icon" />
    <slot />
  </button>
</template>
