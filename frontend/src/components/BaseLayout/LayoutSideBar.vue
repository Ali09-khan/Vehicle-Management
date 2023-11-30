<template>
  <div class="sticky top-0 h-screen w-[20rem] shrink-0 self-start border-r border-gray-100 bg-white drop-shadow">
    <div class="mb-10 flex h-[4.5rem] flex-col justify-center border-b border-gray-100 bg-white px-6">
      <h2 class="text-lg font-semibold">{{ 'Vehicle management' }}</h2>
      <p class="font-medium"><slot name="title" /></p>
    </div>

    <slot />
  </div>
</template>
