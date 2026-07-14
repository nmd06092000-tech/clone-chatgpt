<template>
  <div class="relative pr-10">
  <button
    class="w-full flex items-center gap-3 rounded-xl px-4 py-2 mb-2 text-left text-sm"
    :class="
      active
        ? 'bg-gray-200'
        : 'hover:bg-gray-100'
    "
    @click="emit('click-item')"
  >
    <span class="truncate">
      {{ title }}
    </span>
  </button>

  <button class="absolute right-2 top-1/2 -translate-y-1/2"
          @click.stop="toggleMenu"
  >
    &#8942;
  </button>

  <div
  v-if="showMenu"
  class="absolute right-2 top-1/2 -translate-y-1/2 mt-8 w-35 bg-white border border-gray-300 rounded-2xl shadow-xl z-50"
  >
  <button
   class="flex w-full items-center gap-3 rounded-xl px-3 py-2 text-sm font-medium text-red-600 hover:bg-gray-50"
   @click.stop="handleDelete">Delete
  </button>

  </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
const props = defineProps<{
  title: string;
  active: boolean;
  id: string;
}>();

const emit = defineEmits<{
  (e: "click-item"): void;
  (e: "delete-item", id: string): void;
}>();

const showMenu = ref(false);

function toggleMenu() {
  showMenu.value = !showMenu.value;
}

function handleDelete() {
  emit('delete-item', props.id);
  showMenu.value = false;
}
</script>
