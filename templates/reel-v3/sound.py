"""SuperVision reel audio v3: više muzičkih stilova + dizajnirani zvučni efekti (bez 8-bit i blip zvukova).

Upotreba:
  STYLE=deep_house|lofi_chill|synthwave|cinematic|minimal_tech  KEY=0..11 (transpozicija u polutonovima)
  INTRO=3.0 (sekunde tekstualnog hook-a pre glavnog dela)  SEED=<broj>
  SFX=sfx.json (opciono; lista događaja u APSOLUTNOM vremenu: {"type","t","g","pan"})
  OUT_WAV=music.wav  python3 sound.py
Glavni deo traje 21 s na 120 BPM; „drop“ (ulazak bubnja) je na INTRO+2.0 s.
Tipovi efekata: shutter, impact, impact_big, whoosh (t = trenutak reza), swish, riser (t = kraj), tap, confirm, thud, revcym (t = kraj).
"""
import json, os
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile

STYLE = os.environ.get("STYLE", "deep_house")
KEY = int(os.environ.get("KEY", "0"))
INTRO = float(os.environ.get("INTRO", "3.0"))
SEED = int(os.environ.get("SEED", "11"))
SR = 44100
MAIN = 21.0
DUR = INTRO + MAIN
BEAT = 0.5
N = int(SR * DUR)
rng = np.random.default_rng(SEED)
DROP = INTRO + 2.0
END = INTRO + 18.5          # posle ovoga ide outro

def sos(kind, f, o=2): return butter(o, f, kind, fs=SR, output='sos')
def lp(x, f, o=2): return sosfilt(sos('low', min(f, SR / 2 - 100), o), x)
def hp(x, f, o=2): return sosfilt(sos('high', f, o), x)
def bp(x, f1, f2, o=2): return sosfilt(sos('band', [f1, min(f2, SR / 2 - 100)], o), x)
def mhz(m): return 440 * 2 ** ((m + KEY - 69) / 12)
def tt(n): return np.arange(n) / SR
def noise(n): return rng.standard_normal(n)

class Bus:
    def __init__(s): s.L = np.zeros(N); s.R = np.zeros(N)
    def add(s, sig, t0, g=1.0, pan=0.0):
        i = int(round(t0 * SR))
        if i < 0: sig = sig[-i:]; i = 0
        if i >= N or len(sig) == 0: return
        x = sig[: N - i] * g
        if x.ndim == 2:
            s.L[i:i+len(x)] += x[:, 0]; s.R[i:i+len(x)] += x[:, 1]; return
        gl = np.cos((pan + 1) * np.pi / 4) * 1.414; gr = np.sin((pan + 1) * np.pi / 4) * 1.414
        s.L[i:i+len(x)] += x * gl; s.R[i:i+len(x)] += x * gr

music, drums, sfx, send = Bus(), Bus(), Bus(), Bus()

def make_ir(length=2.2, decay=0.55, pre=0.018, damp=6000):
    n = int(length * SR); t = tt(n); irs = []
    for _ in range(2):
        x = lp(noise(n) * np.exp(-t / decay), damp); x = hp(x, 180)
        x = np.concatenate([np.zeros(int(pre * SR)), x]); irs.append(x / np.sqrt((x ** 2).sum()))
    return irs

# ================= INSTRUMENTI =================
def kick(decay=0.2, punch=120, drive=2.2):
    n = int(0.45 * SR); t = tt(n)
    f = 46 + punch * np.exp(-t / 0.028)
    s = np.tanh(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / decay) * drive) / np.tanh(drive)
    return s + hp(noise(n), 2500) * np.exp(-t / 0.003) * 0.35

def clap():
    n = int(0.35 * SR); x = np.zeros(n)
    for k, off in enumerate([0, 0.009, 0.019, 0.03]):
        i = int(off * SR); m = n - i
        x[i:] += noise(m) * np.exp(-tt(m) / (0.012 if k < 3 else 0.09))
    return bp(x, 1000, 4200) * 0.8

def snare(big=False):
    n = int((0.5 if big else 0.25) * SR); t = tt(n)
    body = np.sin(2 * np.pi * 190 * t) * np.exp(-t / 0.05)
    nz = bp(noise(n), 1500, 9000) * np.exp(-t / (0.12 if big else 0.06))
    return body * 0.6 + nz

