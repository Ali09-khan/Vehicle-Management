<script setup lang="ts">
import BaseTable from '@/components/BaseTable/BaseTable.vue'
import TableBody from '@/components/BaseTable/TableBody.vue'
import TableCell from '@/components/BaseTable/TableCell.vue'
import TableHeader from '@/components/BaseTable/TableHeader.vue'
import TableRow from '@/components/BaseTable/TableRow.vue'

import type { MaintenanceView } from '@/api/maintenance-person/types'

type Props = {
  maintenanceRecords: MaintenanceView[]
}

const props = defineProps<Props>()
</script>

<template>
  <BaseTable>
    <TableHeader>
      <TableRow>
        <TableCell>{{ 'ID' }}</TableCell>
        <TableCell>{{ 'vehicle id' }}</TableCell>
        <TableCell>{{ 'mainteneance personnel id' }}</TableCell>
        <TableCell>{{ 'maintenance description' }}</TableCell>
        <TableCell>{{ 'date and time' }}</TableCell>
        <TableCell>{{ 'part numbers' }}</TableCell>
        <TableCell>{{ 'status' }}</TableCell>
        <TableCell>{{ 'price' }}</TableCell>
        <TableCell>{{ 'milage' }}</TableCell>
      </TableRow>
    </TableHeader>

    <TableBody>
      <TableRow v-for="user in props.maintenanceRecords" :key="user.id">
        <TableCell>{{ user.id }}</TableCell>
        <TableCell>{{ user.vehicle_id }}</TableCell>
        <TableCell>{{ user.mainteneance_personnel_id }}</TableCell>
        <TableCell>{{ user.maintenance_description }}</TableCell>
        <TableCell>{{ user.date_and_time }}</TableCell>
        <TableCell>{{ user.part_numbers }}</TableCell>
        <TableCell>{{ user.status }}</TableCell>
        <TableCell>{{ user.price }}</TableCell>
        <TableCell>{{ user.milage }}</TableCell>
      </TableRow>
    </TableBody>
  </BaseTable>
</template>
