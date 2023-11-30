<script setup lang="ts">
import * as yup from 'yup'
import type { AxiosError } from 'axios'
import { useForm } from 'vee-validate'
import { useRouter } from 'vue-router'

import BaseButton from '@/components/BaseButton/BaseButton.vue'
import BaseInput from '@/components/BaseInput/BaseInput.vue'

import { useSnackbar } from '@/composables'

import { useApi } from '@/api'
import type { AuthRegisterErrorResponse } from '@/api/auth-rest/types'
import type { TaskView } from '@/api/task-rest/types'
import { RouteNames } from '@/router/types'

const api = useApi()
const router = useRouter()

const validationSchema = yup.object().shape({
  id: yup.number().positive().required(),  
  startTime: yup.string().required(),  
  driverID: yup.number().positive().required(),
  distance: yup.number().positive().required(),
  endTime: yup.string().required(),  
  startLocation: yup.string().required(),  
  endLocation: yup.string().required(),  
  timeSpent: yup.string().required(),  
  status: yup.string().required(),  
})

type FormValues = yup.InferType<typeof validationSchema>

const initialValues: FormValues = {
  id: '',
  startTime: '',
  driverID: '',
  distance: '',

  endTime: '',
  startLocation: '',
  endLocation: '',

  timeSpent: '',
  status: '',
} as any

const { handleSubmit, setErrors } = useForm<FormValues>({
  validationSchema,
  initialValues,
})

const onSubmit = handleSubmit(async (values) => {
  const payload = {
    id: values.id,
    start_time: values.startTime,
    driver_id: values.driverID,
    distance: values.distance,
    end_time: values.endTime,
    start_location: values.startLocation,
    end_location: values.endLocation,
    time_spent: values.timeSpent,
    status: values.status,
  }

  await api.task.createTaskView(payload)

  await router.push({
    name: RouteNames.ADMIN_TASK_CREATE,
  })

  useSnackbar().show({
    message: 'Task successfully created',
  })
}, console.error)
</script>

<template>
  <div class="flex flex-col gap-8">
    <h1 class="text-2xl font-bold">{{ 'Driver Create Form' }}</h1>

    <form class="flex flex-col gap-6" @submit="onSubmit">
      <div class="grid grid-cols-3 gap-4">
        <div class="flex flex-col gap-2">
          <BaseInput name="id" type="number">
            <template #label>
              {{ 'ID' }}
            </template>
          </BaseInput>
          <BaseInput name="driverID" type="number">
            <template #label>
              {{ 'Driver ID' }}
            </template>
          </BaseInput>
          <BaseInput name="status">
            <template #label>
              {{ 'Status' }}
            </template>
          </BaseInput>
        </div>

        <div class="flex flex-col gap-2">
          <BaseInput name="startTime">
            <template #label>
              {{ 'Start Time' }}
            </template>
          </BaseInput>
          <BaseInput name="endTime">
            <template #label>
              {{ 'End Time' }}
            </template>
          </BaseInput>
          <BaseInput name="startLocation">
            <template #label>
              {{ 'Start Location' }}
            </template>
          </BaseInput>
        </div>

        <div class="flex flex-col gap-2">
          <BaseInput name="endLocation">
            <template #label>
              {{ 'End Location' }}
            </template>
          </BaseInput>
          <BaseInput name="timeSpent">
            <template #label>
              {{ 'Time Spent' }}
            </template>
          </BaseInput>
          <BaseInput name="distance">
            <template #label>
              {{ 'Distance' }}
            </template>
          </BaseInput>          
        </div>
      </div>

      <BaseButton class="self-start" type="submit">
        {{ 'Create' }}
      </BaseButton>
    </form>
  </div>
</template>
