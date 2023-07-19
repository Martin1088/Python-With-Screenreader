## Rätsel 
import qrcode
text = "Das Rätsel: Falsches Gold - wer findet es? "
text1 = "Vor Ihnen liegen fünf Beutel mit Gold, die genau gleich aussehen. Jeder von ihnen beinhaltet zehn Goldstücke - doch das Gold in einem der fünf Beutel ist gefälscht. Das echte und das falsche Gold sehen genau gleich aus. Der Einzige Unterschied ist das Gewicht: Die gefälschten Goldstücke wiegen jeweils 1,1 Gramm und die echten Goldstücke je ein Gramm."
text2 = "Glücklicherweise besitzen Sie eine sehr genaue digitale Waage, die Sie jedoch nur einmal benutzen dürfen. Wie finden Sie heraus, in welchem der Beutel ist?"
img = qrcode.make(text + text1 + text2)
type(img)
img.save("qr-img02.jpg")