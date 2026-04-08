import pandas as pd
import time

def consultar_onpe(dni):
    # Aquí iría la lógica de scraping.
    # Para el ejercicio, simularemos una respuesta.
    print(f"Consultando DNI: {dni}...")
    time.sleep(1) # Simula tiempo de espera de red
    return "NO" if int(str(dni)[-1]) % 2 == 0 else "SI"

def procesar_caso():
    archivo_entrada = 'datos_reniec.xlsx' # CAMBIA ESTO por el nombre de tu archivo
    archivo_salida = 'resultado_final.xlsx'
    try:
        df = pd.read_excel(archivo_entrada)

        # Asumiendo que la columna se llama 'dni'
        if 'dni' in df.columns:
            df['miembro de mesa'] = df['dni'].apply(consultar_onpe)
            df['ubicación'] = 'Lima/Lima/Miraflores' # Dato de ejemplo
            df['direccion'] = 'Calle Ejemplo 123'    # Dato de ejemplo
            df.to_excel(archivo_salida, index=False)
            print(f"✅ Proceso terminado. Archivo guardado como: {archivo_salida}")
        else:
            print("❌ Error: No se encontró la columna 'dni' en el Excel.")

    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")

if __name__ == "__main__":
    procesar_caso()
