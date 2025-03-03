<template>
  <div class="h-screen flex items-center justify-center">
    <div class="justify-center items-center px-6 py-12 lg:px-8 w-fit min-w-96 mx-auto lg:px-8 border-sky-100 border-2 rounded-md hover:scale-105 transition duration-300 ease-in-out">
      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <h2 class="text-center text-2xl/9 font-bold tracking-tight text-gray-900">Sign In</h2>
      </div>

      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form class="space-y-6" method="POST" @submit="login">
          <div>
            <label for="email" class="block text-sm/6 font-medium text-gray-900">Email</label>
            <div class="mt-2">
              <input
                type="email"
                name="email"
                id="email"
                autocomplete="email"
                required
                class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-sky-600 sm:text-sm/6 hover:scale-105 focus:scale-105 active:scale-105 transition duration-700 ease-bounce"
                v-model="email"
              />
            </div>
          </div>

          <div>
            <div class="flex items-center justify-between">
              <label for="password" class="block text-sm/6 font-medium text-gray-900">Password</label>
              <!--              <div class="text-sm">-->
              <!--                <a href="#" class="font-semibold text-sky-600 hover:text-sky-500">Forgot password?</a>-->
              <!--              </div>-->
            </div>
            <div class="mt-2">
              <input
                type="password"
                name="password"
                id="password"
                autocomplete="current-password"
                required
                class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-sky-600 sm:text-sm/6 hover:scale-105 focus:scale-105 active:scale-105 transition duration-700 ease-bounce"
                v-model="password"
              />
            </div>
          </div>

          <div>
            <button
              type="submit"
              class="flex w-full justify-center rounded-md bg-sky-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-sky-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-sky-600 hover:scale-105 transition duration-700 ease-bounce"
            >
              Sign in
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const email = ref("");
const password = ref("");

async function login(e) {
  e.preventDefault();

  const params = {
    email: email.value,
    password: password.value,
  };

  try {
    const response = await $fetch("http://localhost:8000/api/login", {
      method: "POST",
      body: params,
    });
    console.log("response", response);
    localStorage.setItem("token", response.access_token);

    router.push("/cashier");
  } catch (err) {
    error.value = err;
  } finally {
    // loading.value = false;
  }
}
</script>