def rim():
    n = int(0.06 * SR); t = tt(n)
    return bp(noise(n), 1800, 5000) * np.exp(-t / 0.006) + np.sin(2 * np.pi * 520 * t) * np.exp(-t / 0.01) * 0.3

def hat(open_=False):
    n = int((0.28 if open_ else 0.07) * SR); t = tt(n)
    met = sum(np.sign(np.sin(2 * np.pi * f * t)) for f in [205.3, 304.4, 369.6, 522.7, 540, 800])
    return hp(met * 0.3 + noise(n), 7500, 3) * np.exp(-t / (0.09 if open_ else 0.016)) * 0.6

def shaker():
    n = int(0.09 * SR); t = tt(n)
    return bp(noise(n), 5000, 12000) * (1 - np.exp(-t / 0.01)) * np.exp(-t / 0.03)

def tom(f0=110):
    n = int(0.9 * SR); t = tt(n)
    f = f0 * (1 + 0.6 * np.exp(-t / 0.04))
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.35)
    return np.tanh(s * 1.8) + lp(noise(n), 400) * np.exp(-t / 0.03) * 0.5

def supersaw(f, n, voices=7, spread=0.12):
    t = tt(n); out = np.zeros(n)
    for v in range(voices):
        d = (v - (voices - 1) / 2) / ((voices - 1) / 2) * spread
        out += 2 * ((t * f * 2 ** (d / 12) + rng.random()) % 1) - 1
    return out / voices

def env_ar(n, a, r):
    e = np.ones(n); na = max(1, int(a * SR)); nr = max(1, int(r * SR))
    e[:na] = np.linspace(0, 1, na); e[-nr:] *= np.linspace(1, 0, nr); return e

def pad_saw(notes, length, cutoff, bright=1.0):
    n = int(length * SR); l = np.zeros(n); r = np.zeros(n)
    for m in notes:
        l += supersaw(mhz(m), n); r += supersaw(mhz(m) * 1.002, n)
    e = env_ar(n, 0.35, 0.25)
    return np.stack([lp(l, cutoff * bright) * e, lp(r, cutoff * bright) * e], 1) / len(notes)

def epiano(notes, length, vel=1.0):
    """toplo električno pijanino (FM), akord udaren jednom i drži se"""
    n = int(length * SR); t = tt(n); out = np.zeros(n)
    for k, m in enumerate(notes):
        f = mhz(m); d = k * 0.012
        i = int(d * SR); tm = t[: n - i]
        mod = 1.4 * np.exp(-tm / 0.25) * np.sin(2 * np.pi * f * tm)
        out[i:] += np.sin(2 * np.pi * f * tm + mod) * np.exp(-tm / 1.6) * (1 + 0.15 * np.sin(2 * np.pi * 5 * tm))
    out = lp(out, 3500) * vel / len(notes)
    return np.stack([out, np.roll(out, 220)], 1)

def strings(notes, length, cutoff=1800):
    n = int(length * SR); l = np.zeros(n); r = np.zeros(n); t = tt(n)
    vib = 1 + 0.004 * np.sin(2 * np.pi * 5.2 * t)
    for m in notes:
        for d in (-0.07, 0.0, 0.07):
            ph = np.cumsum(mhz(m + d) * vib) / SR
            l += 2 * ((ph + rng.random()) % 1) - 1; r += 2 * ((ph * 1.001 + rng.random()) % 1) - 1
    e = env_ar(n, 0.8, 0.5)
    return np.stack([lp(l, cutoff) * e, lp(r, cutoff) * e], 1) / (len(notes) * 3)

def sub_bass(m, length, drive=1.6, cutoff=900):
    n = int(length * SR); t = tt(n); f = mhz(m)
    s = np.tanh((np.sin(2 * np.pi * f * t) + 0.18 * np.sin(4 * np.pi * f * t)) * drive)
    return lp(s, cutoff) * np.minimum(1, t / 0.006) * np.exp(-t / (length * 0.8))

