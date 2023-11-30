import type { WithId } from '../types'

export type FuelingView = {
  vehicle_id: number
  driver_id: number
  car_plate_info: string
  date_and_time: null | string
  amount_of_fuel: number
  fuel_type: string
  cost: number
  gas_station_name: string
  fueling_personnel_id: number
  fuel_levels_before: number
  fuel_levels_after: number
  milage: number
} & WithId
