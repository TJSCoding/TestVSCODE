datei = open("D:/vscode/Sprichtwort.txt", encoding="utf-8")
#inhalt = datei.read()
#print(inhalt)
zeilen = datei.readlines()
print(zeilen)
datei.seek(20)
datei.write("Test")
datei.flush()
einkauf = ["Eier","Milch","Mehr"]
datei.write("\n".join(einkauf))
datei.write("\n-----\n")
datei.writelines(einkauf)

datei.close()
