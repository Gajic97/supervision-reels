"""SuperVision reel audio v2 — modern house bed + cinematic/UI sound design (no chiptune blips)."""
import os
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile

SR = 44100
DUR = 21.0
BEAT = 0.5  # 120 BPM
N = int(SR * DUR)
rng = np.random.default_rng(11)

def sos(kind, f, o=2): return butter(o, f, kind, fs=SR, output='sos')
def lp(x, f, o=2): return sosfilt(sos('low', f, o), x)
def hp(x, f, o=2): return sosfilt(sos('high', f, o), x)
def bp(x, f1, f2, o=2): return sosfilt(sos('band', [f1, f2], o), x)
def mhz(m): return 440 * 2 ** ((m - 69) / 12)
def tt(n): return np.arange(n) / SR
def noise(n): return rng.standard_normal(n)

class Bus:
    def __init__(s): s.L = np.zeros(N); s.R = np.zeros(N)
    def add(s, sig, t0, g=1.0, pan=0.0):
        i = int(round(t0 * SR))
        if i < 0: sig = sig[-i:]; i = 0
        if i >= N: return
        x = sig[: N - i] * g
        if x.ndim == 2:
            s.L[i:i+len(x)] += x[:, 0]; s.R[i:i+len(x)] += x[:, 1]; return
        gl = np.cos((pan + 1) * np.pi / 4) * 1.414; gr = np.sin((pan + 1) * np.pi / 4) * 1.414
        s.L[i:i+len(x)] += x * gl; s.R[i:i+len(x)] += x * gr

music, drums, sfx, send = Bus(), Bus(), Bus(), Bus()

# ---------- reverb IR ----------
def make_ir(length=2.2, decay=0.55, pre=0.018, damp=6000):
    n = int(length * SR); t = tt(n)
    irs = []
    for _ in range(2):
        x = noise(n) * np.exp(-t / decay)
        x = lp(x, damp) ; x = hp(x, 180)
        x = np.concatenate([np.zeros(int(pre * SR)), x])
        irs.append(x / np.sqrt((x ** 2).sum()))
    return irs
IR = make_ir()

# ---------- drums ----------
def kick():
    n = int(0.42 * SR); t = tt(n)
    f = 46 + 120 * np.exp(-t / 0.028)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.2)
    s = np.tanh(s * 2.2) / np.tanh(2.2)
    click = hp(noise(n), 2500) * np.exp(-t / 0.003) * 0.35
    return s + click

def clap():
    n = int(0.35 * SR); t = tt(n); x = np.zeros(n)
    for k, off in enumerate([0, 0.009, 0.019, 0.03]):
        i = int(off * SR); m = n - i
        x[i:] += noise(m) * np.exp(-tt(m) / (0.012 if k < 3 else 0.09))
    return bp(x, 1000, 4200) * 0.8

def hat(open_=False):
    n = int((0.28 if open_ else 0.07) * SR); t = tt(n)
    met = sum(np.sign(np.sin(2 * np.pi * f * t)) for f in [205.3, 304.4, 369.6, 522.7, 540, 800])
    x = hp(met * 0.3 + noise(n), 7500, 3)
    return x * np.exp(-t / (0.09 if open_ else 0.016)) * 0.6

def shaker():
    n = int(0.09 * SR); t = tt(n)
    e = (1 - np.exp(-t / 0.01)) * np.exp(-t / 0.03)
    return bp(noise(n), 5000, 12000) * e

# ---------- music ----------
def supersaw(f, n, voices=7, spread=0.12):
    t = tt(n); out = np.zeros(n)
    for v in range(voices):
        d = (v - (voices - 1) / 2) / ((voices - 1) / 2) * spread
        ff = f * 2 ** (d / 12); ph = rng.random()
        out += 2 * ((t * ff + ph) % 1) - 1
    return out / voices

def pad_chord(notes, length, cutoff):
    n = int(length * SR)
    l = np.zeros(n); r = np.zeros(n)
    for i, m in enumerate(notes):
        a = supersaw(mhz(m), n); b = supersaw(mhz(m) * 1.002, n)
        l += a; r += b
    l, r = lp(l, cutoff, 2), lp(r, cutoff, 2)
    att = np.minimum(1, tt(n) / 0.35); rel = np.minimum(1, (n - np.arange(n)) / (0.25 * SR))
    env = att * rel
    return np.stack([l * env, r * env], 1) / len(notes)

def sub_bass(m, length):
    n = int(length * SR); t = tt(n); f = mhz(m)
    s = np.sin(2 * np.pi * f * t) + 0.18 * np.sin(4 * np.pi * f * t)
    s = np.tanh(s * 1.6)
    env = np.minimum(1, t / 0.006) * np.exp(-t / (length * 0.8))
    return lp(s, 900) * env

