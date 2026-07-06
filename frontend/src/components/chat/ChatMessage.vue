<script setup lang="ts">
import type {
  Message,
} from "@/types/chat";

defineProps<{
  message: Message;
}>();
</script>

<template>

  <div
    class="
    max-w-4xl
    mx-auto
    py-4
    "
  >

    <div
      class="font-semibold mb-2"
    >
      {{ message.role }}
    </div>

    <div
      class="leading-7"
    >
      {{ message.content }}
    </div>

  </div>

</template>