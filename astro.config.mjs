import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://shangri-la-yunnan.com",
  integrations: [tailwind(), sitemap()],
  trailingSlash: "never",
  server: { port: 4321 },
});