CHORDS = [[57, 60, 64, 67, 71], [53, 57, 60, 64, 69], [48, 55, 59, 62, 64], [55, 59, 62, 64, 67]]  # Am9 Fmaj7 Cmaj9 G6
ROOTS = [33, 29, 36, 31]

# ---------- sfx ----------
def impact(size=1.0):
    n = int(1.6 * SR); t = tt(n)
    f = 38 + 40 * np.exp(-t / 0.06)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / (0.45 * size))
    thud = lp(noise(n), 260) * np.exp(-t / 0.05) * 1.2
    crack = bp(noise(n), 1500, 6000) * np.exp(-t / 0.015) * 0.25
    return np.tanh((sub + thud + crack) * 1.3)

def shutter():
    """mechanical camera-ish clack: two tight transients + small body thump"""
    n = int(0.25 * SR); t = tt(n); x = np.zeros(n)
    for off, g in [(0, 1.0), (0.032, 0.7)]:
        i = int(off * SR); m = n - i; tm = tt(m)
        x[i:] += bp(noise(m), 1800, 9000) * np.exp(-tm / 0.004) * g
        x[i:] += np.sin(2 * np.pi * 170 * tm) * np.exp(-tm / 0.025) * 0.5 * g
    return x

def whoosh(length=0.7, peak=0.62, f0=300, f1=6500, pan_from=-0.8, pan_to=0.8):
    n = int(length * SR); u = np.linspace(0, 1, n)
    x = noise(n); out = np.zeros(n); seg = 256
    for i in range(0, n, seg):
        p = u[i]; fc = f0 * (f1 / f0) ** min(1, p / peak) if p < peak else f1 * (0.5 ** ((p - peak) / (1 - peak)))
        out[i:i+seg] = bp(x[i:i+seg], max(60, fc * 0.6), min(fc * 1.6, 19000))
    amp = np.where(u < peak, (u / peak) ** 2.2, np.exp(-(u - peak) / 0.08))
    out *= amp
    pan = np.interp(u, [0, 1], [pan_from, pan_to])
    l = out * np.cos((pan + 1) * np.pi / 4); r = out * np.sin((pan + 1) * np.pi / 4)
    return np.stack([l, r], 1) * 1.4

def swish(length=0.16):
    n = int(length * SR); t = tt(n)
    e = (1 - np.exp(-t / 0.012)) * np.exp(-t / 0.035)
    return bp(noise(n), 2500, 9000) * e

def riser(length=1.5):
    n = int(length * SR); u = np.linspace(0, 1, n)
    x = noise(n); out = np.zeros(n); seg = 512
    for i in range(0, n, seg):
        fc = 400 + 7000 * u[i] ** 2
        out[i:i+seg] = bp(x[i:i+seg], fc * 0.7, min(fc * 1.3, 19000))
    return out * u ** 2.5

def rev_cymbal(length=1.0):
    n = int(length * SR); t = tt(n)
    x = hp(noise(n), 4000) * np.exp(-t / 0.35)
    return x[::-1] * 0.9

def tap():
    n = int(0.08 * SR); t = tt(n)
    click = bp(noise(n), 1200, 6000) * np.exp(-t / 0.0025)
    thock = np.sin(2 * np.pi * 240 * t) * np.exp(-t / 0.018) * 0.6
    return click + thock

def confirm():
    """soft airy confirmation: filtered noise swell + gentle FM bell, very short"""
    n = int(0.9 * SR); t = tt(n)
    out = np.zeros(n)
    for m, g, dl in [(81, 1.0, 0.0), (88, 0.7, 0.06)]:
        i = int(dl * SR); tm = tt(n - i); f = mhz(m)
        bell = np.sin(2 * np.pi * f * tm + 1.2 * np.exp(-tm / 0.08) * np.sin(2 * np.pi * f * 2.0 * tm))
        out[i:] += bell * np.exp(-tm / 0.22) * g
    air = bp(noise(n), 4000, 12000) * np.exp(-t / 0.12) * 0.25
    return lp(out, 7000) * 0.5 + air

# ================= ARRANGEMENT =================
# Music bed: pad per bar with section-dependent filter
for bar in range(11):
    t0 = bar * 2.0
    if t0 >= DUR: break
    c = CHORDS[bar % 4]
    if t0 < 2.0: cut = 500
    elif t0 < 8.5: cut = 1300
    elif t0 < 18.5: cut = 2200
    else: cut = 1600
    g = 0.62 if t0 < 2 else 0.42
    music.add(pad_chord(c, 2.06, cut), t0, g)
    send.add(pad_chord(c, 2.06, cut), t0, g * 0.5)
    # rolling offbeat sub bass from the drop
    for k in range(4):
        t = t0 + k * BEAT + BEAT / 2
        if 2.0 <= t < 18.5:
            music.add(sub_bass(ROOTS[bar % 4] + 12, 0.24), t, 0.55)
        tk = t0 + k * BEAT
        if 2.0 <= tk < 18.5 and k == 0:
            music.add(sub_bass(ROOTS[bar % 4] + 12, 0.45), tk + 0.0, 0.25)

