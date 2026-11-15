# Beat-synced sound design for intro.html. 120 BPM. Usage: python3 audio.py hits.json out.wav
import json,sys,numpy as np
SR=44100;D=30;B=.5;rng=np.random.default_rng(7)
N=SR*D;L=np.zeros(N);R=np.zeros(N)
def tt(d):return np.arange(int(d*SR))/SR
def add(t0,x,g=1,pan=0):
    i=int(t0*SR)
    if i<0:x=x[-i:];i=0
    x=x[:N-i]
    if len(x)<=0:return
    L[i:i+len(x)]+=x*g*(1-max(0,pan));R[i:i+len(x)]+=x*g*(1+min(0,pan))
def lp(x,a):  # one-pole lowpass via kernel
    k=(1-a)*a**np.arange(400);return np.convolve(x,k)[:len(x)]
def hp(x,a):return x-lp(x,a)
def noise(d):return rng.standard_normal(int(d*SR))
def env(d,k):return np.exp(-tt(d)*k)
def kick(v=1):
    t=tt(.42);f=45+90*np.exp(-t*28);ph=2*np.pi*np.cumsum(f)/SR
    return (np.sin(ph)*np.exp(-t*7)+.35*hp(noise(.42),.5)*np.exp(-t*120))*v
def clap(v=1):
    t=tt(.3);n=hp(noise(.3),.6);return n*(np.exp(-t*22)+.6*np.exp(-((t-.012)%.02)*0)*np.exp(-t*50))*v*.7
def hat(d=.05,k=90,v=1):return hp(noise(d),.4)*env(d,k)*v*.5
def tok(v=1):
    t=tt(.12);f=300+900*np.exp(-t*60);return (np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*34)+.4*hp(noise(.12),.5)*np.exp(-t*90))*v
def boom(v=1):
    t=tt(1.2);f=38+60*np.exp(-t*12);return (np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*3.2)+.5*lp(noise(1.2),.9)*np.exp(-t*5))*v
def whoosh(d=.5):
    t=tt(d);n=noise(d);s=np.zeros_like(n)
    for a in (.97,.9,.7,.4):  # sweep: brighter over time
        m=np.clip((t/d-(.97-a)),0,1);s+=hp(lp(n,a),.5)*m*.5
    return s*(t/d)**2*np.minimum(1,(d-t)*40)
def riser(d):
    t=tt(d);n=hp(noise(d),.55)*(t/d)**2.2
    f=200*2**(t/d*3);saw=np.sin(2*np.pi*np.cumsum(f)/SR)*(t/d)**2
    return n*.6+saw*.25
def pluck(f,v=1,d=.35):
    t=tt(d);return (np.sin(2*np.pi*f*t)+.4*np.sin(4*np.pi*f*t)+.2*np.sin(6*np.pi*f*t))*np.exp(-t*11)*v
def bass(f,d=.45):
    t=tt(d);x=np.sin(2*np.pi*f*t)+.25*np.sin(4*np.pi*f*t)+.1*np.sin(6*np.pi*f*t);return x*np.minimum(1,t*200)*np.exp(-t*3.4)
def pad(d):
    t=tt(d);x=0
    for f in (110,130.81,164.81,220):
        for dt in (-.4,.4):x=x+np.sin(2*np.pi*(f+dt)*t)+.3*np.sin(4*np.pi*(f+dt)*t)
    x*=(.5+.5*np.sin(2*np.pi*t/8-1.2))**1.2;return x/10
J=json.load(open(sys.argv[1]));hits=J['hits'];starts=J['starts']
# drums
kk=[];beats=int(D/B)
for i in range(beats):
    t=i*B
    if 7<=t<8 or t>=29.5:continue
    add(t,kick(),1.0 if t>=4 else .8);kk.append(t)
    if t>=2:add(t+B/2,hat(.05,90,.8),.45,.3)
    if t>=4 and i%2==1:add(t,clap(),.7)
    if t>=4:add(t+B/2,hat(.18,18,.8),.35,-.3)
for k in range(16):add(7+k*.0625*1.0,clap(.4+k*.04),.5)  # snare roll 7-8
# bass + pluck + pad
roots=[55,55,65.41,49,55,55,73.42,65.41]
for i in range(int(8/B*2),int(29.5/B)*1):
    pass
t=8.0;n=0
while t<29.5:
    f=roots[n%8];add(t,bass(f),.7);add(t+B/2,bass(f*(2 if n%4==3 else 1)),.45);t+=B;n+=1
sc=[220,261.63,329.63,392,440,523.25,392,329.63]
t=12.0;n=0
while t<29.5:
    add(t,pluck(sc[n%8]),.22,-.5+.1*(n%8));add(t+B/4*1,pluck(sc[(n+3)%8]*1,0.8),.12,.5-.1*(n%8));t+=B/2;n+=1
add(0,pad(D),.35,0)
# fx
for s in starts:add(s-.4,whoosh(.4),.5,0);add(s,boom(),.8 if s in(0,24) else .55)
add(6,riser(2),.5);add(22,riser(2),.55)
for t0,k in hits:
    if k=='k':add(t0,tok(),.5,rng.uniform(-.2,.2))
    elif k=='b':add(t0,boom(),.6);add(t0,tok(1.2),.6)
    else:add(t0,pluck(rng.choice([523.25,659.25,784,880,1046.5]),1,.3),.28,rng.uniform(-.6,.6))
add(29.5,boom(),.9)
# sidechain pump on everything but drums is approximated: duck whole bed slightly on kicks
duck=np.ones(N)
for t0 in kk:
    i=int(t0*SR);m=np.arange(min(N-i,int(.3*SR)))/SR;duck[i:i+len(m)]*=1-.35*np.exp(-m*14)
L*=duck;R*=duck
# reverb
ir=noise(1.1)*np.exp(-tt(1.1)*4.2);ir=lp(ir,.6)
def rev(x):
    n=1<<int(np.ceil(np.log2(len(x)+len(ir))));return np.fft.irfft(np.fft.rfft(x,n)*np.fft.rfft(ir,n),n)[:len(x)]
send=.12/np.abs(ir).sum()*40
L=L+rev(L)*send;R=R+rev(R)*send
fade=np.minimum(1,(D-tt(D))/1.0);fade=np.minimum(fade,np.minimum(1,tt(D)/.02))
out=np.stack([L,R],1)*fade[:,None]
out=np.tanh(out*1.3);out/=np.abs(out).max()/.89
import wave
w=wave.open(sys.argv[2],'wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((out*32767).astype('<i2').tobytes());w.close()
