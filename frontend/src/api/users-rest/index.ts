import type { AxiosInstance } from 'axios'

import { BaseRest } from '../BaseRest'
import type { WithId } from '../types'
import type { User, UserUpdate } from './types'

export class UsersRest extends BaseRest {
  constructor(instance: AxiosInstance) {
    super(instance)
  }

  public getAll() {
    return this.instance.get<User[]>('/api/users/get_all_users')
  }

  public getById({ id }: { id: number }) {
    return this.instance.get<User>(`/users/${id}`)
  }

  public me() {
    return this.instance.get<User>('/users/me')
  }

  public update(body: Partial<UserUpdate> & WithId) {
    return this.instance.patch(`/users/${body.id}`, body)
  }

  public updateMe(body: Partial<UserUpdate> & WithId) {
    return this.instance.patch('/users/me', body)
  }

  public remove({ id }: { id: number }) {
    return this.instance.delete(`/users/${id}`)
  }
}
