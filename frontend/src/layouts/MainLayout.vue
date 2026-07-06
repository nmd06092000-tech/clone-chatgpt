<script setup lang="ts">
import { ref, onMounted } from "vue";

import Sidebar from "../components/sidebar/Sidebar.vue";
import ChatHeader from "../components/chat/ChatHeader.vue";
import ChatWindow from "../components/chat/ChatWindow.vue";
import ChatInput from "../components/chat/ChatInput.vue";

import { getConversations } from "../services/conversation.service";
import { getMessages } from "../services/message.service";

const sidebarOpen = ref(true);

const conversations = ref<any[]>([]);
const messages = ref<any[]>([]);

onMounted(async () => {
  try {
    conversations.value = await getConversations();
  } catch (error) {
    console.error(error);
  }
});

const handleConversationSelect = async (
  conversationId: number
) => {
  try {
    messages.value = await getMessages(
      conversationId
    );
  } catch (error) {
    console.error(error);
  }
};

const handleSend = (
  message: string
) => {
  console.log(message);
};
</script>

<template>
  <div class="flex h-screen">

    <!-- Sidebar -->
    <Sidebar
      v-show="sidebarOpen"
      :conversations="conversations"
      @select="handleConversationSelect"
    />

    <!-- Main Content -->
    <div
      class="flex flex-1 flex-col"
    >

      <ChatHeader
        model-name="GPT-5.2"
        @toggle-sidebar="
          sidebarOpen = !sidebarOpen
        "
      />

      <ChatWindow
        :messages="messages"
      />

      <ChatInput
        @send="handleSend"
      />

    </div>

  </div>
</template>