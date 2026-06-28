// Copia los datos canónicos de ../app-data a public/app-data para que el build
// de Vite los incluya y Workbox pueda cachearlos (PWA 100% offline).
// La fuente de verdad sigue siendo la carpeta raíz app-data/.
import { cp, mkdir, rm, stat } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const SRC = resolve(__dirname, '..', '..', 'app-data');
const DEST = resolve(__dirname, '..', 'public', 'app-data');

const FILES = ['content.json', 'references.json', 'questions.json', 'content.md'];

async function main() {
  if (!existsSync(SRC)) {
    console.error(`[sync-data] No se encuentra la carpeta de datos: ${SRC}`);
    process.exit(1);
  }
  await rm(DEST, { recursive: true, force: true });
  await mkdir(DEST, { recursive: true });
  for (const f of FILES) {
    const from = resolve(SRC, f);
    if (!existsSync(from)) {
      console.error(`[sync-data] Falta el archivo requerido: ${from}`);
      process.exit(1);
    }
    await cp(from, resolve(DEST, f));
    const { size } = await stat(from);
    console.log(`[sync-data] ${f} (${(size / 1024).toFixed(0)} kB)`);
  }
  console.log(`[sync-data] OK → ${DEST}`);
}

main().catch((err) => {
  console.error('[sync-data] Error:', err);
  process.exit(1);
});
