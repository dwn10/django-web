import random

# Liste der Zeichenfolgennamen
namen = ["A.D.", "NEA.", "A.F.", "CHG.", "Μ.K.", "SLC.", "NCM.", "Α.M.",
         "M.MA.", "DM.", "М.Mw.", "G.A.", "D.P.", "A.Pd.", "A.Pt.", "F.R.",
         "AS.", "I.S.", "E.S.", "N.V.", "A.Y", "C.Z."]

# Wähle zufälligen Index
zufalls_index = random.randint(0, len(namen) - 1)

# Wähle den Namen an der zufälligen Position
ausgewaehlter_name = namen[zufalls_index]

# Ausgabe des ausgewählten Namens
print("--------------------------"),
print("Zufälliger Name:", ausgewaehlter_name)