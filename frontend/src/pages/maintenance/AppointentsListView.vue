<script setup lang="ts">
import { ref } from 'vue'

import MaintenanceRecordTable from '@/components/tables/MaintenanceRecordTable.vue'

import { useApi } from '@/api'

const api = useApi()

const maintenanceRecords = ref(await api.maintenance.getAll().then(({ data }) => data))
</script>

<template>
  <div class="flex flex-col gap-8">
    <div class="flex items-center gap-8">
      <h1 class="text-2xl font-bold">{{ 'Maintenance Records' }}</h1>
    </div>

    <h1 class="text-2xl font-bold">{{ `Maintenance Records: ${maintenanceRecords.length}` }}</h1>

    <MaintenanceRecordTable :maintenance-records="maintenanceRecords" />
  </div>
</template>
