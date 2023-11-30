<script setup lang="ts">
import * as yup from 'yup'
import type { AxiosError } from 'axios'
import { useForm } from 'vee-validate'
import { useRouter } from 'vue-router'

import BaseButton from '@/components/BaseButton/BaseButton.vue'
import BaseInput from '@/components/BaseInput/BaseInput.vue'

import { useApi } from '@/api'
import { AUTH_REDIRECT_QUERY } from '@/router'
import { RouteNames } from '@/router/types'
import { useAuthStore } from '@/stores'

const api = useApi()
const authStore = useAuthStore()
const router = useRouter()

const validationSchema = yup.object().shape({
  email: yup.string().email().required(),
  password: yup.string().required(),
})

type FormValues = yup.InferType<typeof validationSchema>

const initialValues: FormValues = {
  email: '',
  password: '',
}

const { handleSubmit, setErrors } = useForm<FormValues>({
  validationSchema,
  initialValues,
})

const onSubmit = handleSubmit(async (values) => {
  try {
    await api.auth.login({
      password: values.password,
      username: values.email,
    })

    await authStore.initialize()

    router.push(
      AUTH_REDIRECT_QUERY in router.currentRoute.value.query
        ? String(router.currentRoute.value.query[AUTH_REDIRECT_QUERY])
        : { name: RouteNames.PANEL_WELCOME },
    )
  } catch (e) {
    const { response } = e as AxiosError

    if (response?.status == 400) {
      setErrors({
        email: ' ',
        password: 'Invalid credentials',
      })
    }
  }
})
</script>

<template>
  <form class="flex w-full max-w-[30rem] flex-col gap-5 rounded-lg bg-white px-10 py-12 text-center" @submit="onSubmit">
    <h1 class="text-xl font-bold">{{ 'LOGIN' }}</h1>

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

      <BaseButton type="submit">{{ 'Sign In' }}</BaseButton>
    </div>

    <RouterLink
      class="font-medium text-blue-500"
      :to="{ name: RouteNames.SIGN_UP, query: router.currentRoute.value.query }"
    >
      {{ "Don't have an account yet? Sign Up" }}
    </RouterLink>
  </form>
</template>
