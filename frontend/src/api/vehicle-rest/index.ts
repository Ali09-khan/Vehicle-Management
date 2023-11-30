import type { AxiosInstance } from 'axios'

import { BaseRest } from '../BaseRest'
import type { Vehicle } from './types'

export class VehicleRest extends BaseRest {
  constructor(instance: AxiosInstance) {
    super(instance)
  }

  public getAll() {
    return this.instance.get<Vehicle[]>('/api/vehicle/get_all_vehicles')
  }

  public create(body: Omit<Vehicle, 'id'>) {
    return this.instance.post<Vehicle>('/api/vehicle/create_vehicle', body)
  }
}
