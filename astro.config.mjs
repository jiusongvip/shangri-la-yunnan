import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://shangri-la-yunnan.com",
  integrations: [
    tailwind(),
    sitemap({
      serialize(item) {
        item.lastmod = new Date("2026-08-05");
        if (item.url === "https://shangri-la-yunnan.com/") item.priority = 1.0;
        else if (item.url.includes("/attractions/")) item.priority = 0.8;
        else if (item.url.includes("/food/")) item.priority = 0.7;
        else item.priority = 0.5;
        return item;
      },
    }),
  ],
  trailingSlash: "never",
  server: { port: 4321 },
});
