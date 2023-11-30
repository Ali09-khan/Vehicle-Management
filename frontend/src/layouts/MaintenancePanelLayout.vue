<script setup lang="ts">
import BaseLayout from '@/components/BaseLayout/BaseLayout.vue'
import LayoutNavigationItem from '@/components/BaseLayout/LayoutNavigationItem.vue'
import LayoutSideBar from '@/components/BaseLayout/LayoutSideBar.vue'

import { RouteNames } from '@/router/types'

const links = [
  {
    name: RouteNames.MAINTENANCE_WELCOME,
    title: 'Welcome',
  },
  {
    name: RouteNames.MAINTENANCE_APPOINTENTS_LIST,
    title: 'Maintenance Records',
  },
  {
    name: RouteNames.MAINTENANCE_REGISTER_VIEW,
    title: 'Register Maintenance Record',
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
          {{ 'Maintenance Panel' }}
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
