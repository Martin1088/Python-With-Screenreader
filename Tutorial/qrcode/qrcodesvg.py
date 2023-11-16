## Rasel
import qrcode
import qrcode.image.svg
f = qrcode.image.svg.SvgPathImage
img = qrcode.make("import qwcode")
img.save("test.svg")

