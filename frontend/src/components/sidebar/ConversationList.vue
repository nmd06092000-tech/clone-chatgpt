<script setup lang="ts">
import ConversationListItem from "./ConversationListItem.vue";
import type { Conversation } from "../../types/chat.ts";

const props = defineProps<{
  conversations: Conversation[];
  activeConversationId: string;
}>();

const emit = defineEmits<{
  (e: "select-conversation", id: string): void;
  (e: "delete-conversation", id: string): void;
}>();

function handleDelete(id: string) {
  emit('delete-conversation', id);
}
</script>

<template>
  <div class="px-4 pb-4">
    <h3
      class="
        text-xs
        font-semibold
        text-gray-400
        uppercase
        mb-4
      "
    >
      Recent
    </h3>

    <ConversationListItem
      v-for="chat in conversations"
      :key="chat.id"
      :title="chat.title"
      :active="chat.id === activeConversationId"
      :id="chat.id"
      @click="$emit('select-conversation', chat.id)"
      @delete-item="handleDelete"
    />
  </div>
</template>

