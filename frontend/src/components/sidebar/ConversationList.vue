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
      v-for="chat in chats"
      :key="chat.id"
      :title="chat.title"
      :active="chat.active"
    />
  </div>
</template>

<script setup lang="ts">
import ConversationListItem from "./ConversationListItem.vue";

const chats = [
  
];
</script>