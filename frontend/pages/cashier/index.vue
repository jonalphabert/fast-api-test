<template>
  <div>
    <Header />

    <div class="container mx-auto px-6 py-12">
      <div class="flex justify-between">
        <div class="flex items-center gap-2 justify-center">
          <label for="email" class="block text-base font-medium text-gray-900 py-1">Kode Product</label>
          <div class="mt-2">
            <input
              type="text"
              name="searchByProductCodeFields"
              id="searchByProductCodeFields"
              required
              class="block w-full rounded-md bg-white px-3 py-1 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-sky-600 sm:text-sm/6"
              :autofocus="!isVisible"
              v-model="searchByProductCodeFields"
            />
          </div>
        </div>

        <button class="bg-sky-950 py-1 px-3 text-gray-50 rounded cursor-pointer" @click="showModalProductSearch">Cari Barang</button>
      </div>

      <div class="mt-8">
        <TableCashier :table-data="tableDataTransaction" @deleteFromTransaction="deleteProductFromTransaction" />
      </div>

      <div class="fixed bottom-0 container px-6">
        <div class="border border-zinc-400 rounded-t-xl py-6 px-6 flex items-center justify-between">
          <h5 class="text-2xl font-bold tracking-wide">Total : {{ totalTransaction }}</h5>
          <button class="cursor-pointer py-2 px-4 bg-zinc-200 rounded-lg text-zinc-900" @click="saveTransaction">Simpan Transaksi</button>
        </div>
      </div>

      <ModalSearchProduct ref="searchProductModal" @close-modal="isVisible = false" @addProduct="addProductToTransaction" />
    </div>
  </div>
</template>

<script setup>
import ModalSearchProduct from "~/components/Cashier/ModalSearchProduct.vue";
import TableCashier from "~/components/Cashier/TableCashier.vue";

import { debounce } from "@/utils/debounce";
import { headerGenerator } from "@/utils/generateHeader";
import { showErrorAlert, showSuccessAlert } from "@/utils/showSweetalert";

const searchByProductCodeFields = ref("");
const searchProductModal = ref(null);

const tableDataTransaction = ref([]);

const isVisible = ref(false);

const totalTransaction = computed(() => {
  if (tableDataTransaction.value.length === 0) {
    return 0;
  }
  return tableDataTransaction.value.reduce((accumulator, currentValue) => accumulator + currentValue.product_price * currentValue.quantityTransaction, 0);
});

function showModalProductSearch() {
  isVisible.value = true;
  searchProductModal.value.openModal();
}

function deleteProductFromTransaction(product, index) {
  tableDataTransaction.value.splice(index, 1);
}

async function saveTransaction() {
  try {
    console.log(tableDataTransaction.value);

    const product_list = tableDataTransaction.value.map((item) => {
      return {
        product_id: item.product_id,
        quantity_transaction: item.quantityTransaction,
        product_price: item.product_price,
      };
    });

    const param = {
      transaction_details: product_list,
    };

    const response = await fetch("http://localhost:8000/api/transactions", {
      method: "POST",
      headers: headerGenerator(),
      body: JSON.stringify(param),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail);
    }

    tableDataTransaction.value = [];
    showSuccessAlert("Transaksi berhasil disimpan");
  } catch (err) {
    showErrorAlert(err);
  }
}

const searchProductbyBarcode = async () => {
  try {
    if (searchByProductCodeFields.value.trim().length === 0) {
      return;
    }
    const response = await fetch(`http://localhost:8000/api/products?barcode=${searchByProductCodeFields.value}`, {
      method: "GET",
      headers: headerGenerator(),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail);
    }

    data.data.quantityTransaction = 1;

    tableDataTransaction.value.push(data.data);

    searchByProductCodeFields.value = "";
  } catch (err) {
    showErrorAlert(err);
  }
};

const debouncedSearch = debounce(searchProductbyBarcode, 1000);

watch(searchByProductCodeFields, (newValue) => {
  debouncedSearch(newValue);
});

const addProductToTransaction = (product) => {
  product.quantityTransaction = 1;
  tableDataTransaction.value.push(product);
};
</script>
