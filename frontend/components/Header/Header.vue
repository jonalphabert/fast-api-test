<template>
  <nav class="w-full bg-sky-50">
    <div class="flex items-center justify-between container mx-auto py-6 px-6 text-sky-950">
      <div class="text-2xl font-semibold">Cashier App</div>
      <div class="flex gap-6">
        <nuxt-link to="/cashier">Cashier</nuxt-link>
        <nuxt-link to="/cashier/transaction">Transaction</nuxt-link>
      </div>
    </div>
  </nav>
</template>