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
import type { Driver } from '@/api/driver-rest/types'
import { RouteNames } from '@/router/types'

const api = useApi()
const router = useRouter()

const validationSchema = yup.object().shape({
  email: yup.string().email().required(),
  password: yup.string().required(),
  passwordConfirmation: yup
    .string()
    .oneOf([yup.ref('password')], 'Passwords do not match.')
    .required('password confirmation is a required field'),

  firstName: yup.string().required(),
  lastName: yup.string().required(),
  middleName: yup.string().required(),

  phoneNumber: yup.string().required(),
  drivingLicense: yup.string().required(),
})

type FormValues = yup.InferType<typeof validationSchema>

const initialValues: FormValues = {
  email: '',
  password: '',
  passwordConfirmation: '',

  firstName: '',
  lastName: '',
  middleName: '',

  phoneNumber: '',
  drivingLicense: '',
}

const { handleSubmit, setErrors } = useForm<FormValues>({
  validationSchema,
  initialValues,
})

const onSubmit = handleSubmit(async (values) => {
  try {
    const user = await api.auth.register(values).then(({ data }) => data)

    const payload: Omit<Driver, 'id'> = {
      user_id: user.id,
      mname: values.middleName,
      phone_num: values.phoneNumber,
      registration_date: new Date().toJSON().split('T')[0],
      fname: values.firstName,
      lname: values.lastName,
      driving_license: values.drivingLicense,
    }

    await api.driver.create(payload)

    await router.push({
      name: RouteNames.ADMIN_DRIVERS_LIST,
    })

    useSnackbar().show({
      message: 'Driver successfully created',
    })
  } catch (e) {
    const { response } = e as AxiosError<AuthRegisterErrorResponse>

    if (response?.status == 400 && response.data.detail == 'REGISTER_USER_ALREADY_EXISTS') {
      setErrors({
        email: 'This email address is busy',
      })
    }
  }
})
</script>

<template>
  <div class="flex flex-col gap-8">
    <h1 class="text-2xl font-bold">{{ 'Driver Create Form' }}</h1>

    <form class="flex flex-col gap-6" @submit="onSubmit">
      <div class="grid grid-cols-3 gap-4">
        <div class="flex flex-col gap-2">
          <BaseInput name="email">
            <template #label>
              {{ 'Email' }}
            </template>
          </BaseInput>
          <BaseInput name="password" type="password">
            <template #label>
              {{ 'Password' }}
            </template>
          </BaseInput>
          <BaseInput name="passwordConfirmation" type="password">
            <template #label>
              {{ 'Password confirmation' }}
            </template>
          </BaseInput>
        </div>

        <div class="flex flex-col gap-2">
          <BaseInput name="firstName">
            <template #label>
              {{ 'First name' }}
            </template>
          </BaseInput>
          <BaseInput name="lastName">
            <template #label>
              {{ 'Last name' }}
            </template>
          </BaseInput>
          <BaseInput name="middleName">
            <template #label>
              {{ 'Middle name' }}
            </template>
          </BaseInput>
        </div>

        <div class="flex flex-col gap-2">
          <BaseInput name="phoneNumber">
            <template #label>
              {{ 'Phone number' }}
            </template>
          </BaseInput>
          <BaseInput name="drivingLicense">
            <template #label>
              {{ 'Driving licensee' }}
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
