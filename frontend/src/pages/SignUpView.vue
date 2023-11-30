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
    .oneOf([yup.ref('password')], 'Your passwords do not match.')
    .required(),
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
      name: RouteNames.SIGN_IN,
      query: router.currentRoute.value.query,
    })

    useSnackbar().show({
      message: 'You have successfully registered',
    })
  } catch (e) {
    const { response } = e as AxiosError<AuthRegisterErrorResponse>

    if (response?.status == 400 && response.data.detail == 'REGISTER_USER_ALREADY_EXISTS') {
      setErrors({
        email: ' ',
        password: ' ',
        passwordConfirmation: 'This email address is busy',
      })
    }
  }
})
</script>

<template>
  <form class="flex w-full max-w-[30rem] flex-col gap-5 rounded-lg bg-white px-10 py-12 text-center" @submit="onSubmit">
    <h1 class="text-xl font-bold">{{ 'REGISTER' }}</h1>

    <div class="flex flex-col gap-3">
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

      <BaseButton type="submit">{{ 'Sign Up' }}</BaseButton>
    </div>

    <RouterLink
      class="font-medium text-blue-500"
      :to="{ name: RouteNames.SIGN_IN, query: router.currentRoute.value.query }"
    >
      {{ 'Already have an account? Sign In' }}
    </RouterLink>
  </form>
</template>
