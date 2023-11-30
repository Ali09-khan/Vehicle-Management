<script setup lang="ts">
import BaseLayout from '@/components/BaseLayout/BaseLayout.vue'
import LayoutNavigationItem from '@/components/BaseLayout/LayoutNavigationItem.vue'
import LayoutSideBar from '@/components/BaseLayout/LayoutSideBar.vue'

import { RouteNames } from '@/router/types'

const links = [
  {
    name: RouteNames.ADMIN_WELCOME,
    title: 'Welcome',
  },
  {
    name: RouteNames.ADMIN_USERS_LIST,
    title: 'Users',
  },
  {
    name: RouteNames.ADMIN_DRIVERS_LIST,
    title: 'Drivers',
  },
  {
    name: RouteNames.ADMIN_VEHICLES_LIST,
    title: 'Vehicles',
  },
  {
    name: RouteNames.ADMIN_TASK_CREATE,
    title: 'Create Tasks',
  },  
  {
    name: RouteNames.PANEL_WELCOME,
    title: 'Menu',
  },
]
</script>

<template>
  <BaseLayout>
    <template #sidebar>
      <LayoutSideBar>
        <template #title>
          {{ 'Admin Panel' }}
        </template>

        <LayoutNavigationItem v-for="link in links" :key="link.name" :to="{ name: link.name }">
          {{ link.title }}
        </LayoutNavigationItem>
      </LayoutSideBar>
    </template>

    <RouterView v-slot="{ Component }">
      <Suspense :timeout="0">
        <template #fallback>
          {{ 'Загрузка...' }}
        </template>

        <Component :is="Component" />
      </Suspense>
    </RouterView>
  </BaseLayout>
</template>
