<script setup lang="ts">
import ConversationListItem from "./ConversationListItem.vue";
import type { Conversation } from "../../types/chat.ts";
import { computed } from "vue";

type TimeGroup = "Today" | "Yesterday" | "Last 7 days" | "Last 30 days";

function getTimeGroup(timestamp: string): TimeGroup {
  const now = new Date();
  const todayStart = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  const yesterdayStart = new Date(todayStart);
  yesterdayStart.setDate(todayStart.getDate() - 1);
  const last7DaysStart = new Date(todayStart);
  last7DaysStart.setDate(todayStart.getDate() - 7);
  const last30DaysStart = new Date(todayStart);
  last30DaysStart.setDate(todayStart.getDate() - 29);

  const itemDate = new Date(timestamp);

  if (itemDate >= todayStart) {
    return "Today";
  } else if (itemDate >= yesterdayStart) {
    return "Yesterday";
  } else if (itemDate >= last7DaysStart) {
    return "Last 7 days";
  } else {
    return "Last 30 days";
  }
}
  function groupConversations(conversations: Conversation[]): GroupedConversations {
    const groups: GroupedConversations = {
      "today": [],
      "yesterday": [],
      "last7Days": [],
      "last30Days": []
    };
    for (const conversation of conversations) {
      const group = getTimeGroup(conversation.last_message_at);
      
      if (group === "Today") groups.today.push(conversation);
      else if (group === "Yesterday") groups.yesterday.push(conversation);
      else if (group === "Last 7 days") groups.last7Days.push(conversation);
      else if (group === "Last 30 days") groups.last30Days.push(conversation);
    }

    

    return groups;
  }



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

const groups = computed(() => groupConversations(props.conversations));
const groupSections = computed(() => [
  { label: "Today", items: groups.value.today },
  { label: "Yesterday", items: groups.value.yesterday },
  { label: "Last 7 days", items: groups.value.last7Days },
  { label: "Last 30 days", items: groups.value.last30Days },
]);
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
<template v-for ="section in groupSections" :key="section.label">
    <div v-if="section.items.length > 0" class="mb-4">
      <div class="mb-2 text-xs font-semibold uppercase text-gray-500">
        {{ section.label }}
      </div>
      <ConversationListItem
      v-for="chat in section.items"
      :key="chat.id"
      :title="chat.title"
      :active="chat.id === activeConversationId"
      :id="chat.id"
      @click="$emit('select-conversation', chat.id)"
      @delete-item="handleDelete"
    />
    </div>
</template>
  </div>
</template>

