<script setup lang="ts">
const emit = defineEmits([
  "toggle-sidebar"
]);

defineProps<{
  modelName: string;
}>();
</script>

<template>
  <header
    class="
    h-16
    px-4
    flex
    items-center
    justify-between
    "
  >

    <button
      class="text-2xl lg:hidden"
      @click="emit('toggle-sidebar')"
    >
      ☰
    </button>

    <div class="flex-1 text-center text-2xl">
      {{ modelName }}
    </div>

    <div class="w-8" />

  </header>
</template>