def saw_bass(m, length, cutoff=500):
    n = int(length * SR); t = tt(n); f = mhz(m)
    s = 2 * ((t * f) % 1) - 1 + 0.6 * np.sin(2 * np.pi * f / 2 * t)
    fc = cutoff * (1 + 3 * np.exp(-t / 0.05))
    out = np.zeros(n); seg = 256
    for i in range(0, n, seg): out[i:i+seg] = lp(s[i:i+seg], fc[i])
    return out * np.minimum(1, t / 0.004) * np.exp(-t / (length * 0.9))

def saw_arp(m, length=0.24, cutoff=1800):
    """meki filtrirani saw arpeggio (synthwave), dug rep kroz reverb; nije čip/blip"""
    n = int(length * SR); t = tt(n); f = mhz(m)
    s = (2 * ((t * f) % 1) - 1) + (2 * ((t * f * 1.005) % 1) - 1)
    return lp(s, cutoff) * np.minimum(1, t / 0.01) * np.exp(-t / (length * 0.6)) * 0.5

def crackle(n):
    x = np.zeros(n); idx = rng.integers(0, n, int(n / SR * 40))
    x[idx] = rng.standard_normal(len(idx)); return hp(x, 1500) * 0.6 + lp(noise(n), 300) * 0.02

# ================= EFEKTI =================
def impact(size=1.0):
    n = int(1.6 * SR); t = tt(n)
    f = 38 + 40 * np.exp(-t / 0.06)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / (0.45 * size))
    return np.tanh((sub + lp(noise(n), 260) * np.exp(-t / 0.05) * 1.2 + bp(noise(n), 1500, 6000) * np.exp(-t / 0.015) * 0.25) * 1.3)

def shutter():
    n = int(0.25 * SR); x = np.zeros(n)
    for off, g in [(0, 1.0), (0.032, 0.7)]:
        i = int(off * SR); m = n - i; tm = tt(m)
        x[i:] += bp(noise(m), 1800, 9000) * np.exp(-tm / 0.004) * g + np.sin(2 * np.pi * 170 * tm) * np.exp(-tm / 0.025) * 0.5 * g
    return x

def thud():
    n = int(0.3 * SR); t = tt(n)
    return np.sin(2 * np.pi * (60 + 50 * np.exp(-t / 0.02)) * t) * np.exp(-t / 0.09) + bp(noise(n), 2000, 7000) * np.exp(-t / 0.004) * 0.25

def whoosh(length=0.7, peak=0.62, f0=300, f1=6500, pan_from=-0.8, pan_to=0.8):
    n = int(length * SR); u = np.linspace(0, 1, n); x = noise(n); out = np.zeros(n); seg = 256
    for i in range(0, n, seg):
        p = u[i]; fc = f0 * (f1 / f0) ** min(1, p / peak) if p < peak else f1 * (0.5 ** ((p - peak) / (1 - peak)))
        out[i:i+seg] = bp(x[i:i+seg], max(60, fc * 0.6), min(fc * 1.6, 19000))
    out *= np.where(u < peak, (u / peak) ** 2.2, np.exp(-(u - peak) / 0.08))
    pan = np.interp(u, [0, 1], [pan_from, pan_to])
    return np.stack([out * np.cos((pan + 1) * np.pi / 4), out * np.sin((pan + 1) * np.pi / 4)], 1) * 1.4

def swish(length=0.16):
    n = int(length * SR); t = tt(n)
    return bp(noise(n), 2500, 9000) * (1 - np.exp(-t / 0.012)) * np.exp(-t / 0.035)

def riser(length=1.5):
    n = int(length * SR); u = np.linspace(0, 1, n); x = noise(n); out = np.zeros(n); seg = 512
    for i in range(0, n, seg):
        fc = 400 + 7000 * u[i] ** 2; out[i:i+seg] = bp(x[i:i+seg], fc * 0.7, min(fc * 1.3, 19000))
    return out * u ** 2.5

def rev_cymbal(length=1.0):
    n = int(length * SR); return (hp(noise(n), 4000) * np.exp(-tt(n) / 0.35))[::-1] * 0.9

def tap():
    n = int(0.08 * SR); t = tt(n)
    return bp(noise(n), 1200, 6000) * np.exp(-t / 0.0025) + np.sin(2 * np.pi * 240 * t) * np.exp(-t / 0.018) * 0.6

