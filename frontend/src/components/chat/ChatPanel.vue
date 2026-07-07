<script setup lang="ts">
import ChatHeader from "./ChatHeader.vue";
import ChatBody from "./ChatBody.vue";
import ChatComposer from "./ChatComposer.vue";
</script>

<template>
  <div class="h-screen flex flex-col">
    <ChatHeader />

    <ChatBody class="flex-1 overflow-hidden" />

    <ChatComposer />
  </div>
</template>

