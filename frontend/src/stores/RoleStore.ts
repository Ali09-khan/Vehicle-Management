import { defineStore } from 'pinia'
import { ref } from 'vue'

import { useApi } from '@/api'
import type { Role } from '@/api/role-rest/types'

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

export const useRoleStore = defineStore('RoleStore', () => {
  const api = useApi()

  const roles = ref<Role[]>([])

  async function initialize() {
    await api.role
      .getAll()
      .then(({ data }) => (roles.value = data))
      .catch(console.error)
  }

  function find(role: 'customer' | 'driver' | 'maintenance_person' | 'fueling_person') {
    return roles.value.find(({ name }) => name.toLowerCase() == role.toLowerCase())
  }

  function findById(id: number) {
    return roles.value.find((role) => role.id == id)
  }

  return {
    roles,
    find,
    findById,
    initialize,
  }
})
