import type { WithId } from '../types'

export type Driver = {
  mname: string
  phone_num: string
  registration_date: string
  user_id: number
  fname: string
  lname: string
  driving_license: string
} & WithId

export type DriverTask = {
  start_time: string
  driver_id: number
  distance: number
  end_time: null | string
  start_location: string
  end_location: string
  time_spent: string
  status: string
} & WithId
