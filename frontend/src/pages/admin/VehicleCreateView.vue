<script setup lang="ts">
import * as yup from 'yup'
import { useForm } from 'vee-validate'
import { useRouter } from 'vue-router'

import BaseButton from '@/components/BaseButton/BaseButton.vue'
import BaseInput from '@/components/BaseInput/BaseInput.vue'
import BaseSelect from '@/components/BaseSelect/BaseSelect.vue'

import { useSnackbar } from '@/composables'

import { useApi } from '@/api'
import { RouteNames } from '@/router/types'

const api = useApi()
const router = useRouter()

const driverOptions = await api.driver
  .getAll()
  .then(({ data }) =>
    data.map((driver) => ({ name: `${driver.fname} ${driver.mname} ${driver.lname}`, value: driver.id })),
  )

const validationSchema = yup.object().shape({
  sitting_capacity: yup.number().positive().required(),
  model: yup.string().required(),
  license_plate: yup.string().required(),
  driver_id: yup.number().positive().required(),
})

type FormValues = yup.InferType<typeof validationSchema>

const initialValues: FormValues = {
  sitting_capacity: 0,
  model: '',
  license_plate: '',
  driver_id: 0,
}

const { handleSubmit } = useForm<FormValues>({
  validationSchema,
  initialValues,
})

const onSubmit = handleSubmit(async (values) => {
  await api.vehicle.create(values)

  await router.push({
    name: RouteNames.ADMIN_VEHICLES_LIST,
  })

  useSnackbar().show({
    message: 'Vehicle successfully created',
  })
})
</script>

<template>
  <div class="flex flex-col gap-8">
    <h1 class="text-2xl font-bold">{{ 'Driver Create Form' }}</h1>

    <form class="flex flex-col gap-6" @submit="onSubmit">
      <div class="grid grid-cols-3 gap-4">
        <div class="flex flex-col gap-2">
          <BaseInput name="sitting_capacity" type="number">
            <template #label>
              {{ 'Sitting capacity' }}
            </template>
          </BaseInput>
          <BaseInput name="model">
            <template #label>
              {{ 'Model' }}
            </template>
          </BaseInput>
          <BaseInput name="license_plate">
            <template #label>
              {{ 'License plate' }}
            </template>
          </BaseInput>
          <BaseSelect label-field="name" name="driver_id" :options="driverOptions" value-field="value">
            <template #label>
              {{ 'Driver' }}
            </template>
          </BaseSelect>
        </div>
      </div>

      <BaseButton class="self-start" type="submit">
        {{ 'Create' }}
      </BaseButton>
    </form>
  </div>
</template>
