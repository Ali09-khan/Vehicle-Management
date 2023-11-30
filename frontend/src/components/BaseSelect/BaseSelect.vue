<script setup lang="ts" generic="T extends { [K in keyof T]: T[K] }">
import { onClickOutside, useToggle } from '@vueuse/core'
import { useFuse } from '@vueuse/integrations/useFuse'
import { cva } from 'class-variance-authority'
import _ from 'lodash-es'
import { useField } from 'vee-validate'
import { onMounted, ref, watch } from 'vue'
import type { Ref } from 'vue'

import ChevronDown from '@/assets/icons/chevron-down.svg'
import ChevronUp from '@/assets/icons/chevron-up.svg'

import BaseInput from '../BaseInput/BaseInput.vue'

type SelectProps = {
  name?: string
  options: T[]
  label?: string
  error?: string
  hint?: string
  labelField?: keyof T
  modelValue?: unknown
  placeholder?: string
  applyPlaceholder?: string
  loadingPlaceholder?: string
  searchPlaceholder?: string
  valueField?: keyof T
  disabled?: boolean
  loading?: boolean
  multiple?: boolean
  readonly?: boolean
  withSearch?: boolean
  withApply?: boolean
  size?: 'large' | 'medium' | 'small'
}

type SelectSlots = {
  option?(props: { index: number; option: T }): void
  selectedOption?(props: { option: T }): void
  label?(): void
  error?(): void
  hint?(): void
}

type SelectEmits = {
  (event: 'update:modelValue', value: T | T[]): void
  (event: 'apply', value: T): void
}

const props = withDefaults(defineProps<SelectProps>(), {
  applyPlaceholder: 'Применить для всех',
  loadingPlaceholder: 'Загрузка...',
  searchPlaceholder: 'Поиск...',
  placeholder: 'Выберите из списка',
  withSearch: true,
  size: 'medium',
})

const slots = defineSlots<SelectSlots>()
const emits = defineEmits<SelectEmits>()

const searchQuery = ref<string>('')
const selected = ref<T[]>([]) as Ref<T[]>
const dropdownRef = ref<HTMLDivElement>()

const { results } = useFuse<T>(
  searchQuery,
  () => props.options,
  () => {
    return {
      fuseOptions: {
        keys: Object.keys(props.options?.[0] || []),
      },
      matchAllWhenSearchEmpty: true,
    }
  },
)

const styles = cva([], {
  variants: {
    size: {
      small: 'px-4 py-2',
      medium: 'px-5 py-3',
      large: 'px-6 py-4',
    },
    disabled: {
      true: 'cursor-not-allowed bg-gray-200',
      false: null,
    },
    readonly: {
      true: 'text-ellipsis rounded-none border-transparent border-b-gray-300 bg-transparent !px-0',
      false: null,
    },
  },
  compoundVariants: [
    {
      disabled: false,
      readonly: false,
      class: 'cursor-pointer bg-white hover:border-black',
    },
  ],
})

const [isDropdownOpen, toggleDropdown] = useToggle()

const {
  /* prettier-ignore */
  value,
  setValue,
  errorMessage,
} = useField<T | T[]>(props.name ?? 'name', undefined, {
  controlled: Boolean(props.name),
  syncVModel: true,
})

function getOptionLabel(option: T) {
  const labelField = props.labelField as keyof T
  const valueField = props.valueField as keyof T

  if (
    /* prettier-ignore */
    (
      labelField &&
      valueField
    ) &&
    typeof option !== 'object'
  ) {
    return _.get(
      props.options.find((item) => _.get(item, valueField) === option),
      labelField,
    )
  }

  if (
    /* prettier-ignore */
    (
      labelField ||
      valueField
    ) &&
    typeof option === 'object'
  ) {
    return _.get(option, labelField || valueField)
  }

  return option
}

function handleClick() {
  if (props.disabled || props.readonly) {
    return
  }

  toggleDropdown()
}

function handleSelect(option: T) {
  if (props.multiple) return

  const value = props.valueField ? _.get(option, props.valueField) : option

  setValue(value)
  toggleDropdown()
}

function handleApply() {
  emits('apply', value.value as T)
}

watch(selected, () => {
  setValue(selected.value)
})

onClickOutside(dropdownRef, () => {
  toggleDropdown()
})

onMounted(() => {
  if (props.multiple && value.value) selected.value = Object.values(value.value)
})
</script>

<template>
  <div class="flex w-full flex-col gap-2">
    <template v-if="label || slots.label">
      <div class="text-sm text-gray-500">
        <slot name="label">
          {{ label }}
        </slot>
      </div>
    </template>

    <div class="relative">
      <div
        :class="['overflow-hidden whitespace-nowrap rounded border border-gray-300 pr-8', styles(props)]"
        @click="handleClick()"
      >
        <template v-if="value && !loading">
          <slot name="selectedOption" v-bind="{ option: value as T }">
            <template v-if="multiple">
              {{ 'Выбрано: ' + selected.length }}
            </template>
            <template v-else>
              {{ getOptionLabel(value as T) }}
            </template>
          </slot>
        </template>
        <template v-else>
          <div class="select-none text-gray-300">
            {{ loading ? loadingPlaceholder : placeholder }}
          </div>
        </template>

        <template v-if="!readonly">
          <div
            :class="['absolute bottom-0 right-0 top-0 flex items-center justify-center !bg-transparent', styles(props)]"
          >
            <ChevronUp v-if="isDropdownOpen" class="stroke-gray-400" />
            <ChevronDown v-else class="stroke-gray-400" />
          </div>
        </template>
      </div>

      <template v-if="isDropdownOpen">
        <div
          ref="dropdownRef"
          class="absolute left-0 z-[9999] mt-1 max-h-80 w-fit min-w-full overflow-auto rounded border border-gray-300 bg-white"
        >
          <template v-if="withSearch">
            <div class="p-2">
              <BaseInput
                :placeholder="searchPlaceholder"
                size="small"
                @input="(event: Event) => (searchQuery = (event.target as HTMLInputElement).value)"
              />
            </div>
          </template>

          <template v-if="results.length > 0">
            <template v-for="({ item: option }, index) in results" :key="index">
              <label
                :class="['flex items-center gap-2 hover:bg-gray-200', styles(props)]"
                @click="handleSelect(option)"
              >
                <template v-if="multiple">
                  <!-- prettier-ignore -->
                  <input
                    v-model="selected"
                    type="checkbox"
                    :value="option"
                  />
                </template>

                <slot name="option" v-bind="{ option, index }">
                  {{ getOptionLabel(option) }}
                </slot>
              </label>
            </template>
          </template>
          <template v-else>
            <div :class="['text-center text-sm text-gray-500', styles(props)]">
              {{ 'Пусто' }}
            </div>
          </template>
        </div>
      </template>
    </div>

    <template v-if="value && withApply">
      <a class="-mt-1" href="#" @click="handleApply()">
        {{ applyPlaceholder }}
      </a>
    </template>

    <template v-if="error || slots.error || errorMessage">
      <div class="text-danger-500 text-sm">
        <slot name="error">
          {{ error || errorMessage }}
        </slot>
      </div>
    </template>
    <template v-else-if="hint || slots.hint">
      <div class="text-sm text-gray-500">
        <slot name="hint">
          {{ hint }}
        </slot>
      </div>
    </template>
  </div>
</template>
