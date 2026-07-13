<script setup lang="ts">
import { ref } from "vue";
import SidebarShell from "../components/sidebar/SidebarShell.vue";
import ChatPanel from "../components/chat/ChatPanel.vue";

type UiMessage = { role: "user" | "assistant"; content: string };

const messages = ref <UiMessage[]>([]);

function handleSend(text: string) {
  messages.value.push({ role:"user", content:text});
  messages.value.push({ role:"assistant", content:"OK, mình đã nhận: " + text });
}

function handleNewChat() {
  messages.value = [];
}
</script>

<template>
  <div class="h-screen flex bg-white">
    <SidebarShell @new-chat="handleNewChat" />

    <main class="flex-1">
      <ChatPanel 
      :messages="messages"
      @send="handleSend"
      @new-chat="handleNewChat"
      />
    </main>
  </div>
</template>

