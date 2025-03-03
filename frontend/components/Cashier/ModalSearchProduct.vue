<template>
  <div v-if="isOpen" class="fixed inset-0 bg-gray-400 opacity-50 transition-opacity duration-300 ease-in-out" @click="closeModal"></div>

  <div v-if="isOpen" class="fixed inset-0 flex items-center justify-center p-4">
    <div
      class="bg-white rounded-lg shadow-lg w-full max-w-4xl transform transition-all duration-300 ease-in-out"
      :class="{
        'opacity-0 translate-y-10': !isVisible,
        'opacity-100 translate-y-0': isVisible,
      }"
    >
      <div class="p-4 border-b border-zinc-200">
        <h2 class="text-xl font-semibold">Cari Barang</h2>
      </div>

      <div class="p-4">
        <div class="flex items-center gap-2 mb-8">
          <label for="email" class="block text-base font-medium text-gray-900 py-1">Nama Product</label>
          <div class="mt-2">
            <input
              type="text"
              name="searchByProductCode"
              id="searchByProductCode"
              required
              class="block w-full rounded-md bg-white px-3 py-1 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-sky-600 sm:text-sm/6"
              :autofocus="isVisible"
              v-model="searchByProductName"
            />
          </div>
        </div>

        <TableProduct :table-data="tableData" @select="addProduct" />
      </div>

      <div class="p-4 border-t border-zinc-200 flex justify-end">
        <button @click="closeModal" class="bg-red-400 text-white px-4 py-2 rounded-lg hover:bg-red-500">Close</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import { debounce } from "@/utils/debounce";
import TableProduct from "~/components/Cashier/TableProduct.vue";

const isOpen = ref(false);
const isVisible = ref(false);

const searchByProductName = ref("");

const tableData = ref([]);

const openModal = () => {
  isOpen.value = true;
  setTimeout(() => {
    isVisible.value = true;
  }, 10);
};

const closeModal = () => {
  isVisible.value = false;
  setTimeout(() => {
    isOpen.value = false;
  }, 300); // Match the duration of the animation
  emit("closeModal");
};

const searchProduct = async (query) => {
  if (query.trim().length === 0) {
    return;
  }

  try {
    const response = await fetch(`http://localhost:8000/api/products?name=${query}`, {
      method: "GET",
      headers: headerGenerator(),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail);
    }

    tableData.value = data.data;
  } catch (err) {
    showErrorAlert(err);
  }
};

const debouncedSearch = debounce(searchProduct, 1000);

watch(searchByProductName, (newValue) => {
  debouncedSearch(newValue);
});

const emit = defineEmits(["closeModal", "addProduct"]);

const addProduct = (product) => {
  closeModal();
  tableData.value = [];
  searchByProductName.value = "";
  emit("addProduct", product);
};

defineExpose({
  openModal,
});
</script>
