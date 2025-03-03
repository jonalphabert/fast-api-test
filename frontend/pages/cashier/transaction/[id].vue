<template>
  <div>
    <Header />

    <div class="container mx-auto px-6 py-12">

      <div class="mt-8">
        <TableCashier :tableData="transactionsData"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import TableCashier from "~/components/Cashier/TableCashier.vue";

const transactionsData = [{
  code: "9755142",
  name: "haahhaha",
  stock: 99,
  price: 9999
},{
  code: "9755144",
  name: "haahhaha",
  stock: 99,
  price: 9999
},{
  code: "9755145",
  name: "haahhaha",
  stock: 99,
  price: 9999
},{
  code: "9755149",
  name: "haahhaha",
  stock: 99,
  price: 9999
}]
</script>