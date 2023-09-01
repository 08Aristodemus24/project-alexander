/** @type {import('tailwindcss').Config} */

import plugin from "preline/plugin.js"

export default {
  content: [
    // "./src/components/**/*.{js,html,svelte}",
    "./src/**/*.{svelte,js}",
    "./node_modules/preline/dist/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [plugin],
  purge: ["./index.html", "./src/**/*.{svelte,js,ts}"], 
}

