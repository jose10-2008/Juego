import random

# Clase base
class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self._vida = vida
        self.ataque = ataque

    @property
    def vida(self):
        return self._vida

    def recibir_danio(self, d):
        self._vida = max(0, self._vida - d)

    def esta_vivo(self):
        return self._vida > 0

    def atacar(self, enemigo):
        enemigo.recibir_danio(self.ataque)
        print(f"{self.nombre} hace {self.ataque} daño")

    def habilidad(self, enemigo):
        pass


class Guerrero(Personaje):
    def __init__(self, n): super().__init__(n, 110, 14)
    def habilidad(self, e):
        d = self.ataque + 8
        e.recibir_danio(d)
        print(f"{self.nombre} usa golpe fuerte ({d})")


class Mago(Personaje):
    def __init__(self, n):
        super().__init__(n, 85, 12)
        self.mana = 40

    def habilidad(self, e):
        if self.mana >= 10:
            d = self.ataque + 12
            self.mana -= 10
            e.recibir_danio(d)
            print(f"{self.nombre} lanza hechizo ({d})")
        else:
            self.atacar(e)


class Arquero(Personaje):
    def __init__(self, n): super().__init__(n, 95, 13)
    def habilidad(self, e):
        d = self.ataque * 2 if random.random() < 0.4 else self.ataque + 5
        e.recibir_danio(d)
        print(f"{self.nombre} dispara ({d})")


def batalla(j, e):
    while j.esta_vivo() and e.esta_vivo():
        print(f"\n{j.nombre}: {j.vida} | {e.nombre}: {e.vida}")
        op = input("1.Atacar 2.Habilidad: ")

        (j.atacar if op == "1" else j.habilidad)(e)

        if e.esta_vivo():
            random.choice([e.atacar, e.habilidad])(j)

    print("👑 𝗚𝗔𝗡𝗔𝗗𝗢𝗥 👑:", j.nombre if j.esta_vivo() else e.nombre)


def main():
    print("===================================")
    print("⚔️ GUARDIANS OF THE ANCIENT KINGDOM ⚔️")
    print("===================================")

    nombre = input("Nombre: ")
    clases = {"1": Guerrero, "2": Mago, "3": Arquero}

    print("\n1.Guerrero 2.Mago 3.Arquero")
    jugador = clases.get(input("Elige: "), Guerrero)(nombre)

    enemigo = random.choice([Guerrero("Orco"), Mago("Brujo"), Arquero("Cazador")])

    print(f"\nTe enfrentas a: {enemigo.nombre}")

    batalla(jugador, enemigo)


main()