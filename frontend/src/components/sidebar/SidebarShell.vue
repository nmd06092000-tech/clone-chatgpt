<template>
  <aside
    class="
      w-[220px]
      min-w-[220px]
      border-r
      border-gray-200
      bg-[#f9fafb]
      flex
      flex-col
    "
  >
    <SidebarHeader />

    <ConversationList class="flex-1 overflow-y-auto" />

    <SidebarProfile />
  </aside>
</template>

<script setup lang="ts">
import SidebarHeader from "./SidebarHeader.vue";
import ConversationList from "./ConversationList.vue";
import SidebarProfile from "./SidebarProfile.vue";
</script>