# Drums
kick_times = []
for b in range(int(DUR / BEAT)):
    t = b * BEAT
    if 2.0 <= t < 18.5:
        drums.add(kick(), t, 0.8); kick_times.append(t)
        if b % 2 == 1:
            drums.add(clap(), t, 0.42, 0.05); send.add(clap(), t, 0.3)
        drums.add(hat(), t + BEAT / 2 + 0.012, 0.32, -0.25)
        if t >= 8.5:
            drums.add(shaker(), t + BEAT / 4 + 0.01, 0.16, 0.35)
            drums.add(shaker(), t + 3 * BEAT / 4 + 0.014, 0.12, 0.35)
        if t >= 13.0 and b % 4 == 3:
            drums.add(hat(True), t + BEAT / 2, 0.2, -0.2); send.add(hat(True), t + BEAT / 2, 0.12)
drums.add(kick(), 20.0, 0.5); kick_times.append(20.0)

# Hook: 4 camera reveals = shutter clack + sub hit, riser into drop at 2.0
for i, t in enumerate([0.0, 0.5, 1.0, 1.5]):
    sfx.add(shutter(), t, 0.95, (-0.35, 0.35, -0.2, 0.2)[i]); send.add(shutter(), t, 0.25)
    sfx.add(impact(0.6), t, 0.75); send.add(impact(0.6), t, 0.25)
sfx.add(riser(1.4), 0.6, 0.14); send.add(riser(1.4), 0.6, 0.08)
sfx.add(impact(1.2), 2.0, 0.75); send.add(impact(1.2), 2.0, 0.35)
sfx.add(rev_cymbal(0.5), 1.5, 0.1)

# Scene transitions: whoosh synced to wipe (wipe = cut-0.2 .. cut+0.2)
for i, c in enumerate([3.5, 8.5, 13.0, 15.5, 18.5]):
    pf, pt = (-0.7, 0.7) if i % 2 == 0 else (0.7, -0.7)
    w = whoosh(0.7, 0.62, pan_from=pf, pan_to=pt)
    sfx.add(w, c - 0.43, 0.32); send.add(w, c - 0.43, 0.2)
# risers into bigger sections
sfx.add(riser(1.6), 6.9, 0.1); sfx.add(riser(1.3), 14.2, 0.09)
sfx.add(rev_cymbal(1.0), 17.5, 0.12)

# Card / element entrances: soft swishes (no tones)
for t, p in zip([4.0, 5.0, 6.0], [0.4, 0.4, 0.4]):
    sfx.add(swish(), t - 0.02, 0.22, p); send.add(swish(), t, 0.1)
for t in [9.0, 10.0, 11.0, 12.0]:
    sfx.add(swish(0.2), t - 0.02, 0.22, 0.4)
for t, p in zip([13.4, 13.8, 14.2, 14.6], [0.0, 0.4, -0.4, 0.4]):
    sfx.add(swish(0.12), t, 0.16, p)
sfx.add(swish(0.12), 16.4, 0.18)

# Tap on "Dodaj u korpu" + confirmation
sfx.add(tap(), 17.5, 0.55); send.add(tap(), 17.5, 0.15)
sfx.add(confirm(), 17.62, 0.22); send.add(confirm(), 17.62, 0.25)

# Outro
sfx.add(impact(1.3), 18.5, 0.6); send.add(impact(1.3), 18.5, 0.3)

# ================= MIX =================
# sidechain duck on music from kick
duck = np.ones(N)
for t in kick_times:
    i = int(t * SR); n = int(0.3 * SR); j = min(N, i + n)
    d = 1 - 0.6 * np.exp(-np.arange(n) / (0.09 * SR))
    duck[i:j] = np.minimum(duck[i:j], d[: j - i])

revL = fftconvolve(send.L, IR[0])[:N]; revR = fftconvolve(send.R, IR[1])[:N]
L = music.L * duck * 0.9 + drums.L + sfx.L + revL * 0.55
R = music.R * duck * 0.9 + drums.R + sfx.R + revR * 0.55
L = hp(L, 28); R = hp(R, 28)
mix = np.stack([L, R], 1)
mix /= np.abs(mix).max() + 1e-9
mix = np.tanh(mix * 1.6) / np.tanh(1.6)
mix *= 10 ** (-1.0 / 20)
fade = int(0.9 * SR); mix[-fade:] *= np.linspace(1, 0, fade)[:, None] ** 1.5
wavfile.write(os.environ.get('OUT_WAV','music.wav'), SR, (mix * 32767).astype(np.int16))
print('ok')
