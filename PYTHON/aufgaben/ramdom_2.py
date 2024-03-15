import random

# Liste der Namen
namen = ["A.D.", "NEA.", "A.F.", "CHG.", "Μ.K.", "SLC.", "NCM.", "Α.M.",
         "M.MA.", "DM.", "М.Mw.", "G.A.", "D.P.", "A.Pd.", "A.Pt.", "F.R.",
         "AS.", "I.S.", "E.S.", "N.V.", "A.Y.", "C.Z."]

# Zufällige Anordnung der Namen
random.shuffle(namen)

# Ausgabe der neugeordneten Liste
print("\n--------------------------"),
print("Zufällige Reihenfolge:")
for name in namen:
    print(name)

# Alternative Ausgabe mit Formatierung
print("\n--------------------------"),
print("Alternative Ausgabe:")
print(", ".join(namen))