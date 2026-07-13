<template>
  <button
    class="
      w-full
      flex
      items-center
      gap-3
      rounded-xl
      px-4
      py-2
      mb-2
      text-left
      text-sm
    "
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
</template>

<script setup lang="ts">
const props = defineProps<{
  title: string;
  active: boolean;
}>();

const emit = defineEmits<{
  (e: "click-item"): void;
}>();
</script>
