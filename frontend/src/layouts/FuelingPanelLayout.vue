<script setup lang="ts">
import BaseLayout from '@/components/BaseLayout/BaseLayout.vue'
import LayoutNavigationItem from '@/components/BaseLayout/LayoutNavigationItem.vue'
import LayoutSideBar from '@/components/BaseLayout/LayoutSideBar.vue'

import { RouteNames } from '@/router/types'

const links = [
  {
    name: RouteNames.FUELING_WELCOME,
    title: 'Welcome',
  },
  {
    name: RouteNames.FUELING_FUEL_LIST,
    title: 'Fuel',
  },
  {
    name: RouteNames.FUELING_REGISTER_VIEW,
    title: 'Register Fueling Record',
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
          {{ 'Fueling Panel' }}
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
