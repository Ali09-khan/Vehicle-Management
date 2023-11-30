import type { WithId } from '../types'

export type MaintenanceView = {
  vehicle_id: number
  mainteneance_personnel_id: number
  maintenance_description: string
  date_and_time: null | string
  part_numbers: number
  status: string
  price: number
  milage: number
} & WithId 