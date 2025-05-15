import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_data(data):
    # Analiza los datos y devuelve algún resultado (personaliza según tu proyecto)
    summary = data.describe()
    return summary

def load_data(file_path):
    """Carga el dataset desde un archivo CSV."""
    try:
        data = pd.read_csv(file_path)
        print("Datos cargados exitosamente.")
        return data
    except FileNotFoundError:
        print(f"Archivo no encontrado: {file_path}")
        return None

def describe_data(data):
    """Describe la estructura y estadísticas básicas del dataset."""
    print("Estructura del dataset:")
    print(data.info())
    print("\nEstadísticas descriptivas:")
    print(data.describe())

def visualize_data(data):
    """Genera visualizaciones para entender mejor los datos."""
    print("Generando visualizaciones...")

    # Distribución de precios
    plt.figure(figsize=(8, 5))
    sns.histplot(data['item_price'], bins=20, kde=True, color='blue')
    plt.title('Distribución de Precios')
    plt.xlabel('Precio')
    plt.ylabel('Frecuencia')
    plt.show()

    # Distribución de cantidad
    plt.figure(figsize=(8, 5))
    sns.histplot(data['quantity'], bins=20, kde=True, color='green')
    plt.title('Distribución de Cantidad')
    plt.xlabel('Cantidad')
    plt.ylabel('Frecuencia')
    plt.show()

    # Frecuencia por tipo de producto
    plt.figure(figsize=(8, 5))
    sns.countplot(y=data['item_type'], order=data['item_type'].value_counts().index, palette='viridis')
    plt.title('Frecuencia por Tipo de Producto')
    plt.xlabel('Frecuencia')
    plt.ylabel('Tipo de Producto')
    plt.show()

    # Ventas por fecha
    data['date'] = pd.to_datetime(data['date'])
    sales_by_date = data.groupby('date')['transaction_amount'].sum()
    plt.figure(figsize=(10, 6))
    sales_by_date.plot()
    plt.title('Ventas Totales por Fecha')
    plt.xlabel('Fecha')
    plt.ylabel('Monto de la Transacción')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # Ruta al archivo de datos
    input_path = os.path.abspath("C:/Users/pavil/OneDrive/Escritorio/AWS ReStart/Proyecto/AWSproyecto.css/dataset/ventas_limpias.csv")
    
    # Cargar datos
    data = load_data(input_path)
    if data is not None:
        # Describir datos
        describe_data(data)
        
        # Visualizar datos
        visualize_data(data)
