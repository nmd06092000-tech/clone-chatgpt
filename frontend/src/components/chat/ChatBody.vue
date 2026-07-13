<script setup lang="ts">
import MessageItem from "./MessageItem.vue";
import type { Message } from "../../types/chat.ts";

defineProps<{
  messages: Message[];
}>();
</script>

<template>
  <div class="flex-1 overflow-y-auto">
    <div class="max-w-3xl mx-auto w-full py-10 px-8 space-y-6">
      <MessageItem
        v-for="(m, idx) in messages"
        :key= "idx"
        :role= "m.role"
        :content="m.content"
      />
    </div>
  </div>
</template>