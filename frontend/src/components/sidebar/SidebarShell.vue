<script setup lang="ts">
import { ref } from "vue";
import SidebarHeader from "./SidebarHeader.vue";
import ConversationList from "./ConversationList.vue";
import SidebarProfile from "./SidebarProfile.vue";

const isCollapsed = ref(false);

const currentUser = {
  name: "Your Name",
  email: "nmd0609",
  avatarUrl: "",
};

const emit = defineEmits<{
  (e: 'new-chat'): void;
}>();
</script>

<template>
  <aside
    class="flex h-screen shrink-0 flex-col border-r border-gray-200 bg-[#f9fafb] transition-all duration-200"
    :class="isCollapsed ? 'w-[64px]' : 'w-[220px]'"
  >
    <SidebarHeader :collapsed="isCollapsed"
                    @toggle="isCollapsed = !isCollapsed"
                    @new-chat="$emit('new-chat')"
    />

    <ConversationList v-if="!isCollapsed" class="flex-1 overflow-y-auto" />

    <SidebarProfile v-if="!isCollapsed" :user="currentUser" />
  </aside>
</template>
