import type { AxiosInstance } from 'axios'

import { BaseRest } from '../BaseRest'
import type { MaintenanceView } from './types'

export class MaintenanceRest extends BaseRest {
  constructor(instance: AxiosInstance) {
    super(instance)
  }

  public createMaintenanceView(body: any) {
    return this.instance.post('/api/maintenance_record/create_maintenance_record', body)
  }

  public getAll() {
    return this.instance.get<MaintenanceView[]>('/api/maintenance_record/get_all_maintenance_records')
  }
}
