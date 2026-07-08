<script setup lang="ts">
defineProps<{
  role: "user" | "assistant";
  content: string;
}>();
</script>

<template>
  <div class="flex gap-4 px-8">
    <div
      class="w-12 h-12 rounded-full text-white flex items-center justify-center"
      :class="role === 'assistant' ? 'bg-[#10A37F]' : 'bg-gray-700'"
    >
      {{ role === "assistant" ? "AI" : "U" }}
    </div>

    <div class="prose max-w-none whitespace-pre-wrap">
      <p>{{ content }}</p>
    </div>
  </div>
</template>