def confirm():
    n = int(0.9 * SR); t = tt(n); out = np.zeros(n)
    for m, g, dl in [(81, 1.0, 0.0), (88, 0.7, 0.06)]:
        i = int(dl * SR); tm = tt(n - i); f = mhz(m)
        out[i:] += np.sin(2 * np.pi * f * tm + 1.2 * np.exp(-tm / 0.08) * np.sin(4 * np.pi * f * tm)) * np.exp(-tm / 0.22) * g
    return lp(out, 7000) * 0.5 + bp(noise(n), 4000, 12000) * np.exp(-t / 0.12) * 0.25

# ================= STILOVI =================
# akordi (MIDI, pre transpozicije) i koreni basa, 4 takta po 2 s
STYLES = {
    "deep_house":   dict(ch=[[57,60,64,67,71],[53,57,60,64,69],[48,55,59,62,64],[55,59,62,64,67]], root=[45,41,48,43], key=0),
    "lofi_chill":   dict(ch=[[50,53,57,60,64],[55,59,62,65,69],[48,52,55,59,62],[57,60,64,67,71]], root=[38,43,36,45], key=2),
    "synthwave":    dict(ch=[[52,55,59,64],[48,52,55,60],[55,59,62,67],[50,54,57,62]], root=[40,36,43,38], key=0),
    "cinematic":    dict(ch=[[50,53,57,62],[46,50,53,58],[53,57,60,65],[48,52,55,60]], root=[38,34,41,36], key=0),
    "minimal_tech": dict(ch=[[53,56,60,63],[49,53,56,60],[56,60,63,67],[51,55,58,63]], root=[41,37,44,39], key=0),
}
st = STYLES[STYLE]
if "KEY" not in os.environ: KEY = st["key"]
CH, ROOT = st["ch"], st["root"]
kick_times = []

def add_kick(t, g=0.85, **kw):
    drums.add(kick(**kw), t, g); kick_times.append(t)

bars = int(np.ceil(MAIN / 2))
# ---- intro: tihi bed + riser do drop-a glavnog dela
for bar in range(int(np.ceil(INTRO / 2))):
    c = CH[bar % 4]; tb = bar * 2.0
    if STYLE == "lofi_chill":   music.add(epiano(c, 2.0, 0.8), tb, 0.5)
    elif STYLE == "cinematic":  music.add(strings(c, 2.1, 900), tb, 0.6)
    else:                       music.add(pad_saw(c, 2.05, 420), tb, 0.5)

for bar in range(bars):
    tb = INTRO + bar * 2.0; c = CH[bar % 4]; r = ROOT[bar % 4]
    pre = tb < DROP; outro = tb >= END
    # ---------- harmonija
    if STYLE == "deep_house":
        cut = 500 if pre else (1300 if tb < INTRO + 8.5 else (2200 if not outro else 1600))
        p = pad_saw(c, 2.06, cut); music.add(p, tb, 0.42 if not pre else 0.6); send.add(p, tb, 0.22)
    elif STYLE == "lofi_chill":
        e = epiano(c, 2.0); music.add(e, tb, 0.75); send.add(e, tb, 0.35)
        music.add(np.stack([crackle(int(2 * SR))] * 2, 1), tb, 0.08)
    elif STYLE == "synthwave":
        p = pad_saw(c, 2.06, 900 if pre else 2600); music.add(p, tb, 0.35); send.add(p, tb, 0.25)
    elif STYLE == "cinematic":
        s = strings(c, 2.15, 1200 if pre else 2600); music.add(s, tb, 0.7); send.add(s, tb, 0.45)
    elif STYLE == "minimal_tech":
        p = pad_saw(c, 2.06, 700 if pre else 1100, 0.9); music.add(p, tb, 0.3); send.add(p, tb, 0.3)
    # ---------- bas
    for k in range(4):
        t = tb + k * BEAT
        if t < DROP or t >= END: continue
        if STYLE == "deep_house":
            music.add(sub_bass(r + 12, 0.24), t + BEAT / 2, 0.55)
        elif STYLE == "lofi_chill":
            music.add(sub_bass(r + 12, 0.45, 1.2, 600), t, 0.5 if k in (0, 2) else 0.0)
        elif STYLE == "synthwave":
            for h in (0, BEAT / 2): music.add(saw_bass(r + 12, 0.22, 420), t + h, 0.32)
        elif STYLE == "cinematic":
            if k == 0: music.add(sub_bass(r + 12, 1.8, 1.4, 500), t, 0.55)
        elif STYLE == "minimal_tech":
            for q in range(4): music.add(saw_bass(r + 12 + (12 if q == 2 else 0), 0.11, 350), t + q * BEAT / 4, 0.28)
    # ---------- melodijski sloj
    if STYLE == "synthwave" and INTRO + 8.5 <= tb < END:
        arp = [c[0] + 12, c[1] + 12, c[2] + 12, c[1] + 24] if len(c) > 3 else c
        for k in range(16):
            a = saw_arp(arp[k % len(arp)], 0.22, 2200); music.add(a, tb + k * BEAT / 4, 0.16, 0.3 if k % 2 else -0.3); send.add(a, tb + k * BEAT / 4, 0.12)

