<script setup lang="ts">
import { ref } from "vue";
import ChatHeader from "./ChatHeader.vue";
import ChatBody from "./ChatBody.vue";
import ChatComposer from "./ChatComposer.vue";
import { computed } from "vue";
import EmptyState from "./EmptyState.vue";

type UiMessage = { role: "user" | "assistant"; content: string };

const props = defineProps<{
  messages: UiMessage[];
}>();

const emit = defineEmits<{
  (e: "send", text: string): void;
  (e: "new-chat"): void;
}>();

const isEmptyChat = computed(() => props.messages.length === 0);

</script>

<template>
  <div class="h-screen flex flex-col">
    <ChatHeader @new-chat="emit('new-chat')" />
    
    <div v-if="isEmptyChat" class="flex flex-1 items-center justify-center px-4">
      <div class="w-full max-w-3xl">
        <EmptyState title="What can I help with?" />
        <div class="mt-8">
          <ChatComposer @send="emit('send', $event)" />
        </div>
      </div>
    </div>
  <template v-else>
    <ChatBody class="flex-1 overflow-hidden" :messages="messages" />
    <ChatComposer @send="emit('send', $event)" />
  </template>
  </div>
</template>