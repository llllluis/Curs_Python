# main.py
from estado import contadores

# Simula diferentes acciones
contadores.incrementar("visitas")
contadores.incrementar("visitas")
contadores.incrementar("descargas")

contadores.mostrar("visitas")     # visitas: 2
contadores.mostrar("descargas")   # descargas: 1

# Puedes también resetear un contador si quieres
# contadores.resetear("visitas")