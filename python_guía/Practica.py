# Creamos una variable 'player' y le pedimos al jugador su nombre
player = input("Ingresa tu nombre: ")


vida = 100
dinero = 0
inventario = []
jugando = True

while jugando == True:
    print(f"{player} que quieres hacer")
    print(f"dinero: {dinero}")
    print("1.Explorar \n", "2.Ir A la tienda \n", "3. Salir del juego \n")
    value = int(input("Introduce el numero de tu eleccion: "))

    if value == 1: tienda()
    if value == 2: exploracion()
    if value == 3:
        print ("Haz salido del juego")
        jugando = False
    
    if vida <= 0:
        print("You Are Die <3 madafaka")
        jugando = False
    
    def tienda():
        print("----Tienda----")
        
        
    
    def exploracion():
        pass

