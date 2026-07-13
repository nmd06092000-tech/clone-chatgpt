<script setup lang="ts">
defineProps<{
  role: "user" | "assistant" | "system";
  content: string;
}>();
</script>

<template>
  <div class="max-w-[80%] rounded-xl px-4 py-2"
       :class="role === 'user' ? 'ml-auto bg-gray-100 ' : 'bg-gray-100 text-gray-800'"
       >
       {{ content }}
  </div>
</template>