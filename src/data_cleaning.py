import pandas as pd
import os

def load_data(file_path):
    """Carga el dataset desde un archivo CSV."""
    try:
        data = pd.read_csv(file_path)
        print("Datos cargados exitosamente.")
        return data
    except FileNotFoundError:
        print(f"Archivo no encontrado: {file_path}")
        return None

def clean_data(data):
    """Limpia el dataset."""
    print("Iniciando limpieza de datos...")
    
    # Eliminar duplicados
    initial_shape = data.shape
    data = data.drop_duplicates()
    print(f"Eliminados {initial_shape[0] - data.shape[0]} duplicados.")
    
    # Manejo de valores nulos
    missing_values = data.isnull().sum()
    print("Valores faltantes por columna antes de limpieza:")
    print(missing_values)
    
    # Rellenar o eliminar según el contexto
    data['item_price'] = data['item_price'].fillna(data['item_price'].mean())
    data = data.dropna(subset=['order_id', 'date'])  # Asegurar que estas columnas clave no tengan nulos
    
    print("Valores faltantes después de limpieza:")
    print(data.isnull().sum())
    
    # Asegurar que la columna 'date' sea de tipo datetime
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    
    # Eliminar filas con fechas inválidas
    data = data.dropna(subset=['date'])
    
    print("Limpieza de datos completada.")
    return data

def save_clean_data(data, output_csv_path, output_excel_path):
    """Guarda el dataset limpio en archivos CSV y Excel."""
    try:
        # Guardar como CSV
        data.to_csv(output_csv_path, index=False)
        print(f"Archivo limpio guardado en CSV: {output_csv_path}")

        # Guardar como Excel
        data.to_excel(output_excel_path, index=False)
        print(f"Archivo limpio guardado en Excel: {output_excel_path}")
    except Exception as e:
        print(f"Error al guardar los archivos: {e}")

if __name__ == "__main__":
    # Ruta de entrada y salida
    input_path = os.path.abspath("C:/Users/pavil/OneDrive/Escritorio/AWS ReStart/Proyecto/AWSproyecto.css/dataset/ventas.csv")
    output_csv_path = os.path.abspath("C:/Users/pavil/OneDrive/Escritorio/AWS ReStart/Proyecto/AWSproyecto.css/dataset/ventas_limpias.csv")
    output_excel_path = os.path.abspath("C:/Users/pavil/OneDrive/Escritorio/AWS ReStart/Proyecto/AWSproyecto.css/dataset/ventas_limpias.xlsx")

    # Cargar datos
    raw_data = load_data(input_path)
    if raw_data is not None:
        # Limpiar datos
        cleaned_data = clean_data(raw_data)  # Renombrado para evitar conflicto
        
        # Guardar datos limpios
        save_clean_data(cleaned_data, output_csv_path, output_excel_path)
