<script setup lang="ts">
import { ref } from "vue";

const input = ref("");

const emit = defineEmits<{
  send: [message: string];
}>();

const handleSend = () => {
  if (!input.value.trim()) return;

  emit("send", input.value);

  input.value = "";
};
</script>

<template>

  <div
    class="
    py-8
    px-4
    "
  >

    <div
      class="
      max-w-4xl
      mx-auto
      rounded-full
      bg-white
      shadow
      flex
      items-center
      px-5
      py-3
      "
    >

      <input
        v-model="input"
        class="
        flex-1
        outline-none
        "
        placeholder="Type a message"
        @keyup.enter="handleSend"
      />

      <button
        class="
        w-10
        h-10
        rounded-full
        bg-gray-400
        text-white
        "
        @click="handleSend"
      >
        ↑
      </button>

    </div>

  </div>

</template>