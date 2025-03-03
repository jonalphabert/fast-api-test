<template>
  <nav class="w-full bg-sky-50">
    <div class="flex items-center justify-between container mx-auto py-6 px-6 text-sky-950">
      <div class="text-2xl font-semibold">Cashier App</div>
      <div class="flex gap-6">
        <nuxt-link to="/cashier">Cashier</nuxt-link>
        <nuxt-link to="/cashier/transaction">Transaction</nuxt-link>
        <div class="cursor-pointer" @click="logout">Logout</div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const logout = () => {
  localStorage.removeItem("token");
  router.push("/");
};
</script>
