<script setup lang="ts">
import SidebarHeader from "./SidebarHeader.vue";
import ConversationList from "./ConversationList.vue";

defineProps<{
  conversations: any[];
}>();

const emit = defineEmits([
  "select"
]);
</script>

<template>
  <aside
    class="
      w-[320px]
      min-w-[320px]
      border-r
      bg-[#f3f3f3]
      flex
      flex-col
    "
  >
    <SidebarHeader />

    <ConversationList
      :conversations="conversations"
      @select="emit('select', $event)"
    />
  </aside>
</template>