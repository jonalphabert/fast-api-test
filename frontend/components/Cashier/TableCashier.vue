<template>
  <div class="overflow-x-auto rounded-lg border border-zinc-200 shadow-sm">
    <table class="min-w-full divide-y divide-zinc-200">
      <thead class="bg-zinc-50">
      <tr>
        <th
            scope="col"
            class="px-6 py-3 text-left text-xs font-medium text-zinc-700 uppercase tracking-wider"
        >
          Product Code
        </th>
        <th
            scope="col"
            class="px-6 py-3 text-left text-xs font-medium text-zinc-700 uppercase tracking-wider"
        >
          Product Name
        </th>
        <th
            scope="col"
            class="px-6 py-3 text-left text-xs font-medium text-zinc-700 uppercase tracking-wider"
        >
          Stock
        </th>
        <th
            scope="col"
            class="px-6 py-3 text-left text-xs font-medium text-zinc-700 uppercase tracking-wider"
        >
          Price
        </th>
        <th
            scope="col"
            class="px-6 py-3 text-left text-xs font-medium text-zinc-700 uppercase tracking-wider"
        >
          Actions
        </th>
      </tr>
      </thead>

      <tbody class="bg-white divide-y divide-zinc-200">
      <tr v-for="(product, index) in tableData" :key="index">
        <td class="px-6 py-4 whitespace-nowrap text-sm text-zinc-700">
          {{ product.code }}
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-zinc-700">
          {{ product.name }}
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-zinc-700">
          {{ product.stock }}
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-zinc-700">
          ${{ product.price.toFixed(2) }}
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-zinc-700">
          <button
              @click="deleteDetailTransaction(product, index)"
              class="text-zinc-50 hover:text-zinc-100 hover:bg-zinc-900 mr-2 bg-zinc-600 px-2.5 py-1 rounded cursor-pointer"
          >
            -
          </button>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import {showConfirmationDelete} from "~/utils/showSweetalert.js";

const props = defineProps({
  tableData: {
    type: Array,
    // required: true,
    default: () => [{
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
    }],
  },
});

const emit = defineEmits(['deleteFromTransaction']);

const deleteDetailTransaction = async (product, index) => {
  const confirmation = await showConfirmationDelete();
  if(confirmation) emit('deleteFromTransaction', product, index);
};
</script>