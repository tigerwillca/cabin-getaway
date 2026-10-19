from PIL import Image, ImageDraw
for s,n in [(180,'apple-touch-icon.png'),(192,'icon-192.png'),(512,'icon-512.png')]:
    im=Image.new('RGB',(s,s)); d=ImageDraw.Draw(im)
    for y in range(s):
        t=y/s; d.line([(0,y),(s,y)],fill=(int(30+60*t),int(60+50*t),int(70+20*t)))
    k=s/100
    d.polygon([(70*k,20*k),(55*k,55*k),(85*k,55*k)],fill=(40,90,60)); d.rectangle([68*k,55*k,72*k,62*k],fill=(90,60,40))
    d.polygon([(15*k,50*k),(40*k,28*k),(65*k,50*k)],fill=(150,80,50))
    d.rectangle([20*k,50*k,60*k,75*k],fill=(190,130,80)); d.rectangle([35*k,60*k,45*k,75*k],fill=(255,210,130))
    d.ellipse([22*k,12*k,26*k,16*k],fill=(255,240,200))
    im.save('site/'+n)
