<script setup lang="ts">
import * as yup from 'yup'
import { useForm } from 'vee-validate'
import { useRouter } from 'vue-router'

import BaseButton from '@/components/BaseButton/BaseButton.vue'
import BaseInput from '@/components/BaseInput/BaseInput.vue'

import { useSnackbar } from '@/composables'

import { useApi } from '@/api'
import { RouteNames } from '@/router/types'

const api = useApi()
const router = useRouter()

const validationSchema = yup.object().shape({
  vehicleID: yup.number().positive().required(),
  mainteneancePersonnelID: yup.number().positive().required(),
  maintenanceDescription: yup.string().required(),

  dateAndTime: yup.date().required(),
  partNumbers: yup.number().positive().required(),
  price: yup.number().positive().required(),
  status: yup.string().required(),
  milage: yup.number().positive().required(),
})

type FormValues = yup.InferType<typeof validationSchema>

const initialValues: FormValues = {
  vehicleID: '',
  mainteneancePersonnelID: '',
  maintenanceDescription: '',

  dateAndTime: '',
  partNumbers: '',
  status: '',

  price: '',
  milage: '',
} as any

const { handleSubmit } = useForm<FormValues>({
  validationSchema,
  initialValues,
})

const onSubmit = handleSubmit(async (values) => {
  const payload = {
    vehicle_id: values.vehicleID,
    mainteneance_personnel_id: values.mainteneancePersonnelID,
    maintenance_description: values.maintenanceDescription,

    date_and_time: new Date(values.dateAndTime).toJSON(),
    part_numbers: values.partNumbers,
    status: values.status,

    price: values.price,
    milage: values.milage,

    photo: '',
  }

  await api.maintenance.createMaintenanceView(payload)

  await router.push({
    name: RouteNames.MAINTENANCE_APPOINTENTS_LIST,
  })

  useSnackbar().show({
    message: 'Maintenance Record successfully created',
  })
}, console.error)
</script>

<template>
  <div class="flex flex-col gap-8">
    <h1 class="text-2xl font-bold">{{ 'Maintenance Record Create Form' }}</h1>

    <form class="flex flex-col gap-6" @submit="onSubmit">
      <div class="grid grid-cols-3 gap-4">
        <div class="flex flex-col gap-2">
          <BaseInput name="vehicleID" type="number">
            <template #label>
              {{ 'Vehicle ID' }}
            </template>
          </BaseInput>
          <BaseInput name="mainteneancePersonnelID" type="number">
            <template #label>
              {{ 'Mainteneance Personnel ID' }}
            </template>
          </BaseInput>
          <BaseInput name="maintenanceDescription">
            <template #label>
              {{ 'Maintenance Description' }}
            </template>
          </BaseInput>
        </div>

        <div class="flex flex-col gap-2">
          <BaseInput name="dateAndTime" type="datetime-local">
            <template #label>
              {{ 'Date and Time' }}
            </template>
          </BaseInput>
          <BaseInput name="partNumbers" type="number">
            <template #label>
              {{ 'Part Numbers' }}
            </template>
          </BaseInput>
          <BaseInput name="price" type="number">
            <template #label>
              {{ 'Price' }}
            </template>
          </BaseInput>
        </div>

        <div class="flex flex-col gap-2">
          <BaseInput name="status">
            <template #label>
              {{ 'Status' }}
            </template>
          </BaseInput>
          <BaseInput name="milage" type="number">
            <template #label>
              {{ 'Milage' }}
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
