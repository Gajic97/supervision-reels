// Renderuje HTML kompoziciju (window.render(t), window.ready) u frejmove pa u MP4 sa zvukom.
// Upotreba: node scripts/render.js <dir-sa-index.html> <audio.wav> <izlaz.mp4> [trajanje=21] [poster_t=7.9]
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

(async () => {
  const [dir, audio, out, durArg, posterArg] = process.argv.slice(2);
  const FPS = 30, DUR = Number(durArg || 21), N = Math.round(FPS * DUR), POSTER = Number(posterArg || 7.9);
  const frames = path.join(dir, 'frames');
  fs.rmSync(frames, { recursive: true, force: true }); fs.mkdirSync(frames, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.resolve(dir, 'index.html'));
  await p.evaluate(() => window.ready);
  for (let f = 0; f < N; f++) {
    // frejm 0 = poster (najjači smiren kadar), da ga sve platforme prikažu kao thumbnail
    const t = f === 0 ? POSTER : f / FPS;
    await p.evaluate(t => render(t), t);
    await p.screenshot({ path: path.join(frames, `f${String(f).padStart(4, '0')}.jpg`), type: 'jpeg', quality: 94 });
  }
  await b.close();
  fs.copyFileSync(path.join(frames, 'f0000.jpg'), out.replace(/\.mp4$/, '.jpg'));
  execFileSync('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', '-framerate', String(FPS), '-i', path.join(frames, 'f%04d.jpg'),
    '-i', audio, '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p',
    '-profile:v', 'high', '-r', String(FPS), '-c:a', 'aac', '-b:a', '192k', '-ar', '44100', '-shortest', '-movflags', '+faststart', out], { stdio: 'inherit' });
  console.log('OK', out);
})();
