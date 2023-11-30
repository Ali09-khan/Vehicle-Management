import type { AxiosInstance } from 'axios'

import { BaseRest } from '../BaseRest'
import type { Driver, DriverTask } from './types'

export class DriverRest extends BaseRest {
  constructor(instance: AxiosInstance) {
    super(instance)
  }

  public create(body: Omit<Driver, 'id'>) {
    return this.instance.post('/api/driver/create_driver', body)
  }

  public getAll() {
    return this.instance.get<Driver[]>('/api/driver/get_all_drivers')
  }

  public getMyTasks() {
    return this.instance.get<DriverTask[]>('/api/driver/get_my_tasks')
  }
}
