# estado.py
import json
import os
from datetime import datetime

class Contadores:
    def __init__(self, archivo="contadores.json"):
        self.archivo = archivo
        self.datos = self._cargar()

    def _cargar(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                return json.load(f)
        return {}

    def _guardar(self):
        with open(self.archivo, "w") as f:
            json.dump(self.datos, f, indent=2)

    def incrementar(self, nombre):
        ahora = datetime.now().isoformat(timespec='seconds')
        if nombre not in self.datos:
            self.datos[nombre] = {
                "total": 0,
                "historial": []
            }

        self.datos[nombre]["total"] += 1
        self.datos[nombre]["historial"].append(ahora)
        self._guardar()

    def mostrar(self, nombre):
        if nombre in self.datos:
            total = self.datos[nombre]["total"]
            print(f"{nombre}: {total} veces")
            print("Historial:")
            for t in self.datos[nombre]["historial"]:
                print(f"  - {t}")
        else:
            print(f"{nombre} no tiene registros aún.")

    def resetear(self, nombre):
        if nombre in self.datos:
            self.datos[nombre]["total"] = 0
            self.datos[nombre]["historial"] = []
            self._guardar()

# Instancia global
contadores = Contadores()
