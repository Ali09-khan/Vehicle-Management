import type { AxiosInstance } from 'axios'

import { BaseRest } from '../BaseRest'
import type { FuelingView } from './types'

export class FuelRest extends BaseRest {
  constructor(instance: AxiosInstance) {
    super(instance)
  }

  public createFuelingView(body: any) {
    return this.instance.post('/api/fueling_record/create_fueling_record', body)
  }

  public getAll() {
    return this.instance.get<FuelingView[]>('/api/fueling_record/get_all_fueling_records')
  }
}
