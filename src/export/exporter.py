import csv
import os
from datetime import datetime


def export_to_csv(data, filename_prefix="results"):
    if not data:
        print("No hay datos para exportar")
        return

    # 🔥 crear carpeta outputs si no existe
    os.makedirs("outputs", exist_ok=True)

    # 🔥 nombre dinámico
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/{filename_prefix}_{timestamp}.csv"

    # 🔥 obtener headers dinámicamente
    headers = data[0].keys()

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()
        writer.writerows(data)

    print(f"\n✔ Archivo exportado: {filename}")