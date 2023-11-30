type Nullable<T> = T extends object
  ? {
      [K in keyof T]: Nullable<T[K]> | undefined | null
    }
  : T | undefined | null
