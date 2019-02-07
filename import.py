import Verschluesselung

text = "Treffen heute Nacht am alten Pier"
print("Der Klartext lautet :", text)

geheimtext = Verschluesselung.text_verschluesseln(text)
print("Verschlüsselter Tex:", geheimtext)

klartext = Verschluesselung.text_entschluesseln(geheimtext)
print("Entschüsselter Text:",klartext)

