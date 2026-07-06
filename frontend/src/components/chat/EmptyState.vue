<script setup lang="ts">

defineProps<{
  title: string;
}>();

</script>

<template>

  <div class="text-center">

    <h1
      class="
      text-5xl
      font-light
      "
    >
      {{ title }}
    </h1>

  </div>

</template>