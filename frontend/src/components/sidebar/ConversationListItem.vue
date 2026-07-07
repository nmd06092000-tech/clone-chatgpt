<template>
  <button
    class="
      w-full
      flex
      items-center
      gap-3
      rounded-xl
      px-4
      py-3
      mb-2
      text-left
    "
    :class="
      active
        ? 'bg-gray-200'
        : 'hover:bg-gray-100'
    "
  >
    <span>💬</span>

    <span class="truncate">
      {{ title }}
    </span>
  </button>
</template>

<script setup lang="ts">
defineProps<{
  title: string;
  active: boolean;
}>();
</script>
