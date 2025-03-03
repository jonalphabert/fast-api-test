<template>
  <div class="overflow-x-auto rounded-lg border border-zinc-200 shadow-sm">
    <table class="min-w-full divide-y divide-zinc-200">
      <thead class="bg-zinc-50">
      <tr>
        <th
            scope="col"
            class="px-6 py-3 text-left text-xs font-medium text-zinc-700 uppercase tracking-wider"
        >
          Transaction ID
        </th>
        <th
            scope="col"
            class="px-6 py-3 text-left text-xs font-medium text-zinc-700 uppercase tracking-wider"
        >
          Transaction Date
        </th>
        <th
            scope="col"
            class="px-6 py-3 text-left text-xs font-medium text-zinc-700 uppercase tracking-wider"
        >
          Cashier Operator
        </th>
        <th
            scope="col"
            class="px-6 py-3 text-left text-xs font-medium text-zinc-700 uppercase tracking-wider"
        >
          Total Amount
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
      <tr v-for="(transaction, index) in tableData" :key="index">
        <td class="px-6 py-4 whitespace-nowrap text-sm text-zinc-700">
          {{ transaction.code }}
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-zinc-700">
          {{ transaction.date }}
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-zinc-700">
          {{ transaction.user }}
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-zinc-700">
          ${{ transaction.total.toFixed(2) }}
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-zinc-700">
          <button
              @click="detailTransaction(transaction)"
              class="text-zinc-50 hover:text-zinc-100 hover:bg-zinc-900 mr-2 bg-zinc-600 px-2.5 py-1 rounded cursor-pointer"
          >
            Detail
          </button>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const props = defineProps({
  tableData: {
    type: Array,
    // required: true,
    default: () => [{
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
    ],
  },
});

const emit = defineEmits(['select']);

const detailTransaction = (transaction) => {
  router.push('/cashier/transaction/' + transaction.code);
};
</script>