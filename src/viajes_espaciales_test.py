def test_poder_viajar_entrada_usuario():
    edad = int(input("Dame tu edad: "))
    fisico = int(input("Dame tu nivel físico [1-10]: "))
    if edad < 18:
        print("Debes ser mayor de edad")
    elif fisico < 5:
        print("Debes estar en mejor forma")
    else:
        print("Puedes viajar")

def calcula_dias(distancia_km, velocidad_kmh):
    tiempo_horas = distancia_km / velocidad_kmh
    tiempo_dias = tiempo_horas / 24
    return tiempo_dias

def test_calcula_dias(distancia_km, velocidad_kmh):
    tiempo_dias = calcula_dias(distancia_km, velocidad_kmh)
    print(f"Tardarías {tiempo_dias} días en llegar.")

def test_simulacion():
    distancia_kms = 225000000
    for velocidad in range(10000, 50001, 10000):
        dias = calcula_dias(distancia_kms, velocidad)
        print(f"Velocidad: {velocidad} km/h -> Tiempo: {dias} días")


def test_calcula_dias_entrada_usuario():
    distancia_km = input("Dame la distancia en kms: ")
    distancia_km = int(distancia_km)
    velocidad_kmh = input("Velocidad del cohete en km/h: ")
    velocidad_kmh = int(velocidad_kmh)
    test_calcula_dias(distancia_km, velocidad_kmh)

def test_simulacion_por_usuario():
    opcion = "s"
    while opcion == "s":
        test_calcula_dias_entrada_usuario()
        opcion = input("Quieres hacer simulacion? [s/n]: ")

#if __name__ == "__main__":
    
    # distancia Tierra - Luna
    # test_calcula_dias(384400, 5000)

    # distancia Tierra - Marte
    #test_calcula_dias(225000000, 5000)

    #test_calcula_dias_entrada_usuario()
    
    #test_poder_viajar_entrada_usuario()
    #test_simulacion()
test_simulacion_por_usuario()
        