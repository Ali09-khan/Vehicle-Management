import type { AxiosInstance } from 'axios'

export abstract class BaseRest {
  constructor(protected instance: AxiosInstance) {}
}
