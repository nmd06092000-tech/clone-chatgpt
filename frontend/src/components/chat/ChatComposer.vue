<template>
  <div class=" bg-white py-3">
    <div class="max-w-4xl mx-auto">
      <div class="flex items-center gap-3 border rounded-2xl px-5 py-2">
        <textarea
          rows="1"
          placeholder="Message..."
          class="
            flex-1
            resize-none
            outline-none
          "
        />

        <button
          class="
            w-12
            h-12
            rounded-xl
            bg-gray-200
            hover:bg-gray-300
          "
        >
          ➤
        </button>
      </div>

      <p
        class="
          text-center
          text-sm
          text-gray-400
          mt-3
        "
      >
        Chat can make mistakes. Check important info.
      </p>
    </div>
  </div>
</template>