<script setup lang="ts">
import { ref } from 'vue'

import BaseButton from '@/components/BaseButton/BaseButton.vue'
import VehiclesTable from '@/components/tables/VehiclesTable.vue'

import { useApi } from '@/api'
import { RouteNames } from '@/router/types'

const api = useApi()

const vehicles = ref(await api.vehicle.getAll().then(({ data }) => data))
</script>

<template>
  <div class="flex flex-col gap-8">
    <div class="flex items-center gap-8">
      <h1 class="text-2xl font-bold">{{ 'Vehicles List' }}</h1>

      <RouterLink :to="{ name: RouteNames.ADMIN_VEHICLES_CREATE }">
        <BaseButton>{{ 'Create Vehicle' }}</BaseButton>
      </RouterLink>
    </div>

    <h1 class="text-2xl font-bold">{{ `Vehicles: ${vehicles.length}` }}</h1>

    <VehiclesTable :vehicles="vehicles" />
  </div>
</template>
