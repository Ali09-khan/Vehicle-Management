import type { AxiosInstance } from 'axios'

import { BaseRest } from '../BaseRest'
import type { TaskView } from './types'

export class TaskRest extends BaseRest {
  constructor(instance: AxiosInstance) {
    super(instance)
  }

  public createTaskView(body: any) {
    return this.instance.post('/api/task/create_task', body)
  }

  public getAll() {
    return this.instance.get<TaskView[]>('/api/task/get_all_tasks')
  }
}
