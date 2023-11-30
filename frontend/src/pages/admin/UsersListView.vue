<script setup lang="ts">
import { ref } from 'vue'

import BaseButton from '@/components/BaseButton/BaseButton.vue'
import UsersTable from '@/components/tables/UsersTable.vue'

import { useApi } from '@/api'
import type { User } from '@/api/users-rest/types'
import { RouteNames } from '@/router/types'

const api = useApi()

const users = ref<User[]>([])

async function fetchData() {
  await api.users
    .getAll()
    .then(({ data }) => data)
    .then((data) => (users.value = data))
}

await fetchData()
</script>

<template>
  <div class="flex flex-col gap-8">
    <div class="flex items-center gap-8">
      <h1 class="text-2xl font-bold">{{ 'Users List' }}</h1>

      <RouterLink :to="{ name: RouteNames.ADMIN_USERS_CREATE }">
        <BaseButton>{{ 'Create User' }}</BaseButton>
      </RouterLink>
    </div>

    <h1 class="text-2xl font-bold">{{ `Users: ${users.length}` }}</h1>

    <UsersTable :users="users" @update="fetchData()" />
  </div>
</template>
