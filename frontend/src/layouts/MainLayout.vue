<script setup lang="ts">
import SidebarShell from "../components/sidebar/SidebarShell.vue";
import ChatPanel from "../components/chat/ChatPanel.vue";
</script>

<template>
  <div class="h-screen flex bg-white">
    <SidebarShell />

    <main class="flex-1">
      <ChatPanel />
    </main>
  </div>
</template>

