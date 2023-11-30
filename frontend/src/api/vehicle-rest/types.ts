import type { WithId } from '../types'

export type Vehicle = {
  sitting_capacity: number
  model: string
  license_plate: string
  driver_id: number
} & WithId
