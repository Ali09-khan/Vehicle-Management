import type { AxiosInstance } from 'axios'
import qs from 'qs'

import { BaseRest } from '../BaseRest'
import type { User } from '../users-rest/types'
import type { AuthLogin, AuthRegister } from './types'

export class AuthRest extends BaseRest {
  constructor(instance: AxiosInstance) {
    super(instance)
  }

  public register(body: AuthRegister) {
    return this.instance.post<User>('/api/auth/register', body)
  }

  public login(body: AuthLogin) {
    return this.instance.post('/api/auth/jwt/login', qs.parse(body), {
      headers: { 'content-type': 'application/x-www-form-urlencoded' },
    })
  }

  public logOut() {
    return this.instance.post('/api/auth/jwt/logout')
  }
}
