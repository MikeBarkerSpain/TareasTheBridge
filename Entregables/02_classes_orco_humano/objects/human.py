class Humano ():
    def __init__(self, nombre,  nivel, armadura, ataque, ojos=2, piernas=2,dientes=32, salud =100):
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.salud = salud

    def atacar (self, orco):
        if orco.armadura < self.ataque:
            orco.salud = orco.salud + orco.armadura - self.ataque

    def no_vivo (self):
        if self.salud <= 0:
            return True 
        else:
            return False

    def resumen (self):
        return str(self.ojos) + " | " + str(self.piernas) + " | " + str(self.dientes) + " | " + self.nombre + " | " + str(self.armadura) + " | " + str(self.nivel) + " | " + str(self.ataque) + " | " + str(self.salud)