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
import type { FuelingView } from '@/api/fueling-person/types'
import { RouteNames } from '@/router/types'

const api = useApi()
const router = useRouter()

const validationSchema = yup.object().shape({
  vehicleID: yup.number().positive().required(),
  driverID: yup.number().positive().required(),
  carPlateInfo: yup.string().required(),

  dateAndTime: yup.date().required(),
  amountOfFuel: yup.number().positive().required(),
  fuelType: yup.string().required(),
  cost: yup.number().positive().required(),
  gasStationName: yup.string().required(),
  fuelingPersonnelID: yup.number().positive().required(),
  fuelLevelsBefore: yup.number().positive().required(),
  fuelLevelsAfter: yup.number().positive().required(),
  milage: yup.number().positive().required(),
})

type FormValues = yup.InferType<typeof validationSchema>

const initialValues: FormValues = {
  vehicleID: '',
  driverID: '',
  carPlateInfo: '',

  dateAndTime: '',
  amountOfFuel: '',
  fuelType: '',

  cost: '',
  gasStationName: '',
  fuelingPersonnelID: '',
  fuelLevelsBefore: '',
  fuelLevelsAfter: '',
  milage: '',
} as any

const { handleSubmit } = useForm<FormValues>({
  validationSchema,
  initialValues,
})

const onSubmit = handleSubmit(async (values) => {
  const payload = {
    vehicle_id: values.vehicleID,
    driver_id: values.driverID,
    car_plate_info: values.carPlateInfo,

    date_and_time: new Date(values.dateAndTime).toJSON(),
    amount_of_fuel: values.amountOfFuel,
    fuel_type: values.fuelType,

    cost: values.cost,
    gas_station_name: values.gasStationName,
    fueling_personnel_id: values.fuelingPersonnelID,
    fuel_levels_before: values.fuelLevelsBefore,
    fuel_levels_after: values.fuelLevelsAfter,
    milage: values.milage,

    driver_image: '',
  }

  await api.fuel.createFuelingView(payload)

  await router.push({
    name: RouteNames.FUELING_FUEL_LIST,
  })

  useSnackbar().show({
    message: 'Fueling View successfully created',
  })
}, console.error)
</script>

<template>
  <div class="flex flex-col gap-8">
    <h1 class="text-2xl font-bold">{{ 'Fueling View Create Form' }}</h1>

    <form class="flex flex-col gap-6" @submit="onSubmit">
      <div class="grid grid-cols-3 gap-4">
        <div class="flex flex-col gap-2">
          <BaseInput name="vehicleID" type="number">
            <template #label>
              {{ 'Vehicle ID' }}
            </template>
          </BaseInput>
          <BaseInput name="driverID" type="number">
            <template #label>
              {{ 'Driver ID' }}
            </template>
          </BaseInput>
          <BaseInput name="carPlateInfo">
            <template #label>
              {{ 'Car Plate Info' }}
            </template>
          </BaseInput>
          <BaseInput name="dateAndTime" type="datetime-local">
            <template #label>
              {{ 'Date and Time' }}
            </template>
          </BaseInput>
        </div>

        <div class="flex flex-col gap-2">
          <BaseInput name="amountOfFuel" type="number">
            <template #label>
              {{ 'Amount Of Fuel' }}
            </template>
          </BaseInput>
          <BaseInput name="fuelType">
            <template #label>
              {{ 'Fuel Type' }}
            </template>
          </BaseInput>
          <BaseInput name="cost" type="number">
            <template #label>
              {{ 'Cost' }}
            </template>
          </BaseInput>
          <BaseInput name="gasStationName">
            <template #label>
              {{ 'Gas Station Name' }}
            </template>
          </BaseInput>
        </div>

        <div class="flex flex-col gap-2">
          <BaseInput name="fuelingPersonnelID" type="number">
            <template #label>
              {{ 'Fueling Personnel ID' }}
            </template>
          </BaseInput>
          <BaseInput name="fuelLevelsBefore" type="number">
            <template #label>
              {{ 'Fuel Levels Before' }}
            </template>
          </BaseInput>
          <BaseInput name="fuelLevelsAfter" type="number">
            <template #label>
              {{ 'Fuel Levels After' }}
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
