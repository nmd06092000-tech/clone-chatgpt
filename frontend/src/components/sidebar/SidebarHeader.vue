<script setup lang="ts">
defineProps<{
  collapsed: boolean;
}>();

defineEmits<{
  (e: "toggle"): void;
}>();
</script>

<template>
  <div class="space-y-2 p-2">
    <div class="flex h-10 items-center justify-between">
      <div class="flex min-w-0 items-center gap-2">
        <span v-if="!collapsed" class="truncate text-xl font-semibold text-gray-900">ChatGPT</span>
      </div>

      <button class="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg text-gray-500 transition hover:bg-gray-100 hover:text-gray-900" type="button" :aria-label="collapsed ? 'Open sidebar' : 'Close sidebar'" @click="$emit('toggle')">
        <svg v-if="!collapsed" class="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4 5h16" />
          <path d="M4 12h10" />
          <path d="M4 19h16" />
        </svg>

        <svg v-else class="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4 5h16" />
          <path d="M10 12h10" />
          <path d="M4 19h16" />
        </svg>
      </button>
    </div>

    <button class="flex h-10 w-full items-center gap-3 rounded-xl px-2.5 text-sm font-medium text-gray-800 transition hover:bg-gray-100" type="button" :class="collapsed ? 'justify-center px-0' : 'justify-start'">
      <svg class="h-4 w-4 shrink-0 text-gray-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 3H6a3 3 0 0 0-3 3v12a3 3 0 0 0 3 3h12a3 3 0 0 0 3-3v-6" />
        <path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L11 15l-4 1 1-4 8.5-8.5z" />
      </svg>

      <span v-if="!collapsed" class="truncate">New chat</span>
    </button>
  </div>
</template>
