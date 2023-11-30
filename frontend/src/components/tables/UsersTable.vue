<script setup lang="ts">
import BaseTable from '@/components/BaseTable/BaseTable.vue'
import TableBody from '@/components/BaseTable/TableBody.vue'
import TableCell from '@/components/BaseTable/TableCell.vue'
import TableHeader from '@/components/BaseTable/TableHeader.vue'
import TableRow from '@/components/BaseTable/TableRow.vue'

import { useSnackbar } from '@/composables'

import { useApi } from '@/api'
import type { User } from '@/api/users-rest/types'
import { RouteNames } from '@/router/types'
import { useRoleStore } from '@/stores'

import BaseButton from '../BaseButton/BaseButton.vue'

type Props = {
  users: User[]
}

const props = defineProps<Props>()

type Emits = {
  (e: 'update'): void
}

const emit = defineEmits<Emits>()

const roleStore = useRoleStore()

const api = useApi()

async function handleRemove(user: User) {
  if (user.is_superuser) return alert('Removing an administrator is prohibited')
  if (!confirm('Are you sure you want to delete the user?')) return

  await api.users.remove({ id: user.id })

  emit('update')

  useSnackbar().show({
    message: 'User deleted successfully',
  })
}
</script>

<template>
  <BaseTable>
    <TableHeader>
      <TableRow>
        <TableCell>{{ 'ID' }}</TableCell>
        <TableCell>{{ 'Email' }}</TableCell>
        <TableCell>{{ 'Role' }}</TableCell>
        <TableCell>{{ 'Is Admin' }}</TableCell>
        <TableCell>{{ '' }}</TableCell>
        <TableCell>{{ '' }}</TableCell>
      </TableRow>
    </TableHeader>

    <TableBody>
      <TableRow v-for="user in props.users" :key="user.id">
        <TableCell>{{ user.id }}</TableCell>
        <TableCell>{{ user.email }}</TableCell>
        <TableCell>{{ roleStore.findById(user.role_id)?.name ?? 'None' }}</TableCell>
        <TableCell>{{ user.is_superuser }}</TableCell>
        <TableCell>
          <RouterLink
            :disabled="user.is_superuser"
            :to="{ name: RouteNames.ADMIN_USERS_EDIT, params: { id: user.id } }"
          >
            <BaseButton :disabled="user.is_superuser">{{ 'Edit' }}</BaseButton>
          </RouterLink>
        </TableCell>
        <TableCell>
          <BaseButton :disabled="user.is_superuser" @click="() => handleRemove(user)">{{ 'Remove' }}</BaseButton>
        </TableCell>
      </TableRow>
    </TableBody>
  </BaseTable>
</template>
