<script setup lang="ts">
import * as yup from 'yup'
import type { AxiosError } from 'axios'
import { useForm } from 'vee-validate'
import { useRouter } from 'vue-router'

import BaseButton from '@/components/BaseButton/BaseButton.vue'
import BaseInput from '@/components/BaseInput/BaseInput.vue'
import BaseSelect from '@/components/BaseSelect/BaseSelect.vue'

import { useSnackbar } from '@/composables'

import { useApi } from '@/api'
import type { AuthRegisterErrorResponse } from '@/api/auth-rest/types'
import { RouteNames } from '@/router/types'
import { useRoleStore } from '@/stores'

const api = useApi()
const router = useRouter()
const roleStore = useRoleStore()

const validationSchema = yup.object().shape({
  id: yup.number().positive().required(),
  email: yup.string().email().required(),
  password: yup.string(),
  role_id: yup.number().positive().required(),
})

type FormValues = yup.InferType<typeof validationSchema>

const initialValues: FormValues = await api.users
  .getById({ id: Number(router.currentRoute.value.params.id) })
  .then(({ data }) => data)

const { handleSubmit, setErrors } = useForm<FormValues>({
  validationSchema,
  initialValues,
})

const roleOptions = [...roleStore.roles]

const onSubmit = handleSubmit(async (values) => {
  try {
    await api.users.update(values)

    await router.push({
      name: RouteNames.ADMIN_USERS_LIST,
    })

    useSnackbar().show({
      message: 'User successfully updated',
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
    <h1 class="text-2xl font-bold">{{ 'User Edit Form' }}</h1>

    <form class="flex max-w-[30rem] flex-col gap-6" @submit="onSubmit">
      <BaseInput name="id" readonly>
        <template #label>
          {{ 'ID' }}
        </template>
      </BaseInput>
      <BaseInput name="email">
        <template #label>
          {{ 'Email' }}
        </template>
      </BaseInput>
      <BaseSelect label-field="name" name="role_id" :options="roleOptions" type="password" value-field="id">
        <template #label>
          {{ 'Role' }}
        </template>
      </BaseSelect>
      <BaseInput name="password" type="password">
        <template #label>
          {{ 'Password' }}
        </template>
      </BaseInput>

      <BaseButton type="submit">
        {{ 'Update' }}
      </BaseButton>
    </form>
  </div>
</template>
