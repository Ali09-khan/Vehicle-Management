import type { WithId } from '../types'

export type TaskView = {
  id: number
  start_location: string
  end_location: string
  start_time: string
  end_time: string
  driver_id: number
  status: string
  time_spent: string
  distance: number
} & WithId 