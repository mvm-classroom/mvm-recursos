velocitat_nusos = int(input("Indica la velocitat (en nusos): "))
temps_vol = int(input("Indica el temps de vol (en minuts): "))

# 1 nus = 1 milla nàutica per hora
# 1 milla nàutica = 1,852 Km
velocitat_kmh = velocitat_nusos * 1.852

# Si multiplico el temps per la velocitat en km/h:
#   obtindré distància en Km
distancia_recorreguda_en_km = velocitat_kmh * (temps_vol / 60)

# Si multiplico el temps per la velocitat en nusos:
#   obtindré distància en milles nàutiques
#   aquesta dada no la necessitem, es "pa hacerme el chulo"
distancia_recorreguda_en_milles_nautiques = velocitat_nusos * (temps_vol / 60)

print("La nostra aeronau ha viatjat durant", temps_vol, "minuts a",
      velocitat_nusos, "nusos, de manera que ha recorregut",
      distancia_recorreguda_en_km, "Km")