<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from "vue";

type AiMode = {
  id: string;
  key: string;
  display_name: string;
};

const aiModes: AiMode[] = [
  {
    id: "00000000-0000-0000-0000-000000000001",
    key: "gpt-4o",
    display_name: "GPT-4o",
  },
  {
    id: "00000000-0000-0000-0000-000000000002",
    key: "gpt-4o-mini",
    display_name: "GPT-4o mini",
  },
  {
    id: "00000000-0000-0000-0000-000000000003",
    key: "reasoning",
    display_name: "Reasoning",
  },
];

const isModelMenuOpen = ref(false);
const selectedAiModeId = ref(aiModes[0].id);
const modelMenuRef = ref<HTMLElement | null>(null);

const selectedAiMode = computed(
  () => aiModes.find((mode) => mode.id === selectedAiModeId.value) ?? aiModes[0],
);

function toggleModelMenu() {
  isModelMenuOpen.value = !isModelMenuOpen.value;
}

function selectAiMode(mode: AiMode) {
  selectedAiModeId.value = mode.id;
  isModelMenuOpen.value = false;
}

function closeModelMenu(event: MouseEvent) {
  const target = event.target as Node;

  if (!modelMenuRef.value?.contains(target)) {
    isModelMenuOpen.value = false;
  }
}

function closeModelMenuOnEscape(event: KeyboardEvent) {
  if (event.key === "Escape") {
    isModelMenuOpen.value = false;
  }
}

onMounted(() => {
  document.addEventListener("click", closeModelMenu);
  document.addEventListener("keydown", closeModelMenuOnEscape);
});

onBeforeUnmount(() => {
  document.removeEventListener("click", closeModelMenu);
  document.removeEventListener("keydown", closeModelMenuOnEscape);
});
</script>

<template>
  <header
    class="flex h-14 items-center justify-between border-b border-gray-200 px-8 py-2 shadow"
  >
    <div ref="modelMenuRef" class="relative">
      <button
        class="group flex items-center gap-2 rounded-lg px-2.5 py-2 text-left transition hover:bg-gray-100"
        type="button"
        :aria-expanded="isModelMenuOpen"
        aria-haspopup="menu"
        @click="toggleModelMenu"
      >
        <span class="text-base font-semibold text-gray-900">
          {{ selectedAiMode.display_name }}
        </span>

        <svg
          class="h-4 w-4 text-gray-400 transition group-hover:text-gray-700"
          :class="isModelMenuOpen ? 'rotate-180' : ''"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path d="m6 9 6 6 6-6" />
        </svg>
      </button>

      <div
        v-if="isModelMenuOpen"
        class="absolute left-0 top-full z-20 mt-2 w-72 overflow-hidden rounded-xl border border-gray-200 bg-white p-1.5 shadow-xl"
        role="menu"
      >
        <button
          v-for="mode in aiModes"
          :key="mode.id"
          class="flex w-full items-center justify-between gap-3 rounded-lg px-3 py-2.5 text-left transition hover:bg-gray-100"
          :class="selectedAiModeId === mode.id ? 'bg-gray-100' : ''"
          type="button"
          role="menuitem"
          @click="selectAiMode(mode)"
        >
          <span class="min-w-0">
            <span class="block truncate text-sm font-medium text-gray-900">
              {{ mode.display_name }}
            </span>
            <span class="block truncate text-xs text-gray-500">
              {{ mode.key }}
            </span>
          </span>

          <svg
            v-if="selectedAiModeId === mode.id"
            class="h-4 w-4 shrink-0 text-gray-800"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <path d="m20 6-11 11-5-5" />
          </svg>
        </button>
      </div>
    </div>

    <button class="group flex h-10 items-center gap-2 rounded-full border border-gray-200 bg-white px-3.5 text-sm font-medium text-gray-800 shadow-sm transition hover:border-gray-300 hover:bg-gray-50 hover:shadow">
      <svg class="h-4 w-4 text-gray-700 transition group-hover:text-black" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 3H6a3 3 0 0 0-3 3v12a3 3 0 0 0 3 3h12a3 3 0 0 0 3-3v-6" />
        <path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L11 15l-4 1 1-4 8.5-8.5z" />
      </svg>

      <span>New chat</span>
    </button>
  </header>
</template>
