<template>
  <div class="flex min-h-screen">
    <slot name="sidebar" />

    <div class="grow p-4">
      <slot />
    </div>
  </div>
</template>
