<script setup lang="ts">
import BaseTable from '@/components/BaseTable/BaseTable.vue'
import TableBody from '@/components/BaseTable/TableBody.vue'
import TableCell from '@/components/BaseTable/TableCell.vue'
import TableHeader from '@/components/BaseTable/TableHeader.vue'
import TableRow from '@/components/BaseTable/TableRow.vue'

import type { Vehicle } from '@/api/vehicle-rest/types'

type Props = {
  vehicles: Vehicle[]
}

const props = defineProps<Props>()
</script>

<template>
  <BaseTable>
    <TableHeader>
      <TableRow>
        <TableCell>{{ 'ID' }}</TableCell>
        <TableCell>{{ 'Sitting capacity' }}</TableCell>
        <TableCell>{{ 'Model' }}</TableCell>
        <TableCell>{{ 'License plate' }}</TableCell>
        <TableCell>{{ 'Driver ID' }}</TableCell>
      </TableRow>
    </TableHeader>

    <TableBody>
      <TableRow v-for="vehicle in props.vehicles" :key="vehicle.id">
        <TableCell>{{ vehicle.id }}</TableCell>
        <TableCell>{{ vehicle.sitting_capacity }}</TableCell>
        <TableCell>{{ vehicle.model }}</TableCell>
        <TableCell>{{ vehicle.license_plate }}</TableCell>
        <TableCell>{{ vehicle.driver_id }}</TableCell>
      </TableRow>
    </TableBody>
  </BaseTable>
</template>
