<script setup lang="ts">
import { ref } from 'vue'

import BaseButton from '@/components/BaseButton/BaseButton.vue'
import DriversTable from '@/components/tables/DriversTable.vue'

import { useApi } from '@/api'
import { RouteNames } from '@/router/types'

const api = useApi()

const drivers = ref(await api.driver.getAll().then(({ data }) => data))
</script>

<template>
  <div class="flex flex-col gap-8">
    <div class="flex items-center gap-8">
      <h1 class="text-2xl font-bold">{{ 'Drivers List' }}</h1>

      <RouterLink :to="{ name: RouteNames.ADMIN_DRIVERS_CREATE }">
        <BaseButton>{{ 'Create Driver' }}</BaseButton>
      </RouterLink>
    </div>

    <h1 class="text-2xl font-bold">{{ `Drivers: ${drivers.length}` }}</h1>

    <DriversTable :drivers="drivers" />
  </div>
</template>
