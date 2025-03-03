<template>
  <div>
    <Header />

    <div class="container mx-auto px-6 py-12">

      <div class="mt-8">
        <TransactionTable :tableData="transactionsData"/>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">

import TransactionTable from "~/components/Transaction/TransactionTable.vue";

const transactionsData = ref([{
  code: "9755142",
  date: "27 Aug 2025",
  user: "haahhaha",
  total: 9999
},
  {
    code: "9755142",
    date: "27 Aug 2025",
    user: "haahhaha",
    total: 9251
  },
  {
    code: "9755142",
    date: "27 Aug 2025",
    user: "haahhaha",
    total: 111
  },
  {
    code: "9755142",
    date: "27 Aug 2025",
    user: "haahhaha",
    total: 933
  },
])
</script>