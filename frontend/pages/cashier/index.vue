<template>
  <div>
    <Header />

    <div class="container mx-auto px-6 py-12">
      <div class="flex justify-between">
        <div class="flex items-center gap-2 justify-center" >
          <label for="email" class="block text-base font-medium text-gray-900 py-1">Kode Product</label>
          <div class="mt-2">
            <input
                type="text"
                name="searchByProductCode"
                id="searchByProductCode"
                required
                class="block w-full rounded-md bg-white px-3 py-1 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-sky-600 sm:text-sm/6"
                autofocus
                v-model="searchByProductCode"/>
          </div>
        </div>

        <button class="bg-sky-950 py-1 px-3 text-gray-50 rounded cursor-pointer" @click="showModalProductSearch">Cari Barang</button>
      </div>

      <div class="mt-8">
        <TableCashier
            :table-data="tableDateTransaction"
            @deleteFromTransaction="deleteProductFromTransaction"
        />
      </div>

      <div class="fixed bottom-0 container px-6">
        <div class="border border-zinc-400 rounded-t-xl py-6 px-6 flex items-center justify-between">
          <h5 class="text-2xl font-bold tracking-wide">Total : {{lowStockProducts}}</h5>
          <button
              class="cursor-pointer py-2 px-4 bg-zinc-200 rounded-lg text-zinc-900"
              @click="saveTransaction">
            Simpan Transaksi
          </button>
        </div>
      </div>

      <ModalSearchProduct ref="searchProductModal"/>
    </div>
  </div>
</template>

<script setup>
import ModalSearchProduct from "~/components/Cashier/ModalSearchProduct.vue";
import TableCashier from "~/components/Cashier/TableCashier.vue";

const searchByProductCode = ref("");
const searchProductModal = ref(null);

const tableDateTransaction = ref([
  {
    code: "9755144",
    name: "haahhaha",
    stock: 2,
    price: 9999
  },
  {
    code: "9755142",
    name: "haahhaha",
    stock: 1,
    price: 99
  }
])

const lowStockProducts = computed(() => {
  return tableDateTransaction.value.reduce((accumulator, currentValue) => accumulator + currentValue.price, 0);
});

function showModalProductSearch() {
  searchProductModal.value.openModal();
}

function deleteProductFromTransaction(product, index) {
  tableDateTransaction.value.splice(index, 1);
}

function saveTransaction(){
  console.log("simpan transaksi");
  console.log("hahahaha")
}
</script>