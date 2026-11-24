import { copyFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
const out = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
// Keep the server-way program deterministic and network-free.
mkdirSync(out, { recursive: true });
copyFileSync(join(dirname(new URL(import.meta.url).pathname), 'entry.png'), join(out, 'entry.png'));
