import type { WithId } from '../types'

export type User = {
  email: string
  is_active: boolean
  is_superuser: boolean
  is_verified: boolean
  role_id: number
} & WithId

export type UserUpdate = User & { password: string }
