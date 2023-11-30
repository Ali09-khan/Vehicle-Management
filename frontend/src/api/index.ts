import type { AxiosInstance } from 'axios'
import axios from 'axios'

import { API_ENDPOINT } from '@/constants'

import { AuthRest } from './auth-rest'
import { DriverRest } from './driver-rest'
import { FuelRest } from './fueling-person'
import { RoleRest } from './role-rest'
import { UsersRest } from './users-rest'
import { VehicleRest } from './vehicle-rest'
import { MaintenanceRest } from './maintenance-person'
import { TaskRest } from './task-rest'

export class Api {
  private instance: AxiosInstance

  public readonly auth
  public readonly users
  public readonly role
  public readonly driver
  public readonly vehicle
  public readonly fuel
  public readonly maintenance
  public readonly task

  constructor() {
    this.instance = this.createInstance()

    this.auth = new AuthRest(this.instance)
    this.users = new UsersRest(this.instance)
    this.role = new RoleRest(this.instance)
    this.driver = new DriverRest(this.instance)
    this.vehicle = new VehicleRest(this.instance)
    this.fuel = new FuelRest(this.instance)
    this.maintenance = new MaintenanceRest(this.instance)
    this.task = new TaskRest(this.instance)
   }

  private createInstance() {
    return axios.create({
      baseURL: API_ENDPOINT,
      timeout: 20_000,
      withCredentials: true,
    })
  }
}

const useApi = (() => {
  const api = new Api()
  return () => api
})()

export { useApi }
