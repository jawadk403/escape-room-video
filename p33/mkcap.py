import json,re,difflib
W=json.load(open('wall.json')); TL=json.load(open('timeline.json'))
W['C9fix']=[w for w in W['F9a'] if w[1]<3.7]+[w for w in W['C9'] if w[1]>=3.7]
# ASR words on the timeline
A=[]
for s in TL:
    for w,a,b in W[s['a']]:
        if s['ai']-0.05<=a<s['ai']+s['d']-0.05:
            A.append([w,s['t']+a-s['ai'],min(s['t']+b-s['ai'],s['t']+s['d'])])
# script words
txt=[]
for l in open('script.txt'):
    l=l.strip()
    if not l: continue
    txt.append(l.split(':',1)[1].strip())
S=' '.join(txt).replace('—',' — ').replace('"','')
S=re.sub(r'\s+',' ',S).replace(' — ',' ').split(' ')
nz=lambda w:re.sub(r"[^a-z0-9$]","",w.lower().replace('-',''))
an=[nz(w[0]) for w in A]; sn=[nz(w) for w in S]
sm=difflib.SequenceMatcher(None,sn,an,autojunk=False)
T=[None]*len(S)
for a,b,n in sm.get_matching_blocks():
    for k in range(n): T[a+k]=(A[b+k][1],A[b+k][2])
# fill gaps: script words with no ASR match get interpolated between neighbours
ops=sm.get_opcodes(); miss=[]
for tag,i1,i2,j1,j2 in ops:
    if tag in('replace','insert','delete') and i2>i1:
        if j2>j1:
            s0=A[j1][1]; e0=A[j2-1][2]
        else:
            s0=T[i1-1][1] if i1>0 and T[i1-1] else 0; e0=s0+0.3*(i2-i1)
        n=i2-i1
        for q in range(n): T[i1+q]=(s0+(e0-s0)*q/n,s0+(e0-s0)*(q+1)/n)
        miss.append((tag,' '.join(S[i1:i2]),' '.join(w[0] for w in A[j1:j2])))
print('MISMATCH',miss)
json.dump([[S[i],T[i][0],T[i][1]] for i in range(len(S))],open('capwords.json','w'))
print(len(S),'words')
