<script setup lang="ts">

defineProps<{
  conversations: any[];
}>();

const emit = defineEmits([
  "select"
]);

</script>

<template>

  <div
    v-for="conversation in conversations"
    :key="conversation.id"
    @click="
      emit(
        'select',
        conversation.id
      )
    "
  >
    {{ conversation.title }}
  </div>

</template>