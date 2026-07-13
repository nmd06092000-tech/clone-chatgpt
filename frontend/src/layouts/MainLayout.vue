<script setup lang="ts">
import { computed, ref } from "vue";
import SidebarShell from "../components/sidebar/SidebarShell.vue";
import ChatPanel from "../components/chat/ChatPanel.vue";
import type { Conversation } from "../types/chat";

function createId() {
  return (
    globalThis.crypto?.randomUUID?.() ??
    `id-${Date.now()}-${Math.floor(Math.random() * 10000)}`
  )
}

function builTitleFromText(text: string) {
  const trimmed = text.trim();
  if (!trimmed) return "New chat";
  return trimmed.length > 40 ? `${trimmed.slice(0, 37)}...` : trimmed;
}

const userId = "11111111-1111-1111-1111-111111111111";
const aiModeId = "22222222-2222-2222-2222-222222222222";

const conversations = ref<Conversation[]>([
  {
    id: "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
    user_id: userId,
    ai_mode_id: aiModeId,
    title: "Học Vue cơ bản",
    last_message_at: "2026-07-13T09:00:00.000Z",
    created_at: "2026-07-13T08:00:00.000Z",
    updated_at: "2026-07-13T09:00:00.000Z",
    messages: [
      {
        id: "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
        conversation_id: "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
        role: "assistant",
        content: "Chào bạn, mình có thể giúp gì hôm nay?",
        sequence_no: 1,
        created_at: "2026-07-13T08:00:00.000Z",
      },
      {
        id: "cccccccc-cccc-cccc-cccc-cccccccccccc",
        conversation_id: "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
        role: "user",
        content: "Giải thích Vue cho mình",
        sequence_no: 2,
        created_at: "2026-07-13T08:05:00.000Z",
      },
    ],
  },
  {
    id: "dddddddd-dddd-dddd-dddd-dddddddddddd",
    user_id: userId,
    ai_mode_id: aiModeId,
    title: "Kế hoạch cuối tuần",
    last_message_at: "2026-07-13T10:00:00.000Z",
    created_at: "2026-07-13T09:30:00.000Z",
    updated_at: "2026-07-13T10:00:00.000Z",
    messages: [
      {
        id: "eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee",
        conversation_id: "dddddddd-dddd-dddd-dddd-dddddddddddd",
        role: "assistant",
        content: "Bạn có thể học thêm một kỹ năng mới hoặc đi dạo.",
        sequence_no: 1,
        created_at: "2026-07-13T09:30:00.000Z",
      },
      {
        id: "ffffffff-ffff-ffff-ffff-ffffffffffff",
        conversation_id: "dddddddd-dddd-dddd-dddd-dddddddddddd",
        role: "user",
        content: "Mình nên làm gì cuối tuần?",
        sequence_no: 2,
        created_at: "2026-07-13T10:00:00.000Z",
      },
    ],
  },
]);

const activeConversationId = ref<string>(conversations.value[0].id);

const activeConversation = computed(() =>
  conversations.value.find((c) => c.id === activeConversationId.value)
);

const activeMessages = computed<Message[]>(() => activeConversation.value?.messages ?? []);

function selectConversation(id: string) {
  activeConversationId.value = id;
}

function handleSend(text: string) {
  const target = conversations.value.find(
    (c) => c.id === activeConversationId.value
  );

  if (!target) return;

  const now = new Date().toISOString();
  const nextSequence = target.messages.length + 1;

  target.messages.push({
    id: createId(),
    conversation_id: target.id,
    role: "user",
    content: text,
    sequence_no: nextSequence,
    created_at: now,
  });

  target.messages.push({
    id: createId(),
    conversation_id: target.id,
    role: "assistant",
    content: `Đã nhận: ${text}`,
    sequence_no: nextSequence + 1,
    created_at: now,
  });

  if (!target.title || target.title === "New chat") {
    target.title = builTitleFromText(text);
  }

  target.last_message_at = now;
  target.updated_at = now;
}

function handleNewChat() {
  const now = new Date().toISOString();

  const newConversation: Conversation = {
    id: createId(),
    user_id: userId,
    ai_mode_id: aiModeId,
    title: "New chat",
    last_message_at: now,
    created_at: now,
    updated_at: now,
    messages: [],
  };

  conversations.value.unshift(newConversation);
  activeConversationId.value = newConversation.id;
}
</script>

<template>
  <div class="flex h-screen bg-white">
    <SidebarShell
      :conversations="conversations"
      :active-conversation-id="activeConversationId"
      @select-conversation="selectConversation"
      @new-chat="handleNewChat"
    />

    <main class="flex-1">
      <ChatPanel
        :messages="activeMessages"
        @send="handleSend"
        @new-chat="handleNewChat"
      />
    </main>
  </div>
</template>