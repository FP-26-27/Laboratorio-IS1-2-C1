from piedra_papel_tijeras import *

def test_ordenador_decide_jugada():
    '''
    Test para la función ordenador_decide_jugada.
    '''
    print("Testeando ordenador_decide_jugada...")
    eleccion = ordenador_decide_jugada()
    print(f"El ordenador eligió: {eleccion} \n")

def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario

def test_usuario_decide_jugada():
    '''
    Test para la función usuario_decide_jugada.
    '''
    print("Testeando usuario_decide_jugada...")
    usuario_decide_jugada()
    print()

def test_determina_ganador(eleccion_usuario, eleccion_ordenador):
    '''
    Test para la función determina_ganador.
    '''
    print("Testeando determina_ganador...")        
    print(f"Jugador: {eleccion_usuario} vs. Ordenador: {eleccion_ordenador}")
    resultado = determina_ganador(eleccion_usuario, eleccion_ordenador)
    print("Resultado:", resultado)
    print()

def jugar_ronda():
    '''Muestre un mensaje de bienvenida
    Haga que el ordenador decida su jugada
    Haga que el jugador decida su jugada
    Muestre un mensaje indicando la elección del ordenador
    Determine quién es el ganador
    Muestre un mensaje con el resultado de la ronda.'''
    result = None
    print("Inicio de nueva ronda...")
    jugada_ordenador = ordenador_decide_jugada()
    jugada_usuario = usuario_decide_jugada()
    print("El ordenador eligió: ", jugada_ordenador)
    resultado = determina_ganador(jugada_usuario, jugada_ordenador)
    if resultado == -1:
        print("El ordenador ganó!!!")
        result = (0, 1)
    elif resultado == 1:
        print("El humano ganó!!!")
        result = (1, 0)
    else: 
        print("Gran empate...")
        result = (0, 0)
    return result

def jugar_torneo(max_puntos:int)->None:
    print("Bienvenido a mi primer videojuego: PiedraPapelTijering")
    puntos_jugador, puntos_ordenador = 0, 0
    while puntos_jugador < max_puntos and puntos_ordenador < max_puntos:
        p_jug, p_ord = jugar_ronda()
        puntos_jugador += p_jug
        puntos_ordenador += p_ord
    if puntos_jugador>puntos_ordenador:
        print("El humano ha ganado!!")
    else:
        print("El humano ha perdio lamentablemente...")


# Función principal
if __name__ == "__main__":
    #test_ordenador_decide_jugada()
    #test_usuario_decide_jugada()
    #test_determina_ganador("piedra", "tijeras")
    #test_determina_ganador("piedra", "papel")
    #test_determina_ganador("piedra", "piedra")
    #test_determina_ganador("tijeras", "tijeras")
    #test_determina_ganador("tijeras", "papel")
    #test_determina_ganador("tijeras", "piedra")
    #test_determina_ganador("papel", "tijeras")
    #test_determina_ganador("papel", "papel")
    #test_determina_ganador("papel", "piedra")
    #jugar_ronda()
    jugar_torneo(2)