# ---------- bubnjevi
for b in range(int(MAIN / BEAT)):
    t = INTRO + b * BEAT
    if not (DROP <= t < END): continue
    sw = 0.03 if STYLE == "lofi_chill" else 0.012
    if STYLE in ("deep_house", "synthwave"):
        add_kick(t, 0.8)
        if b % 2 == 1:
            sn = clap() if STYLE == "deep_house" else snare(big=True)
            drums.add(sn, t, 0.42 if STYLE == "deep_house" else 0.32, 0.05); send.add(sn, t, 0.3 if STYLE == "deep_house" else 0.5)
        drums.add(hat(), t + BEAT / 2 + sw, 0.3, -0.25)
        if t >= INTRO + 8.5: drums.add(shaker(), t + BEAT / 4 + 0.01, 0.14, 0.35)
    elif STYLE == "lofi_chill":
        bar_pos = b % 4
        if bar_pos == 0: add_kick(t, 0.7, decay=0.16, punch=80, drive=1.5)
        if bar_pos == 1: add_kick(t + BEAT / 2 + sw, 0.55, decay=0.16, punch=80, drive=1.5)
        if bar_pos == 2: sn = snare(); drums.add(lp(sn, 5000), t, 0.32); send.add(sn, t, 0.2)
        drums.add(lp(hat(), 9000), t + sw, 0.2, -0.3); drums.add(lp(hat(), 9000), t + BEAT / 2 + sw, 0.14, -0.3)
    elif STYLE == "cinematic":
        if b % 2 == 0: drums.add(tom(90 if b % 4 == 0 else 120), t, 0.55, -0.2 if b % 4 else 0.2); send.add(tom(100), t, 0.25)
        if b % 8 == 7: drums.add(tom(140), t + BEAT / 2, 0.35, 0.3)
        if t >= INTRO + 8.5 and b % 4 == 2: drums.add(snare(big=True), t, 0.25); send.add(snare(big=True), t, 0.4)
        kick_times.append(t) if b % 4 == 0 else None
    elif STYLE == "minimal_tech":
        add_kick(t, 0.85, decay=0.15, punch=140, drive=2.8)
        if b % 2 == 1: drums.add(rim(), t + BEAT / 4, 0.3, 0.2); send.add(rim(), t + BEAT / 4, 0.2)
        for q in range(4): drums.add(hat(), t + q * BEAT / 4 + (0.02 if q % 2 else 0), 0.18 if q % 2 else 0.1, -0.2)
        if b % 4 == 3: drums.add(hat(True), t + BEAT / 2, 0.16, 0.2)
add_kick(INTRO + 20.0, 0.5)

# ---------- outro akord
oc = [CH[0][0], CH[0][2], CH[0][0] + 12, CH[0][1] + 12]
if STYLE == "lofi_chill": music.add(epiano(oc, 2.5), END, 0.7)
elif STYLE == "cinematic": music.add(strings(oc, 2.5, 2000), END, 0.7)
else: music.add(pad_saw(oc, 2.5, 1600), END, 0.4)

