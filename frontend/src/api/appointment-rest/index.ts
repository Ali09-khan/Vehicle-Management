import type { AxiosInstance } from 'axios'

import { BaseRest } from '../BaseRest'

export class AppointmentRest extends BaseRest {
  constructor(instance: AxiosInstance) {
    super(instance)
  }
}
