<script setup lang="ts">
import { computed, ref } from "vue";

type User = {
  name: string;
  email?: string;
  avatarUrl?: string;
};

type MenuItem = {
  label: string;
  danger?: boolean;
};

const props = defineProps<{
  user?: User;
}>();

const isOpen = ref(false);

const menuItems: MenuItem[] = [
  { label: "My profile" },
  { label: "Settings" },
  { label: "Privacy policy" },
  { label: "Share feedback" },
  { label: "Sign out", danger: true },
];

const displayName = computed(() => props.user?.name || "Guest");
const displayEmail = computed(() => props.user?.email || "Email");

const initials = computed(() => {
  const name = displayName.value.trim();
  if (!name) return "G";

  return name
    .split(" ")
    .map((part) => part[0])
    .join("")
    .slice(0, 2)
    .toUpperCase();
});

function toggleMenu() {
  isOpen.value = !isOpen.value;
}
</script>

<template>
  <div class="relative p-2">
    <div v-if="isOpen" class="absolute bottom-full left-2 right-2 mb-2 overflow-hidden rounded-xl border border-gray-200 bg-white py-1 shadow-lg">
      <button v-for="item in menuItems" :key="item.label" class="flex w-full items-center px-3 py-2 text-left text-sm transition" :class="item.danger ? 'text-red-600 hover:bg-red-50' : 'text-gray-700 hover:bg-gray-100'" type="button">
        {{ item.label }}
      </button>
    </div>

    <button class="flex w-full items-center justify-between rounded-xl bg-white p-2 text-left transition hover:bg-gray-100" type="button" :aria-expanded="isOpen" @click="toggleMenu">
      <div class="flex min-w-0 items-center gap-3">
        <img v-if="user?.avatarUrl" :src="user.avatarUrl" :alt="displayName" class="h-9 w-9 shrink-0 rounded-full object-cover" />

        <div v-else class="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-gray-700 text-sm font-semibold text-white">
          {{ initials }}
        </div>

        <div class="min-w-0">
          <p class="truncate text-sm font-medium text-gray-900">{{ displayName }}</p>
          <p class="truncate text-xs text-gray-500">{{ displayEmail }}</p>
        </div>
      </div>

      <svg class="h-4 w-4 shrink-0 text-gray-400 transition" :class="isOpen ? 'rotate-180' : ''" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="m6 9 6 6 6-6" />
      </svg>
    </button>
  </div>
</template>
