class Automovil:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def avanzar(self):
        print("El coche avanza y es un: " + self.marca)
    
    def retroceder (self):
        print("El coche retrocede y es de color: " + self.color)
        
if __name__ == "__main__":
        auto = Automovil("Honda", "Azul") #Crea, objeto, se inicia la instancia
        auto.avanzar()
        auto.retroceder()
        
        auto2 = Automovil("Nissan", "Blanco") #Crea, objeto, se inicia la instancia
        auto2.retroceder()
        auto2.avanzar()
