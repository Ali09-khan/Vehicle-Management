export type AuthRegister = {
  email: string
  password: string
}

export type AuthLogin = {
  /**
   * is Email fucking backender
   */
  username: string
  password: string
}

export type AuthRegisterErrorResponse = { detail: 'REGISTER_USER_ALREADY_EXISTS' }
