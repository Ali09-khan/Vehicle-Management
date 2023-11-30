import type { AxiosInstance } from 'axios'

import { BaseRest } from '../BaseRest'
import type { Role } from './types'

export class RoleRest extends BaseRest {
  constructor(instance: AxiosInstance) {
    super(instance)
  }

  public getAll() {
    return this.instance.get<Role[]>('/api/role/get_all_roles')
  }
}
