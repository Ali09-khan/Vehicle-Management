<script setup lang="ts">
import { cva } from 'class-variance-authority'
import { useField } from 'vee-validate'
import { computed, useAttrs } from 'vue'

type BaseInputProps = {
  modelValue?: string
  as?: 'input' | 'textarea'
  name?: string
  disabled?: boolean
  readonly?: boolean
}

type BaseInputSlots = {
  label?(): void
  error?(): void
}

const props = withDefaults(defineProps<BaseInputProps>(), {
  as: 'input',
})

const slots = defineSlots<BaseInputSlots>()
const attrs = useAttrs()

const { value, errorMessage, handleBlur, handleChange } = useField(() => props.name ?? 'name', undefined, {
  controlled: Boolean(props.name),
  syncVModel: true,
})

const styles = cva([], {
  variants: {
    disabled: {
      true: 'bg-gray-100',
      false: null,
    },
    readonly: {
      true: 'bg-gray-100',
      false: null,
    },
  },
  compoundVariants: [
    {
      class: 'focus:border-primary-700 hover:border-gray-500',
      disabled: false,
      readonly: false,
    },
  ],
})

const invalidStyles = computed(() => (slots.error || errorMessage.value ? 'border-red-500' : 'border-gray-300'))
</script>

<template>
  <div class="space-y-1 text-start">
    <template v-if="slots.label">
      <label>
        <slot name="label" />
      </label>
    </template>

    <Component
      :is="as"
      :class="['w-full rounded border px-4 py-3 outline-none', styles(props), invalidStyles]"
      :disabled="disabled"
      :readonly="readonly"
      :value="value"
      v-bind="attrs"
      @blur="handleBlur"
      @change="handleChange"
      @input="handleBlur"
    />

    <template v-if="slots.error || errorMessage">
      <span class="ml-auto text-red-500">
        <slot name="error">
          {{ errorMessage }}
        </slot>
      </span>
    </template>
  </div>
</template>
