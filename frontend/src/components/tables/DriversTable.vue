<script setup lang="ts">
import BaseTable from '@/components/BaseTable/BaseTable.vue'
import TableBody from '@/components/BaseTable/TableBody.vue'
import TableCell from '@/components/BaseTable/TableCell.vue'
import TableHeader from '@/components/BaseTable/TableHeader.vue'
import TableRow from '@/components/BaseTable/TableRow.vue'

import type { Driver } from '@/api/driver-rest/types'

type Props = {
  drivers: Driver[]
}

const props = defineProps<Props>()
</script>

<template>
  <BaseTable>
    <TableHeader>
      <TableRow>
        <TableCell>{{ 'ID' }}</TableCell>
        <TableCell>{{ 'First Name' }}</TableCell>
        <TableCell>{{ 'Last Name' }}</TableCell>
        <TableCell>{{ 'Middle Name' }}</TableCell>
        <TableCell>{{ 'Registration Date' }}</TableCell>
        <TableCell>{{ 'Driving License' }}</TableCell>
        <TableCell>{{ 'User ID' }}</TableCell>
      </TableRow>
    </TableHeader>

    <TableBody>
      <TableRow v-for="user in props.drivers" :key="user.id">
        <TableCell>{{ user.id }}</TableCell>
        <TableCell>{{ user.fname }}</TableCell>
        <TableCell>{{ user.lname }}</TableCell>
        <TableCell>{{ user.mname }}</TableCell>
        <TableCell>{{ user.registration_date }}</TableCell>
        <TableCell>{{ user.driving_license }}</TableCell>
        <TableCell>{{ user.user_id }}</TableCell>
      </TableRow>
    </TableBody>
  </BaseTable>
</template>
