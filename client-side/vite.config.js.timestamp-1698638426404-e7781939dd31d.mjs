// vite.config.js
import { defineConfig } from "file:///D:/Projects/To%20Github/project-alexander/client-side/node_modules/vite/dist/node/index.js";
import { svelte } from "file:///D:/Projects/To%20Github/project-alexander/client-side/node_modules/@sveltejs/vite-plugin-svelte/src/index.js";
var vite_config_default = defineConfig({
  plugins: [svelte()],
  ssr: {
    noExternal: ["three"]
  }
});
export {
  vite_config_default as default
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsidml0ZS5jb25maWcuanMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImNvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9kaXJuYW1lID0gXCJEOlxcXFxQcm9qZWN0c1xcXFxUbyBHaXRodWJcXFxccHJvamVjdC1hbGV4YW5kZXJcXFxcY2xpZW50LXNpZGVcIjtjb25zdCBfX3ZpdGVfaW5qZWN0ZWRfb3JpZ2luYWxfZmlsZW5hbWUgPSBcIkQ6XFxcXFByb2plY3RzXFxcXFRvIEdpdGh1YlxcXFxwcm9qZWN0LWFsZXhhbmRlclxcXFxjbGllbnQtc2lkZVxcXFx2aXRlLmNvbmZpZy5qc1wiO2NvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9pbXBvcnRfbWV0YV91cmwgPSBcImZpbGU6Ly8vRDovUHJvamVjdHMvVG8lMjBHaXRodWIvcHJvamVjdC1hbGV4YW5kZXIvY2xpZW50LXNpZGUvdml0ZS5jb25maWcuanNcIjtpbXBvcnQgeyBkZWZpbmVDb25maWcgfSBmcm9tICd2aXRlJ1xuaW1wb3J0IHsgc3ZlbHRlIH0gZnJvbSAnQHN2ZWx0ZWpzL3ZpdGUtcGx1Z2luLXN2ZWx0ZSdcblxuLy8gaHR0cHM6Ly92aXRlanMuZGV2L2NvbmZpZy9cbmV4cG9ydCBkZWZhdWx0IGRlZmluZUNvbmZpZyh7XG4gIHBsdWdpbnM6IFtzdmVsdGUoKV0sXG4gIHNzcjoge1xuICAgIG5vRXh0ZXJuYWw6IFsndGhyZWUnXVxuICB9XG59KVxuIl0sCiAgIm1hcHBpbmdzIjogIjtBQUF1VixTQUFTLG9CQUFvQjtBQUNwWCxTQUFTLGNBQWM7QUFHdkIsSUFBTyxzQkFBUSxhQUFhO0FBQUEsRUFDMUIsU0FBUyxDQUFDLE9BQU8sQ0FBQztBQUFBLEVBQ2xCLEtBQUs7QUFBQSxJQUNILFlBQVksQ0FBQyxPQUFPO0FBQUEsRUFDdEI7QUFDRixDQUFDOyIsCiAgIm5hbWVzIjogW10KfQo=