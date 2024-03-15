class Fahrzeug:
    def __init__(self, geschwindigkeit=3):
        self.geschwindigkeit = geschwindigkeit

    def beschleunigen(self, wert):
        if isinstance(wert, (int, float)):
            if wert > 0:
                self.geschwindigkeit += wert
            else:
                print("Der Beschleunigungswert muss größer als Null sein.")
        else:
            print("Der Beschleunigungswert muss eine Zahl sein.")

    def bremsen(self, wert):
        if isinstance(wert, (int, float)):
            if wert > 0 and wert <= self.geschwindigkeit:
                self.geschwindigkeit -= wert
            else:
                print("Der Bremswert muss größer Null und kleiner oder gleich der aktuellen Geschwindigkeit sein.")
        else:
            print("Der Bremswert muss eine Zahl sein.")

    def ausgabe(self):
        print("Geschwindigkeit:", self.geschwindigkeit)

volvo = Fahrzeug()
opel = Fahrzeug()
volvo.ausgabe()
volvo.beschleunigen(20)
volvo.ausgabe()
volvo.bremsen(10)
volvo.ausgabe()
opel.ausgabe()