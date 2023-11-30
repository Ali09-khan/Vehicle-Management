<script setup lang="ts">
import BaseTable from '@/components/BaseTable/BaseTable.vue'
import TableBody from '@/components/BaseTable/TableBody.vue'
import TableCell from '@/components/BaseTable/TableCell.vue'
import TableHeader from '@/components/BaseTable/TableHeader.vue'
import TableRow from '@/components/BaseTable/TableRow.vue'

import type { FuelingView } from '@/api/fueling-person/types'

type Props = {
  fuelingRecords: FuelingView[]
}

const props = defineProps<Props>()
</script>

<template>
  <BaseTable>
    <TableHeader>
      <TableRow>
        <TableCell>{{ 'ID' }}</TableCell>
        <TableCell>{{ 'vehicle id' }}</TableCell>
        <TableCell>{{ 'car plate info' }}</TableCell>
        <TableCell>{{ 'date and time' }}</TableCell>
        <TableCell>{{ 'amount of fuel' }}</TableCell>
        <TableCell>{{ 'fuel type' }}</TableCell>
        <TableCell>{{ 'cost' }}</TableCell>
        <TableCell>{{ 'gas station name' }}</TableCell>
        <TableCell>{{ 'fueling personnel id' }}</TableCell>
        <TableCell>{{ 'fuel levels before' }}</TableCell>
        <TableCell>{{ 'fuel levels after' }}</TableCell>
        <TableCell>{{ 'milage' }}</TableCell>
      </TableRow>
    </TableHeader>

    <TableBody>
      <TableRow v-for="record in props.fuelingRecords" :key="record.id">
        <TableCell>{{ record.id }}</TableCell>
        <TableCell>{{ record.vehicle_id }}</TableCell>
        <TableCell>{{ record.car_plate_info }}</TableCell>
        <TableCell>{{ new Date(record.date_and_time ?? '').toLocaleString() }}</TableCell>
        <TableCell>{{ record.amount_of_fuel }}</TableCell>
        <TableCell>{{ record.fuel_type }}</TableCell>
        <TableCell>{{ record.cost }}</TableCell>
        <TableCell>{{ record.gas_station_name }}</TableCell>
        <TableCell>{{ record.fueling_personnel_id }}</TableCell>
        <TableCell>{{ record.fuel_levels_before }}</TableCell>
        <TableCell>{{ record.fuel_levels_after }}</TableCell>
        <TableCell>{{ record.milage }}</TableCell>
      </TableRow>
    </TableBody>
  </BaseTable>
</template>
