## qrcode test
import qrcode

text="""Hier ist der
 Schatz
 versteckt """
img = qrcode.make(text)
print(type(img))
img.save("schatz.jpg")
