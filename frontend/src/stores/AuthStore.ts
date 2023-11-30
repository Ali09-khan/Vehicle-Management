import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'

import { useApi } from '@/api'
import type { User } from '@/api/users-rest/types'
import { RouteNames } from '@/router/types'

import { useRoleStore } from './'

// {
//     "name": "customer",
//     "id": 1
//   },
//   {
//     "name": "driver",
//     "id": 2
//   },
//   {
//     "name": "maintenance_person",
//     "id": 3
//   },
//   {
//     "name": "fueling_person",
//     "id": 4
//   }

export const useAuthStore = defineStore('AuthStore', () => {
  const router = useRouter()
  const api = useApi()
  const roleStore = useRoleStore()

  const user = ref<User>({
    email: '',
    id: 0,
    is_active: false,
    is_superuser: false,
    is_verified: false,
    role_id: 0,
  })

  const initialized = ref(false)
  const authenticated = computed(() => Boolean(user.value.id))

  // Дикая дичь но что поделать.
  const isAdmin = computed(() => user.value.is_superuser)
  const isCustomer = computed(() => user.value.role_id == roleStore.find('customer')?.id)
  const isDriver = computed(() => user.value.role_id == roleStore.find('driver')?.id)
  const isMaintenance = computed(() => user.value.role_id == roleStore.find('maintenance_person')?.id)
  const isFueling = computed(() => user.value.role_id == roleStore.find('fueling_person')?.id)

  const role = ref({
    isAdmin,
    isCustomer,
    isDriver,
    isMaintenance,
    isFueling,
  })

  async function initialize() {
    try {
      const response = await api.users.me()

      updateUser(response.data)
    } catch (error) {
      console.error(error)
    } finally {
      initialized.value = true
    }
  }

  function updateUser(data?: User) {
    if (!data) {
      user.value.email = ''
      user.value.id = 0
      user.value.is_active = false
      user.value.is_superuser = false
      user.value.is_verified = false
      user.value.role_id = 0

      return
    }

    user.value.email = data.email
    user.value.id = data.id
    user.value.is_active = data.is_active
    user.value.is_superuser = data.is_superuser
    user.value.is_verified = data.is_verified
    user.value.role_id = data.role_id
  }

  async function logOut() {
    await api.auth.logOut().catch(console.error)
    updateUser()
    router.push({ name: RouteNames.SIGN_IN })
  }

  return {
    user,

    initialized,
    authenticated,

    role,

    initialize,
    logOut,
  }
})
