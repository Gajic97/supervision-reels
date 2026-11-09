import subprocess, numpy as np, os, sys, json
SRC=sys.argv[1] if len(sys.argv)>1 else '/mnt/user-data/uploads/Downloads'
G={'chill':['zephiramusic-chill-lofi-585360','velariomusic-chill-lofi-616929','alex-morgan-lofi-chill-vlog-beats-573883','fassounds-good-night-lofi-cozy-chill-music-160166','atlasaudio-lofi-chill-589987'],
 'b2b':['atlasaudio-corporate-background-587329','nastelbom-corporate-background-488317','nastelbom-technology-technology-music-602443','the_mountain-technology-corporate-186320']}
# Gajic 9.11.2026: samo chill i b2b (energicno, house i cinematic odbijeni)
OUT=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'assets','music'); L=30.0; SR=22050
meta=[]
for g,names in G.items():
    os.makedirs(f'{OUT}/{g}',exist_ok=True)
    for n in names:
        f=f'{SRC}/{n}.mp3'
        raw=subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout
        x=np.frombuffer(raw,np.float32); dur=len(x)/SR
        win=int(0.5*SR); e=np.sqrt(np.convolve(x**2,np.ones(win)/win,'valid')[::win])
        n_w=int(L/0.5); start=0.0
        if dur>L+2:
            lo=int(min(8,dur*0.08)/0.5); best=-1
            for i in range(lo,len(e)-n_w):
                s=e[i:i+n_w].mean()
                if s>best: best=s;start=i*0.5
        seg=min(L,dur-start)
        out=f'{OUT}/{g}/{n}.mp3'
        subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{start:.2f}','-t',f'{seg:.2f}','-i',f,
          '-af',f'afade=t=in:d=0.05,afade=t=out:st={seg-1.5:.2f}:d=1.5,loudnorm=I=-16:TP=-1.5:LRA=11','-ar','44100','-b:a','192k',out],check=True)
        meta.append({'grupa':g,'fajl':f'{g}/{n}.mp3','izvor_id':n.rsplit('-',1)[1],'autor':n.split('-')[0],'pocetak_s':start,'trajanje_s':round(seg,1),'original_s':round(dur,1)})
        print(g,n,f'{dur:.0f}s start {start}s')
json.dump(meta,open(f'{OUT}/index.json','w'),ensure_ascii=False,indent=1)
