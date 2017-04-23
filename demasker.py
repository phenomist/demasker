from PIL import Image

def extrapolate(maskedcolor, maskcolor, alpha):
    if alpha > 250:
        return -1 #difficult to deduce unmasked color
    alpha = alpha/255
    a = min(max(int(1/(1-alpha)*(maskedcolor[0]-maskcolor[0])+maskcolor[0]),1),254)
    b = min(max(int(1/(1-alpha)*(maskedcolor[1]-maskcolor[1])+maskcolor[1]),1),254)
    c = min(max(int(1/(1-alpha)*(maskedcolor[2]-maskcolor[2])+maskcolor[2]),1),254)
    #print(maskedcolor, maskcolor, a,b,c)
    return (a,b,c)

def demasker(maskedimage, maskimage, xoffset=0, yoffset=0, target = "demask.png", alpha=1):
    ciph = Image.open(maskedimage)
    cdim = ciph.size
    mask = Image.open(maskimage)
    mdim = mask.size
    cpix = ciph.load()
    mpix = mask.load()
    out = Image.new("RGB", cdim)
    recent = (0,0,0)
    a = []
    for y in range(cdim[1]):
        for x in range(cdim[0]):
            e = extrapolate(cpix[x,y],mpix[(x+xoffset)%mdim[0],(y+yoffset)%mdim[1]],mpix[(x+xoffset)%mdim[0],(y+yoffset)%mdim[1]][3]*alpha)

            if e == -1:
                e = recent
            else:
                recent = e
            a.append(e)
    out.putdata(a)
    out.save(target, 'PNG')

#example usecase: demasker("35164.png", "weave.png")
