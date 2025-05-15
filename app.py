import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Función para cargar el modelo
@st.cache_resource
def load_model(model_path):
    return joblib.load(model_path)

# Función para cargar datos
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Función para predecir tendencias
def predict_sales(model, day_of_week, month, item_names):
    # Crear un DataFrame con las características seleccionadas
    input_data = pd.DataFrame({
        "day_of_week": [day_of_week] * len(item_names),
        "month": [month] * len(item_names),
    })
    predictions = model.predict(input_data)
    return pd.DataFrame({
        "item_name": item_names,
        "predicted_quantity": predictions
    }).sort_values(by="predicted_quantity", ascending=False)

# Configurar la app de Streamlit
def main():
    st.title("Predicción de Tendencias")
    st.sidebar.header("Configuración de Predicción")
    
    # Ruta del modelo y datos
    model_path ="C:/Users/pavil/OneDrive/Escritorio/AWS ReStart/Proyecto/AWSproyecto.css/model/modelo_ventas.pkl"
    data_path ="C:/Users/pavil/OneDrive/Escritorio/AWS ReStart/Proyecto/AWSproyecto.css/dataset/ventas_limpias.csv"
    
    # Cargar modelo y datos
    model = load_model(model_path)
    data = load_data(data_path)

    # Obtener lista única de platos/bebidas
    item_names = data["item_name"].unique()

    # Seleccionar características para la predicción
    day_of_week = st.sidebar.selectbox("Día de la semana", options=[0, 1, 2, 3, 4, 5, 6], format_func=lambda x: ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"][x])
    month = st.sidebar.selectbox("Mes", options=range(1, 13), format_func=lambda x: f"Mes {x}")

    # Realizar predicciones
    if st.sidebar.button("Predecir"):
        st.subheader("Resultados de la Predicción")
        predictions = predict_sales(model, day_of_week, month, item_names)

        # Mostrar resultados en tabla
        st.write(predictions)

        # Visualizar los platos más vendidos
        top_items = predictions.head(10)
        fig, ax = plt.subplots()
        ax.barh(top_items["item_name"], top_items["predicted_quantity"], color="skyblue")
        ax.set_xlabel("Cantidad Predicha")
        ax.set_ylabel("Plato/Bebida")
        ax.set_title("Top 10 Platos/Bebidas Más Vendidos")
        ax.invert_yaxis()
        st.pyplot(fig)

if __name__ == "__main__":
    main()
