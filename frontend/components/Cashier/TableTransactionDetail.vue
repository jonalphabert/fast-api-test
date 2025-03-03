<template>
  <div class="overflow-x-auto rounded-lg border border-zinc-200 shadow-sm">
    <table class="min-w-full divide-y divide-zinc-200">
      <thead class="bg-zinc-50">
        <tr>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-zinc-700 uppercase tracking-wider">Product Name</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-zinc-700 uppercase tracking-wider">Stock</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-zinc-700 uppercase tracking-wider">Price</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-zinc-700 uppercase tracking-wider">Subtotal</th>
        </tr>
      </thead>

      <tbody class="bg-white divide-y divide-zinc-200">
        <tr v-for="(product, index) in tableData" :key="index">
          <td class="px-6 py-4 whitespace-nowrap text-sm text-zinc-700">
            {{ product.transaction_product_name }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-zinc-700" @click.value="oneclick(product)">
            {{ product.transaction_detail_quantity }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-zinc-700">${{ product.transaction_detail_price.toFixed(2) }}</td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-zinc-700">${{ product.transaction_detail_subtotal.toFixed(2) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { showConfirmationDelete } from "~/utils/showSweetalert.js";

const click = ref(0);
const timer = ref(null);

const props = defineProps({
  tableData: {
    type: Array,
    // required: true,
    default: () => [
      {
        code: "9755142",
        name: "haahhaha",
        stock: 99,
        price: 9999,
      },
      {
        code: "9755144",
        name: "haahhaha",
        stock: 99,
        price: 9999,
      },
      {
        code: "9755145",
        name: "haahhaha",
        stock: 99,
        price: 9999,
      },
      {
        code: "9755149",
        name: "haahhaha",
        stock: 99,
        price: 9999,
      },
    ],
  },
});

const editTransactionQuantity = async (product) => {
  const quantity = prompt("Quantity", product.quantityTransaction);
  if (quantity > 0) {
    product.quantityTransaction = quantity;
  } else {
    alert("Quantity must be greater than 0");
  }
};

function oneclick(product) {
  click.value++;
  if (click.value === 1) {
    timer.value = setTimeout(() => {
      click.value = 0;
    }, 1000);
  } else {
    clearTimeout(timer.value);
    editTransactionQuantity(product);
    click.value = 0;
  }
}
</script>
