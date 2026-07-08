<script setup lang="ts">
import { ref } from "vue";
import ChatHeader from "./ChatHeader.vue";
import ChatBody from "./ChatBody.vue";
import ChatComposer from "./ChatComposer.vue";

type UiMessage = { role: "user" | "assistant"; content: string };
const messages = ref<UiMessage[]>([]);

function handleSend(text: string) {
  messages.value.push({ role: "user", content: text });
  messages.value.push({ role: "assistant", content: "OK, mình đã nhận: " + text });
}
</script>

<template>
  <div class="h-screen flex flex-col">
    <ChatHeader />
    <ChatBody class="flex-1 overflow-hidden" :messages="messages" />
    <ChatComposer @send="handleSend" />
  </div>
</template>