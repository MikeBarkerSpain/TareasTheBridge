class flota ():
    def __init__(self, max2x1, max3x1, max4x1, max5x1):
        self.max2x1 = max2x1
        self.max3x1 = max3x1
        self.max4x1 = max4x1
        self.max5x1 = max5x1

        self.listabarcos = []


tryfleet = flota(4,3,2,1)
print(tryfleet.max2x1)