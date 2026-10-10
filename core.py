import math
def validate(image):
    if not image or not image[0] or any(len(row)!=len(image[0]) for row in image): raise ValueError('Rectangular image required')
def convolve(image,kernel):
    validate(image);h=len(image);w=len(image[0]);out=[]
    for y in range(h):
        row=[]
        for x in range(w):
            value=sum(image[min(h-1,max(0,y+j-1))][min(w-1,max(0,x+i-1))]*kernel[j][i] for j in range(3) for i in range(3))
            row.append(value)
        out.append(row)
    return out
def transform(image,mode):
    if mode=='original':validate(image);return image
    if mode=='blur': return convolve(image,[[1/9]*3 for _ in range(3)])
    if mode=='edges':
        gx=convolve(image,[[-1,0,1],[-2,0,2],[-1,0,1]])
        gy=convolve(image,[[-1,-2,-1],[0,0,0],[1,2,1]])
        return [[min(255,math.hypot(x,y)) for x,y in zip(rx,ry)] for rx,ry in zip(gx,gy)]
    raise ValueError('Unknown filter')
def run(payload):
    image=[[220 if 16<x<47 and 16<y<47 else 25 for x in range(64)] for y in range(64)]
    processed=transform(image,payload.get('mode','edges'))
    return {'image':processed,'width':64,'height':64,'mean_intensity':sum(map(sum,processed))/4096,'boundary':'replicated border pixels'}
