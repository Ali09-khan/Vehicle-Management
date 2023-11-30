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
})

type FormValues = yup.InferType<typeof validationSchema>

const initialValues: FormValues = {
  email: '',
  password: '',
  passwordConfirmation: '',
}

const { handleSubmit, setErrors } = useForm<FormValues>({
  validationSchema,
  initialValues,
})

const onSubmit = handleSubmit(async (values) => {
  try {
    await api.auth.register(values)

    await router.push({
      name: RouteNames.ADMIN_USERS_LIST,
    })

    useSnackbar().show({
      message: 'User successfully created',
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
    <h1 class="text-2xl font-bold">{{ 'User Create Form' }}</h1>

    <form class="flex max-w-[30rem] flex-col gap-6" @submit="onSubmit">
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

      <BaseButton type="submit">
        {{ 'Create' }}
      </BaseButton>
    </form>
  </div>
</template>
