<script setup lang="ts">
import EmptyState from "./EmptyState.vue";
import ChatMessage from "./ChatMessage.vue";

import type {
  Message,
} from "@/types/chat";

defineProps<{
  messages: Message[];
}>();
</script>

<template>

  <main
    class="
    flex-1
    overflow-y-auto
    "
  >

    <EmptyState
      v-if="messages.length === 0"
      title="Hello, how can I assist you today?"
    />

    <div v-else>

      <ChatMessage
        v-for="message in messages"
        :key="message.id"
        :message="message"
      />

    </div>

  </main>

</template>