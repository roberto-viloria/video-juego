import random
from abc import ABC, abstractmethod

# =========================
# CLASE ABSTRACTA: Personaje
# =========================
class Personaje(ABC):
    def __init__(self, nombre: str, vida: int, ataque: int, defensa: int):
        self._nombre = nombre
        self.vida = vida
        self._ataque = ataque
        self._defensa = defensa

    # --- GETTERS Y SETTERS ---
    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def vida(self) -> int:
        return self._vida

    @vida.setter
    def vida(self, valor: int):
        if valor < 0:
            self._vida = 0
        elif valor > 100:
            self._vida = 100
        else:
            self._vida = valor

    @property
    def ataque(self) -> int:
        return self._ataque

    @ataque.setter
    def ataque(self, valor: int):
        self._ataque = valor

    @property
    def defensa(self) -> int:
        return self._defensa

    @defensa.setter
    def defensa(self, valor: int):
        self._defensa = valor

    # --- MÉTODOS ---
    @abstractmethod
    def atacar(self, objetivo: 'Personaje'):
        pass

    def recibir_danio(self, danio: int):
        self.vida -= danio
        print(f"{self.nombre} recibe {danio} puntos de daño. (Vida restante: {self.vida}/100)")

    def mostrar_estado(self):
        print(f"{self.nombre} | Vida: {self.vida} | Ataque: {self.ataque} | Defensa: {self.defensa}")


# =========================
# SUBCLASES
# =========================
class Guerrero(Personaje):
    def atacar(self, objetivo: Personaje):
        danio_base = self.ataque * 1.2
        danio_final = max(1, int(danio_base - objetivo.defensa))
        print(f"[Guerrero] {self.nombre} realiza un ataque poderoso (+20% de fuerza)")
        objetivo.recibir_danio(danio_final)

class Mago(Personaje):
    def atacar(self, objetivo: Personaje):
        danio_final = self.ataque
        print(f"[Mago] {self.nombre} lanza un hechizo que ignora la defensa de {objetivo.nombre}")
        objetivo.recibir_danio(danio_final)

class Arquero(Personaje):
    def atacar(self, objetivo: Personaje):
        if self.ataque > objetivo.defensa:
            danio_base = self.ataque * 2
            print(f"[Arquero] {self.nombre} encuentra una debilidad: ¡DAÑO DOBLE!")
        else:
            danio_base = self.ataque
            print(f"[Arquero] {self.nombre} dispara una flecha estándar")
        danio_final = max(1, int(danio_base - objetivo.defensa))
        objetivo.recibir_danio(danio_final)


# =========================
# SISTEMA DE COMBATE
# =========================
def iniciar_combate(p1: Personaje, p2: Personaje):
    print("=" * 60)
    print(f"⚔️ COMIENZA EL DUELO ⚔️")
    print(f"{p1.nombre} vs {p2.nombre}")
    print("=" * 60)

    print("\n--- ESTADO INICIAL ---")
    p1.mostrar_estado()
    p2.mostrar_estado()

    turno = 1
    while p1.vida > 0 and p2.vida > 0:
        print(f"\n--- TURNO {turno} ---")
        atacante, defensor = p1, p2
        atacante.atacar(defensor)
        print("\nEstado después del ataque:")
        p1.mostrar_estado()
        p2.mostrar_estado()

        if defensor.vida <= 0:
            print(f"\n{defensor.nombre} ha sido derrotado")
            print(f"🏆 ¡{atacante.nombre} gana la batalla! 🏆")
            break

        # Alternar turnos
        p1, p2 = p2, p1
        turno += 1


# =========================
# EJEMPLO DE USO
# =========================
if __name__ == "__main__":
    # NOMBRES MODIFICADOS
    valeria = Guerrero(nombre="Valeria la Invencible", vida=100, ataque=30, defensa=20)
    arkan = Mago(nombre="Arkan el Sabio", vida=80, ataque=40, defensa=10)

    iniciar_combate(valeria, arkan)