<template>
  <div>
    <Header />

    <div class="container mx-auto px-6 py-12">
      <div class="mt-8">
        <TransactionTable :tableData="transactionsData" />
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import TransactionTable from "~/components/Transaction/TransactionTable.vue";

import { headerGenerator } from "@/utils/generateHeader";

const transactionsData = ref([
  {
    code: "9755142",
    date: "27 Aug 2025",
    user: "haahhaha",
    total: 9999,
  },
  {
    code: "9755142",
    date: "27 Aug 2025",
    user: "haahhaha",
    total: 9251,
  },
  {
    code: "9755142",
    date: "27 Aug 2025",
    user: "haahhaha",
    total: 111,
  },
  {
    code: "9755142",
    date: "27 Aug 2025",
    user: "haahhaha",
    total: 933,
  },
]);

const fetchTransaction = async () => {
  try {
    const response = await fetch("http://localhost:8000/api/transactions", {
      method: "GET",
      headers: headerGenerator(),
    });
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.message);
    }
    transactionsData.value = data.data;
    console.log(transactionsData.value);
  } catch (error) {
    console.error("Error fetching products:", error);
  }
};

onMounted(() => {
  fetchTransaction();
});
</script>
