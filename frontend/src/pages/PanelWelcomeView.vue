<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useRouter } from 'vue-router'

import BaseButton from '@/components/BaseButton/BaseButton.vue'

import { RouteNames } from '@/router/types'
import { useAuthStore } from '@/stores'

const authStore = useAuthStore()
const { user, role } = storeToRefs(authStore)
const { logOut } = authStore

const router = useRouter()

const handleClick = (routeName: RouteNames) => router.push({ name: routeName })
</script>

<template>
  <div class="flex h-full w-full items-center justify-center bg-gray-200 p-10">
    <div class="flex w-full max-w-[30rem] flex-col gap-6 rounded-lg bg-white px-8 py-6 text-center shadow">
      <h1 class="text-xl font-semibold">{{ `Hello ${user.email}!` }}</h1>

      <BaseButton :disabled="!role.isAdmin" intent="tertiary" @click="handleClick(RouteNames.ADMIN_WELCOME)">
        {{ 'Admin panel' }}
      </BaseButton>

      <BaseButton
        :disabled="!role.isMaintenance"
        intent="tertiary"
        @click="handleClick(RouteNames.MAINTENANCE_WELCOME)"
      >
        {{ 'Maintenance panel' }}
      </BaseButton>

      <BaseButton :disabled="!role.isFueling" intent="tertiary" @click="handleClick(RouteNames.FUELING_WELCOME)">
        {{ 'Fueling panel' }}
      </BaseButton>

      <BaseButton :disabled="!role.isDriver" intent="tertiary" @click="handleClick(RouteNames.DRIVER_WELCOME)">
        {{ 'Driver panel' }}
      </BaseButton>

      <hr />

      <BaseButton intent="danger" @click="logOut">{{ 'LogOut' }}</BaseButton>
    </div>
  </div>
</template>
