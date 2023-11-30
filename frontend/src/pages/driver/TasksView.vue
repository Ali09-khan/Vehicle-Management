<script setup lang="ts">
import { ref } from 'vue'

import TasksTable from '@/components/tables/TasksTable.vue'

import { useApi } from '@/api'

const api = useApi()

const tasks = ref(await api.driver.getMyTasks().then(({ data }) => data))
</script>

<template>
  <div class="flex flex-col gap-8">
    <div class="flex items-center gap-8">
      <h1 class="text-2xl font-bold">{{ 'Tasks List' }}</h1>
    </div>

    <h1 class="text-2xl font-bold">{{ `Tasks: ${tasks.length}` }}</h1>

    <TasksTable :tasks="tasks" />
  </div>
</template>
