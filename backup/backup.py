"""Copiar o comprimir archivos desde una carpeta de origen a una carpeta de destino.
Comprime los archivos en un .zip y los guarda en una carpeta de respaldo."""

import os
import zipfile
from datetime import datetime
import sys


def obtener_fecha():
    "Obtiene la fecha actual en formato YYYY-MM-DD_HH-MM para nombrar el backup"
    fecha_actual = datetime.now()
    return fecha_actual.strftime("%Y-%m-%d--%H:%M")


def generar_nombre_backup(nombre_base):
    "Usa la fecha actual y un nombre base para construir el nombre"
    fecha = obtener_fecha()
    nombre = f'{nombre_base}_BACKUP_{fecha}.zip'
    return nombre


def verificar_directorio(ruta):
    """Verifica que exista la carpeta origen de la que se quiere hacer backup.
    Si no existe, muestra un error y termina."""
    if not os.path.isdir(ruta):
        raise FileNotFoundError(f"{ruta} NO EXISTE")


def comprimir_directorio(origen, destino, nombre_zip):
    """Crea el archivo .zip en la carpeta destino.
    Recorre el directorio origen (incluso subcarpetas).
    Agrega cada archivo al .zip, manteniendo la estructura."""
    ruta_zip = os.path.join(destino, nombre_zip)
    with zipfile.ZipFile(ruta_zip, mode='w', compression=zipfile.ZIP_DEFLATED) as zipf:
        for carpeta, subcarpetas, archivos in os.walk(origen):
            for archivo in archivos:
                ruta_completa = os.path.join(carpeta, archivo)
                ruta_relativa = os.path.relpath(ruta_completa, origen)
                zipf.write(ruta_completa, arcname=ruta_relativa)


def guardar_log(nombre_zip, destino_log):
    """Guarda un registro del backup en un archivo de log dentro del destino."""

    ruta_zip = os.path.join(destino_log, nombre_zip)

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    if os.path.exists(ruta_zip):
        tamaño_bytes = os.path.getsize(ruta_zip)
        tamaño_mb = tamaño_bytes / (1024 * 1024)
    else:
        tamaño_mb = 0

    try:
        with zipfile.ZipFile(ruta_zip, 'r') as archivo_zip:
            cantidad_archivos = len(archivo_zip.namelist())
    except:
        cantidad_archivos = 0

    mensaje = f"[{fecha}] Backup creado: {nombre_zip} (archivos: {cantidad_archivos}, tamaño: {tamaño_mb:.2f} MB)\n"

    ruta_log = os.path.join(destino_log, "backup.log")

    with open(ruta_log, "a", encoding="utf-8") as log:
        log.write(mensaje)

    print("Registro guardado en:", ruta_log)


def main():
    "MAIN que integra las demas funciones"
    if len(sys.argv) != 3:
        print("Uso: python3 backup.py <origen> <destino>")
        sys.exit(1)

    origen = sys.argv[1]
    destino = sys.argv[2]

    verificar_directorio(origen)
    verificar_directorio(destino)

    nombre_zip = generar_nombre_backup(os.path.basename(origen))

    comprimir_directorio(origen, destino, nombre_zip)

    guardar_log(nombre_zip, destino)

    print(f"✅ Backup creado correctamente: {nombre_zip}")

if __name__ == "__main__":
    main()