# ================= EFEKTI (sfx.json ili podrazumevani raspored reel-v2 + intro) =================
def default_events():
    ev = []
    for i in range(8): ev.append({"type": "thud", "t": 0.1 + i * 0.12, "g": 0.35})
    ev.append({"type": "swish", "t": 1.0, "g": 0.18})
    ev += [{"type": "riser", "t": INTRO, "g": 0.12, "len": 1.6}]
    o = INTRO
    for i, t in enumerate([0.0, 0.5, 1.0, 1.5]): ev.append({"type": "shutter", "t": o + t, "g": 0.95, "pan": (-0.35, 0.35, -0.2, 0.2)[i]})
    ev.append({"type": "impact_big", "t": o + 2.0, "g": 0.75})
    for c in [0.0, 3.5, 8.5, 13.0, 15.5, 18.5]: ev.append({"type": "whoosh", "t": o + c, "g": 0.32})
    for t in [4.0, 5.0, 6.0, 9.0, 10.0, 11.0, 12.0, 13.4, 13.8, 14.2, 14.6, 16.4]: ev.append({"type": "swish", "t": o + t, "g": 0.2})
    ev += [{"type": "riser", "t": o + 8.5, "g": 0.1}, {"type": "revcym", "t": o + 18.5, "g": 0.12},
           {"type": "tap", "t": o + 17.5, "g": 0.55}, {"type": "confirm", "t": o + 17.62, "g": 0.22},
           {"type": "impact_big", "t": o + 18.5, "g": 0.6}]
    return ev

events = json.load(open(os.environ["SFX"])) if os.environ.get("SFX") else default_events()
for i, e in enumerate(events):
    ty, t, g, pan = e["type"], float(e["t"]), float(e.get("g", 0.3)), float(e.get("pan", 0))
    if ty == "shutter":      sfx.add(shutter(), t, g, pan); send.add(shutter(), t, g * 0.25)
    elif ty == "impact":     sfx.add(impact(0.6), t, g); send.add(impact(0.6), t, g * 0.3)
    elif ty == "impact_big": sfx.add(impact(1.3), t, g); send.add(impact(1.3), t, g * 0.45)
    elif ty == "thud":       sfx.add(thud(), t, g, pan)
    elif ty == "whoosh":
        w = whoosh(0.7, 0.62, pan_from=(-0.7 if i % 2 else 0.7), pan_to=(0.7 if i % 2 else -0.7))
        sfx.add(w, t - 0.43, g); send.add(w, t - 0.43, g * 0.6)
    elif ty == "swish":      sfx.add(swish(), t - 0.02, g, pan); send.add(swish(), t, g * 0.4)
    elif ty == "riser":      L = float(e.get("len", 1.4)); sfx.add(riser(L), t - L, g); send.add(riser(L), t - L, g * 0.6)
    elif ty == "revcym":     sfx.add(rev_cymbal(1.0), t - 1.0, g)
    elif ty == "tap":        sfx.add(tap(), t, g); send.add(tap(), t, g * 0.3)
    elif ty == "confirm":    sfx.add(confirm(), t, g); send.add(confirm(), t, g)

# ================= MIKS =================
duck = np.ones(N)
for t in kick_times:
    i = int(t * SR); n = int(0.3 * SR); j = min(N, i + n)
    d = 1 - (0.6 if STYLE != "lofi_chill" else 0.3) * np.exp(-np.arange(n) / (0.09 * SR)); duck[i:j] = np.minimum(duck[i:j], d[: j - i])
IR = make_ir(3.2 if STYLE == "cinematic" else 2.2, 0.8 if STYLE == "cinematic" else 0.55)
revL = fftconvolve(send.L, IR[0])[:N]; revR = fftconvolve(send.R, IR[1])[:N]
L = hp(music.L * duck * 0.9 + drums.L + sfx.L + revL * 0.55, 28)
R = hp(music.R * duck * 0.9 + drums.R + sfx.R + revR * 0.55, 28)
mix = np.stack([L, R], 1); mix /= np.abs(mix).max() + 1e-9
mix = np.tanh(mix * 1.6) / np.tanh(1.6) * 10 ** (-1.0 / 20)
fade = int(0.9 * SR); mix[-fade:] *= np.linspace(1, 0, fade)[:, None] ** 1.5
wavfile.write(os.environ.get("OUT_WAV", "music.wav"), SR, (mix * 32767).astype(np.int16))
print("ok", STYLE, "key", KEY, "dur", DUR)
