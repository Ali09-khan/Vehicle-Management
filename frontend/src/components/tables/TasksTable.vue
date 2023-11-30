<script setup lang="ts">
import BaseTable from '@/components/BaseTable/BaseTable.vue'
import TableBody from '@/components/BaseTable/TableBody.vue'
import TableCell from '@/components/BaseTable/TableCell.vue'
import TableHeader from '@/components/BaseTable/TableHeader.vue'
import TableRow from '@/components/BaseTable/TableRow.vue'

import type { DriverTask } from '@/api/driver-rest/types'

type Props = {
  tasks: DriverTask[]
}

const props = defineProps<Props>()
</script>

<template>
  <BaseTable>
    <TableHeader>
      <TableRow>
        <TableCell>{{ 'ID' }}</TableCell>
        <TableCell>{{ 'Start Time' }}</TableCell>
        <TableCell>{{ 'Driver ID' }}</TableCell>
        <TableCell>{{ 'Distance' }}</TableCell>
        <TableCell>{{ 'End Time' }}</TableCell>
        <TableCell>{{ 'Start Location' }}</TableCell>
        <TableCell>{{ 'End Location' }}</TableCell>
        <TableCell>{{ 'Time Spent' }}</TableCell>
        <TableCell>{{ 'Status' }}</TableCell>
      </TableRow>
    </TableHeader>

    <TableBody>
      <TableRow v-for="task in props.tasks" :key="task.id">
        <TableCell>{{ task.id }}</TableCell>
        <TableCell>{{ task.start_time }}</TableCell>
        <TableCell>{{ task.driver_id }}</TableCell>
        <TableCell>{{ task.distance }}</TableCell>
        <TableCell>{{ task.end_time }}</TableCell>
        <TableCell>{{ task.start_location }}</TableCell>
        <TableCell>{{ task.end_location }}</TableCell>
        <TableCell>{{ task.time_spent }}</TableCell>
        <TableCell>{{ task.status }}</TableCell>
      </TableRow>
    </TableBody>
  </BaseTable>
</template>
