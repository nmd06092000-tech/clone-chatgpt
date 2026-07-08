<script setup lang="ts">
import { ref } from "vue";

const emit = defineEmits<{
  (e: "send", text: string): void;
}>();

const text = ref("");

function submit() {
  const t = text.value.trim();
  if (!t) return;
  emit("send", t);
  text.value = "";
}
</script>

<template>
  <div class="bg-white py-3">
    <div class="max-w-2xl mx-auto">
      <div class="flex items-center justify-between gap-3 border border-gray-200 shadow rounded-3xl px-4 py-1">
        <textarea
          v-model="text"
          rows="1"
          placeholder="Type a message"
          class="flex-1 resize-none outline-none"
          @keydown.enter.exact.prevent="submit"
        />
        <button
          class="w-10 h-10 text-white rounded-full bg-black hover:bg-gray-500"
          @click="submit"
          :disabled="!text.trim()">➤
        </button>

        
       
      </div>
      <span class="flex justify-center text-sm pt-2 text-gray-300">PrivateGPT can make mistakes, so cross-check it.</span>
    </div>
  </div>
</template>