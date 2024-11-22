import qrcode
img = qrcode.make('https://technologychannel.org/')
type(img)  # qrcode.image.pil.PilImage
img.save("brp.png")