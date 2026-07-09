<script setup lang="ts">
import { ref } from "vue";

const emit = defineEmits<{
  (e: "send", text: string): void;
}>();

const text = ref("");

function submit() {
  const value = text.value.trim();
  if (!value) return;

  emit("send", value);
  text.value = "";
}
</script>

<template>
  <div class="bg-white px-3 pb-4 pt-2">
    <div class="mx-auto w-full max-w-3xl">
      <div class="flex h-16 items-center gap-3 rounded-[28px] border border-gray-200 bg-white px-4 py-3 shadow-sm">
        <textarea
          v-model="text"
          rows="1"
          placeholder="Message of type ..."
          class="max-h-40 min-h-7 flex-1 resize-none bg-transparent text-base leading-7 outline-none placeholder:text-gray-400"
          @keydown.enter.exact.prevent="submit"
        />

        <button
          class="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-black text-white disabled:bg-gray-500"
          :disabled="!text.trim()"
          @click="submit"
        >
          &uarr;
        </button>
      </div>

      <p class="pt-2 text-center text-xs text-gray-400">PrivateGPT can make mistakes, so cross-check it.</p>
    </div>
  </div>
</template>
