<script setup lang="ts">
import { ref } from 'vue'

import FuelingTable from '@/components/tables/FuelingTable.vue'

import { useApi } from '@/api'

const api = useApi()

const tasks = ref(await api.fuel.getAll().then(({ data }) => data))
</script>

<template>
  <div class="flex flex-col gap-8">
    <div class="flex items-center gap-8">
      <h1 class="text-2xl font-bold">{{ 'Fueling Records' }}</h1>
    </div>

    <h1 class="text-2xl font-bold">{{ `Fueling Records: ${tasks.length}` }}</h1>

    <FuelingTable :fueling-records="tasks" />
  </div>
</template>
