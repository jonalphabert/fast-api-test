<template>
  <div>
    <Header />

    <div class="container mx-auto px-6 py-12">
      <div class="flex justify-between flex-row gap-2">
        <div>Tanggal Transaksi : {{ transactionsInfo.transaction_date }}</div>
        <div>Operator Kasir : {{ transactionsInfo.user_name }}</div>
      </div>
      <div class="mt-8">
        <TableTransactionDetail :tableData="transactionsData" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from "vue-router";
import TableTransactionDetail from "~/components/Cashier/TableTransactionDetail.vue";

import { headerGenerator } from "@/utils/generateHeader";
import { showErrorAlert } from "@/utils/showSweetalert";

const route = useRoute();

const transactionsData = ref([]);
const transactionsInfo = ref({});

const fetchTransaction = async () => {
  try {
    console.log(route.params.id);

    const response = await fetch(`http://localhost:8000/api/transactions/${route.params.id}`, {
      method: "GET",
      headers: headerGenerator(),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail);
    }

    transactionsData.value = data.transaction_details;
    transactionsInfo.value = data.transaction_info;
  } catch (e) {
    showErrorAlert(e);
  }
};

onMounted(() => {
  fetchTransaction();
});
</script>
