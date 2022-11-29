import pickle


class Vehiculo:
    def __init__(self, tipo, marca):
        self.tipo = tipo
        self.marca = marca

    def getMarca(self):
        return(self.marca)


vehiculo1 = Vehiculo("automovil", "BMW")

f = open('fichero.bin','wb')
pickle.dump(vehiculo1, f)
f.close()

f = open('fichero.bin', 'rb')
vehiculo2 = pickle.load(f)
f.close()
print(vehiculo2.getMarca())